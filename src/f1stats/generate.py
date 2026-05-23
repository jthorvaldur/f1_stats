import json
from pathlib import Path
from datetime import date, datetime
from jinja2 import Environment, FileSystemLoader

from . import api, static_data
from . import coherence as coh
from . import profiles as prof
from . import markets
from . import calendar_data as cal

ROOT = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = ROOT / "templates"
DOCS_DIR = ROOT / "docs"


def build_template_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["team_color"] = lambda tid: static_data.get_team_color(tid)["hex"]
    env.filters["team_css"] = lambda tid: static_data.get_team_color(tid)["css"]
    env.filters["team_display"] = static_data.get_team_display
    env.filters["tojson"] = lambda v: json.dumps(v)
    return env


def compute_age(dob_str: str, ref_date: date) -> int | None:
    if not dob_str:
        return None
    dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
    age = ref_date.year - dob.year
    if (ref_date.month, ref_date.day) < (dob.month, dob.day):
        age -= 1
    return age


def enrich_data(data: dict) -> dict:
    if data["races"]:
        season_start = datetime.strptime(data["races"][0]["date"], "%Y-%m-%d").date()
    else:
        season_start = date(data["year"], 3, 1)

    for d in data["drivers"]:
        d["team_hex"] = static_data.get_team_color(d["team_id"])["hex"]
        d["team_css"] = static_data.get_team_color(d["team_id"])["css"]
        d["team_display"] = static_data.get_team_display(d["team_id"])

        driver_id = d["code"].lower() if d["code"] else d["family_name"].lower()
        for did, info in data["driver_info"].items():
            if info.get("code", "").lower() == d["code"].lower():
                driver_id = did
                break

        d["driver_id"] = driver_id
        d["age"] = compute_age(d["dob"], season_start)

        phys = static_data.DRIVER_WEIGHTS.get(driver_id, {})
        d["weight_kg"] = phys.get("weight")
        d["height_cm"] = phys.get("height")
        d["bmi"] = round(phys["weight"] / (phys["height"] / 100) ** 2, 1) if phys.get("weight") and phys.get("height") else None
        d["ballast"] = max(0, static_data.MIN_DRIVER_WEIGHT - phys.get("weight", 80) - 3) if phys.get("weight") else None
        d["debut_year"] = static_data.DEBUT_YEARS.get(driver_id)
        d["debut_age"] = compute_age(d["dob"], date(d["debut_year"], 3, 1)) if d["debut_year"] and d["dob"] else None
        d["f1_seasons"] = data["year"] - d["debut_year"] + 1 if d["debut_year"] else None

    for c in data["constructors"]:
        c["team_hex"] = static_data.get_team_color(c["team_id"])["hex"]
        c["team_css"] = static_data.get_team_color(c["team_id"])["css"]
        c["team_display"] = static_data.get_team_display(c["team_id"])
        car = static_data.CAR_WEIGHTS.get(c["team_id"], {})
        c["car_weight"] = car.get("weight")
        c["car_over"] = car.get("over")

    for race in data["races"]:
        for r in race["results"]:
            r["team_hex"] = static_data.get_team_color(r["team_id"])["hex"]
            r["team_css"] = static_data.get_team_color(r["team_id"])["css"]
            r["is_retired"] = r["status"] not in ("Finished", "") and "Lap" not in r["status"]
            r["is_lapped"] = "Lap" in r.get("status", "")
            r["is_dns"] = r["status"] == "Did not start" or r.get("grid") == "0"

    max_pts = data["drivers"][0]["points"] if data["drivers"] else 1
    for d in data["drivers"]:
        d["progress_pct"] = round(d["points"] / max_pts * 100) if max_pts else 0

    max_cpts = data["constructors"][0]["points"] if data["constructors"] else 1
    for c in data["constructors"]:
        c["progress_pct"] = round(c["points"] / max_cpts * 100) if max_cpts else 0

    cumulative = {}
    for race in data["races"]:
        for r in race["results"]:
            key = r["driver"]
            cumulative.setdefault(key, [])
            prev = cumulative[key][-1] if cumulative[key] else 0
            cumulative[key].append(prev + r["points"])

    data["cumulative_points"] = cumulative
    data["season_start"] = season_start.isoformat()
    data["remaining_rounds"] = data["total_rounds"] - data["current_round"]
    data["min_car_weight"] = static_data.MIN_CAR_WEIGHT
    data["min_driver_weight"] = static_data.MIN_DRIVER_WEIGHT

    for d in data["drivers"]:
        did = d.get("driver_id", "")
        profile = prof.DRIVER_PROFILES.get(did, {})
        d["profile"] = profile
        budget_info = prof.TEAM_BUDGETS.get(d["team_id"], {})
        d["team_budget_m"] = budget_info.get("budget_m")

    for c in data["constructors"]:
        budget_info = prof.TEAM_BUDGETS.get(c["team_id"], {})
        c["budget_m"] = budget_info.get("budget_m")
        c["staff"] = budget_info.get("staff")
        c["factory"] = budget_info.get("factory", "")
        c["pts_per_million"] = round(c["points"] / budget_info["budget_m"], 2) if budget_info.get("budget_m") and c["points"] else 0

    return data


PAGES = [
    "index.html",
    "races.html",
    "age.html",
    "weight.html",
    "progression.html",
    "halo.html",
    "montecarlo.html",
    "entropy.html",
    "elo.html",
    "nonlinear.html",
    "coherence.html",
    "prediction.html",
    "economics.html",
    "seasonality.html",
    "profiles.html",
    "qualifying.html",
    "markets.html",
    "rules.html",
    "format.html",
    "circuits.html",
]


def generate_all(year: int | None = None) -> None:
    print(f"Fetching {year or 'current'} season data...")
    data = api.get_season_data(year)
    print(f"  Round {data['current_round']}: {len(data['drivers'])} drivers, {len(data['races'])} races")

    print("Enriching data...")
    data = enrich_data(data)

    print("Fetching historical standings (2010-2025)...")
    historical = api.get_historical_standings()
    hist_analysis = {}
    for yr, hdata in historical.items():
        pts = [d["points"] for d in hdata["standings"]]
        hist_analysis[int(yr)] = {
            "round": hdata["round"],
            "standings": hdata["standings"],
            "gini": round(coh.compute_gini(pts), 4),
            "hhi": round(coh.compute_hhi(pts), 4),
            "total_points": sum(pts),
            "n_drivers": len(pts),
        }
    data["historical"] = hist_analysis

    current_pts = [d["points"] for d in data["drivers"]]
    data["gini"] = round(coh.compute_gini(current_pts), 4)
    data["hhi"] = round(coh.compute_hhi(current_pts), 4)

    print("Computing Δ.72 coherence scores...")
    data["coherence"] = coh.compute_f1_coherence(data["cumulative_points"], data["drivers"])

    print("Fetching next race info...")
    data["next_race"] = api.get_next_race(data["year"], data["current_round"])

    data["budgets"] = prof.TEAM_BUDGETS
    data["circuit_types"] = prof.CIRCUIT_TYPES
    data["driver_profiles"] = prof.DRIVER_PROFILES
    data["calendar"] = cal.CALENDAR_2026
    data["regulation_changes"] = cal.REGULATION_CHANGES
    data["weekend_format"] = cal.RACE_WEEKEND_FORMAT
    data["circuit_details"] = cal.CIRCUIT_DETAILS

    print("Fetching prediction market odds...")
    if data["next_race"]:
        data["race_odds"] = markets.get_race_odds(data["next_race"]["date"])
    else:
        data["race_odds"] = []
    data["championship_odds"] = markets.get_championship_odds()

    env = build_template_env()
    DOCS_DIR.mkdir(exist_ok=True)

    for page in PAGES:
        template_path = page
        if not (TEMPLATES_DIR / template_path).exists():
            print(f"  SKIP {page} (no template)")
            continue
        template = env.get_template(template_path)
        html = template.render(data=data, d=data)
        (DOCS_DIR / page).write_text(html)
        print(f"  OK   {page}")

    data_json = {
        "year": data["year"],
        "current_round": data["current_round"],
        "generated": data["generated"],
        "drivers": data["drivers"],
        "constructors": data["constructors"],
        "races": [
            {
                "round": r["round"],
                "name": r["name"],
                "date": r["date"],
                "circuit": r["circuit"],
                "results": [
                    {"position": res["position"], "driver": res["driver"],
                     "team": res["team"], "points": res["points"], "status": res["status"]}
                    for res in r["results"]
                ],
            }
            for r in data["races"]
        ],
    }
    (DOCS_DIR / "data.json").write_text(json.dumps(data_json, indent=2))
    print(f"  OK   data.json")

    generate_sitemap(data)
    print("Done.")


def generate_sitemap(data: dict) -> None:
    base = "https://jthorvaldur.github.io/f1_stats"
    urls = [f"{base}/"] + [f"{base}/{p}" for p in PAGES]
    entries = "\n".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{data['generated']}</lastmod>\n  </url>"
        for u in urls
    )
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n'
    (DOCS_DIR / "sitemap.xml").write_text(xml)
