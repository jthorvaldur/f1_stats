"""Fetch prediction market odds from Polymarket's Gamma API."""
import json
import httpx

GAMMA_API = "https://gamma-api.polymarket.com"


def fetch_polymarket_event(slug: str) -> dict | None:
    try:
        r = httpx.get(f"{GAMMA_API}/events?slug={slug}", timeout=15)
        r.raise_for_status()
        events = r.json()
        if not events:
            return None
        return events[0] if isinstance(events, list) else events
    except Exception:
        return None


def _parse_json_field(val):
    if isinstance(val, str):
        return json.loads(val)
    return val


def get_race_odds(race_date: str) -> list[dict]:
    slug = f"f1-canadian-grand-prix-winner-{race_date}"
    event = fetch_polymarket_event(slug)
    if not event:
        return []

    odds = []
    for market in event.get("markets", []):
        question = market.get("question", "")
        outcomes = _parse_json_field(market.get("outcomes", []))
        prices = _parse_json_field(market.get("outcomePrices", []))
        if len(outcomes) >= 2 and len(prices) >= 2:
            yes_price = float(prices[0])
            driver = question.replace("Will ", "").replace(" win the 2026 Canadian Grand Prix?", "").replace(" win?", "").strip()
            if yes_price > 0.001:
                odds.append({
                    "driver": driver,
                    "market_prob": round(yes_price, 4),
                    "market_id": market.get("id"),
                })
    return sorted(odds, key=lambda x: x["market_prob"], reverse=True)


def get_championship_odds() -> list[dict]:
    event = fetch_polymarket_event("2026-f1-drivers-champion")
    if not event:
        return []

    odds = []
    for market in event.get("markets", []):
        outcomes = _parse_json_field(market.get("outcomes", []))
        prices = _parse_json_field(market.get("outcomePrices", []))
        if len(outcomes) >= 2 and len(prices) >= 2:
            question = market.get("question", "")
            driver = question.replace("Will ", "").replace(" be the 2026 F1 Drivers' Champion?", "").strip()
            yes_price = float(prices[0])
            if yes_price > 0.001:
                odds.append({
                    "driver": driver,
                    "market_prob": round(yes_price, 4),
                    "volume": market.get("volume", 0),
                })
    return sorted(odds, key=lambda x: x["market_prob"], reverse=True)


def compute_edge(model_prob: float, market_prob: float) -> dict:
    if market_prob <= 0 or model_prob <= 0:
        return {"edge": 0, "ev": 0, "kelly": 0, "signal": "neutral"}

    implied_odds = 1 / market_prob
    ev = model_prob * (implied_odds - 1) - (1 - model_prob)
    edge = model_prob - market_prob
    kelly = (model_prob * (implied_odds - 1) - (1 - model_prob)) / (implied_odds - 1) if implied_odds > 1 else 0
    kelly = max(0, kelly)

    if edge > 0.05:
        signal = "strong_buy"
    elif edge > 0.02:
        signal = "buy"
    elif edge < -0.05:
        signal = "strong_sell"
    elif edge < -0.02:
        signal = "sell"
    else:
        signal = "neutral"

    return {
        "edge": round(edge, 4),
        "ev": round(ev, 4),
        "kelly": round(kelly, 4),
        "implied_odds": round(implied_odds, 2),
        "signal": signal,
    }
