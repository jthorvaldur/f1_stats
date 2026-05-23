TEAM_COLORS = {
    "mercedes": {"hex": "#00d2be", "css": "team-mercedes"},
    "ferrari": {"hex": "#dc143c", "css": "team-ferrari"},
    "mclaren": {"hex": "#ff8700", "css": "team-mclaren"},
    "red_bull": {"hex": "#3671C6", "css": "team-redbull"},
    "alpine": {"hex": "#0090ff", "css": "team-alpine"},
    "haas": {"hex": "#b6babd", "css": "team-haas"},
    "rb": {"hex": "#6692ff", "css": "team-rb"},
    "williams": {"hex": "#64c4ff", "css": "team-williams"},
    "sauber": {"hex": "#00e701", "css": "team-audi"},
    "audi": {"hex": "#00e701", "css": "team-audi"},
    "kick_sauber": {"hex": "#00e701", "css": "team-audi"},
    "cadillac": {"hex": "#c0c0c0", "css": "team-cadillac"},
    "andretti": {"hex": "#c0c0c0", "css": "team-cadillac"},
    "aston_martin": {"hex": "#006f62", "css": "team-aston"},
    "alphatauri": {"hex": "#6692ff", "css": "team-rb"},
    "racing_bulls": {"hex": "#6692ff", "css": "team-rb"},
}

TEAM_DISPLAY_NAMES = {
    "mercedes": "Mercedes",
    "ferrari": "Ferrari",
    "mclaren": "McLaren",
    "red_bull": "Red Bull",
    "alpine": "Alpine",
    "haas": "Haas",
    "rb": "RB",
    "williams": "Williams",
    "sauber": "Audi",
    "audi": "Audi",
    "kick_sauber": "Audi",
    "cadillac": "Cadillac",
    "andretti": "Cadillac",
    "aston_martin": "Aston Martin",
    "alphatauri": "RB",
    "racing_bulls": "RB",
}

DRIVER_WEIGHTS = {
    "albon": {"weight": 74, "height": 186},
    "alonso": {"weight": 68, "height": 171},
    "antonelli": {"weight": 70, "height": 172},
    "bearman": {"weight": 68, "height": 184},
    "bortoleto": {"weight": 71, "height": 184},
    "bottas": {"weight": 69, "height": 173},
    "colapinto": {"weight": 71, "height": 175},
    "gasly": {"weight": 70, "height": 177},
    "hadjar": {"weight": 65, "height": 167},
    "hamilton": {"weight": 73, "height": 174},
    "hulkenberg": {"weight": 78, "height": 184},
    "lawson": {"weight": 72, "height": 174},
    "leclerc": {"weight": 69, "height": 180},
    "arvid_lindblad": {"weight": 68, "height": 174},
    "norris": {"weight": 68, "height": 170},
    "ocon": {"weight": 73, "height": 186},
    "piastri": {"weight": 68, "height": 178},
    "perez": {"weight": 63, "height": 173},
    "russell": {"weight": 70, "height": 185},
    "sainz": {"weight": 66, "height": 178},
    "stroll": {"weight": 70, "height": 182},
    "max_verstappen": {"weight": 72, "height": 181},
}

CAR_WEIGHTS = {
    "ferrari": {"weight": 770, "over": 2},
    "mclaren": {"weight": 771, "over": 3},
    "mercedes": {"weight": 772, "over": 4},
    "alpine": {"weight": 773, "over": 5},
    "haas": {"weight": 773, "over": 5},
    "cadillac": {"weight": 774, "over": 6},
    "rb": {"weight": 775, "over": 7},
    "audi": {"weight": 776, "over": 8},
    "sauber": {"weight": 776, "over": 8},
    "red_bull": {"weight": 778, "over": 10},
    "aston_martin": {"weight": 778, "over": 10},
    "williams": {"weight": 796, "over": 28},
}

DEBUT_YEARS = {
    "max_verstappen": 2015,
    "stroll": 2017,
    "arvid_lindblad": 2026,
    "antonelli": 2025,
    "norris": 2019,
    "alonso": 2001,
    "bearman": 2024,
    "leclerc": 2018,
    "ocon": 2016,
    "sainz": 2015,
    "hadjar": 2025,
    "bortoleto": 2025,
    "russell": 2019,
    "piastri": 2023,
    "perez": 2011,
    "gasly": 2017,
    "colapinto": 2024,
    "lawson": 2023,
    "hamilton": 2007,
    "hulkenberg": 2010,
    "albon": 2019,
    "bottas": 2013,
}

MIN_CAR_WEIGHT = 768
MIN_DRIVER_WEIGHT = 80


def get_team_color(team_id: str) -> dict:
    team_id = team_id.lower().replace(" ", "_").replace("-", "_")
    return TEAM_COLORS.get(team_id, {"hex": "#8b949e", "css": "team-default"})


def get_team_display(team_id: str) -> str:
    team_id = team_id.lower().replace(" ", "_").replace("-", "_")
    return TEAM_DISPLAY_NAMES.get(team_id, team_id.replace("_", " ").title())
