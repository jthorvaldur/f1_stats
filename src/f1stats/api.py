import httpx
from datetime import date

BASE = "https://api.jolpi.ca/ergast/f1"


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

    return {
        "year": year,
        "current_round": current_round,
        "total_rounds": 24,
        "drivers": drivers,
        "constructors": constructors,
        "races": races,
        "driver_info": driver_info,
        "generated": date.today().isoformat(),
    }
