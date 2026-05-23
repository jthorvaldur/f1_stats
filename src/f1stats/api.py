import json
import httpx
from datetime import date
from pathlib import Path

BASE = "https://api.jolpi.ca/ergast/f1"
CACHE_DIR = Path(__file__).resolve().parent.parent.parent / "data"


def fetch_json(path: str) -> dict:
    url = f"{BASE}/{path}"
    r = httpx.get(url, timeout=30)
    r.raise_for_status()
    return r.json()


def get_season_data(year: int | None = None) -> dict:
    year = year or date.today().year

    standings = fetch_json(f"{year}/driverStandings.json")
    sl = standings["MRData"]["StandingsTable"]["StandingsLists"]
    current_round = int(sl[0]["round"]) if sl else 0

    drivers_raw = sl[0]["DriverStandings"] if sl else []
    drivers = []
    for d in drivers_raw:
        info = d["Driver"]
        constructor = d["Constructors"][0] if d["Constructors"] else {}
        drivers.append({
            "position": int(d["position"]),
            "name": f"{info['givenName']} {info['familyName']}",
            "given_name": info["givenName"],
            "family_name": info["familyName"],
            "code": info.get("code", ""),
            "dob": info.get("dateOfBirth", ""),
            "nationality": info.get("nationality", ""),
            "number": info.get("permanentNumber", ""),
            "points": float(d["points"]),
            "wins": int(d["wins"]),
            "team": constructor.get("name", ""),
            "team_id": constructor.get("constructorId", ""),
        })

    constructor_data = fetch_json(f"{year}/constructorStandings.json")
    cl = constructor_data["MRData"]["StandingsTable"]["StandingsLists"]
    constructors_raw = cl[0]["ConstructorStandings"] if cl else []
    constructors = []
    for c in constructors_raw:
        constructors.append({
            "position": int(c["position"]),
            "name": c["Constructor"]["name"],
            "team_id": c["Constructor"]["constructorId"],
            "points": float(c["points"]),
            "wins": int(c["wins"]),
        })

    results_data = fetch_json(f"{year}/results.json?limit=600")
    races_raw = results_data["MRData"]["RaceTable"]["Races"]
    races = []
    for race in races_raw:
        results = []
        for r in race.get("Results", []):
            results.append({
                "position": r.get("position", ""),
                "number": r["number"],
                "driver": f"{r['Driver']['givenName']} {r['Driver']['familyName']}",
                "code": r["Driver"].get("code", ""),
                "team": r["Constructor"]["name"],
                "team_id": r["Constructor"]["constructorId"],
                "points": float(r.get("points", 0)),
                "status": r.get("status", ""),
                "grid": r.get("grid", ""),
            })
        races.append({
            "round": int(race["round"]),
            "name": race["raceName"],
            "date": race["date"],
            "circuit": race["Circuit"]["circuitName"],
            "circuit_id": race["Circuit"].get("circuitId", ""),
            "location": race["Circuit"]["Location"].get("locality", ""),
            "country": race["Circuit"]["Location"].get("country", ""),
            "results": results,
        })

    all_drivers_data = fetch_json(f"{year}/drivers.json")
    all_drivers_raw = all_drivers_data["MRData"]["DriverTable"]["Drivers"]
    driver_info = {}
    for d in all_drivers_raw:
        driver_info[d["driverId"]] = {
            "dob": d.get("dateOfBirth", ""),
            "nationality": d.get("nationality", ""),
            "number": d.get("permanentNumber", ""),
            "code": d.get("code", ""),
        }

    qualifying = get_qualifying_data(year, current_round)

    return {
        "year": year,
        "current_round": current_round,
        "total_rounds": 24,
        "drivers": drivers,
        "constructors": constructors,
        "races": races,
        "driver_info": driver_info,
        "qualifying": qualifying,
        "generated": date.today().isoformat(),
    }


def get_qualifying_data(year: int, rounds: int) -> list[dict]:
    results = []
    for rnd in range(1, rounds + 1):
        try:
            data = fetch_json(f"{year}/{rnd}/qualifying.json")
            races = data["MRData"]["RaceTable"]["Races"]
            if not races:
                continue
            race = races[0]
            qual_results = []
            for q in race.get("QualifyingResults", []):
                qual_results.append({
                    "position": int(q["position"]),
                    "driver": f"{q['Driver']['givenName']} {q['Driver']['familyName']}",
                    "code": q["Driver"].get("code", ""),
                    "team": q["Constructor"]["name"],
                    "team_id": q["Constructor"]["constructorId"],
                    "q1": q.get("Q1", ""),
                    "q2": q.get("Q2", ""),
                    "q3": q.get("Q3", ""),
                })
            results.append({
                "round": rnd,
                "name": race["raceName"],
                "qualifying": qual_results,
            })
        except Exception:
            continue
    return results


def get_historical_standings(years: list[int] | None = None) -> dict:
    if years is None:
        years = list(range(2010, 2026))

    cache_file = CACHE_DIR / "historical.json"
    cached = {}
    if cache_file.exists():
        cached = json.loads(cache_file.read_text())

    result = {}
    for year in years:
        if str(year) in cached:
            result[year] = cached[str(year)]
            continue
        try:
            data = fetch_json(f"{year}/driverStandings.json")
            sl = data["MRData"]["StandingsTable"]["StandingsLists"]
            if not sl:
                continue
            standings = []
            for d in sl[0]["DriverStandings"]:
                standings.append({
                    "position": int(d["position"]),
                    "driver": f"{d['Driver']['givenName']} {d['Driver']['familyName']}",
                    "points": float(d["points"]),
                    "wins": int(d["wins"]),
                    "team": d["Constructors"][0]["name"] if d["Constructors"] else "",
                })
            result[year] = {
                "round": int(sl[0]["round"]),
                "standings": standings,
            }
        except Exception:
            continue

    CACHE_DIR.mkdir(exist_ok=True)
    cache_file.write_text(json.dumps({str(k): v for k, v in result.items()}, indent=2))
    return result


def get_next_race(year: int, current_round: int) -> dict | None:
    try:
        data = fetch_json(f"{year}.json")
        races = data["MRData"]["RaceTable"]["Races"]
        for race in races:
            if int(race["round"]) == current_round + 1:
                return {
                    "round": int(race["round"]),
                    "name": race["raceName"],
                    "date": race["date"],
                    "circuit": race["Circuit"]["circuitName"],
                    "circuit_id": race["Circuit"]["circuitId"],
                    "location": race["Circuit"]["Location"].get("locality", ""),
                    "country": race["Circuit"]["Location"].get("country", ""),
                }
    except Exception:
        pass
    return None
