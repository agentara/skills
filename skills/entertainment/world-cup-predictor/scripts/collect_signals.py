#!/usr/bin/env python3
import argparse
import json
import os
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GROUPS = ROOT / "references" / "worldcup-2026-groups.json"

HOST_CITIES = [
    "Atlanta", "Boston", "Dallas", "Guadalajara", "Houston", "Kansas City",
    "Los Angeles", "Mexico City", "Miami", "Monterrey", "New York", "Philadelphia",
    "San Francisco", "Seattle", "Toronto", "Vancouver"
]


def fetch_json(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": "WorldCupPredictor/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8", "ignore"))


def fetch_text(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": "WorldCupPredictor/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", "ignore")


def google_news(query, limit=8):
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode({
        "q": query,
        "hl": "en-US",
        "gl": "US",
        "ceid": "US:en"
    })
    try:
        root = ET.fromstring(fetch_text(url))
        items = []
        for item in root.findall(".//item")[:limit]:
            items.append({
                "title": item.findtext("title", default=""),
                "url": item.findtext("link", default=""),
                "published": item.findtext("pubDate", default=""),
                "query": query
            })
        return items
    except Exception as exc:
        return [{"title": f"news fetch failed: {type(exc).__name__}", "url": url, "published": "", "query": query}]


def polymarket_markets(query, limit=8):
    url = "https://gamma-api.polymarket.com/markets?" + urllib.parse.urlencode({
        "search": query,
        "limit": limit
    })
    try:
        data = fetch_json(url)
        rows = []
        for market in data[:limit]:
            title = market.get("question") or market.get("title") or ""
            if "world cup" not in title.lower() and "fifa" not in title.lower():
                continue
            rows.append({
                "title": title,
                "url": f"https://polymarket.com/event/{market.get('slug', '')}",
                "liquidity": market.get("liquidity"),
                "volume": market.get("volume"),
                "outcomes": market.get("outcomes"),
                "prices": market.get("outcomePrices")
            })
        return rows or polymarket_fallbacks(url, "empty API response")
    except Exception as exc:
        return polymarket_fallbacks(url, f"fetch failed: {type(exc).__name__}")


def polymarket_fallbacks(api_url, reason):
    return [
        {
            "status": "fallback-required",
            "title": "Polymarket API unavailable for World Cup query",
            "url": api_url,
            "note": reason
        },
        {
            "status": "fallback-required",
            "title": "Manual check: World Cup winner market",
            "url": "https://polymarket.com/event/world-cup-winner",
            "note": "Open this page and capture title, timestamp, liquidity/volume, prices, and normalized probabilities."
        },
        {
            "status": "fallback-required",
            "title": "Manual check: World Cup team advancement markets",
            "url": "https://polymarket.com/search?query=World%20Cup%20advance",
            "note": "Use only liquid markets; mark low-liquidity or zero-volume props as stale."
        },
        {
            "status": "fallback-required",
            "title": "Manual check: World Cup match moneylines",
            "url": "https://polymarket.com/search?query=World%20Cup%20moneyline",
            "note": "For match odds, compare against bookmaker snapshots before adjusting probabilities."
        }
    ]


def weather_signals(limit=8):
    rows = []
    for city in HOST_CITIES[:limit]:
        try:
            geo_url = "https://geocoding-api.open-meteo.com/v1/search?" + urllib.parse.urlencode({
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json"
            })
            geo = fetch_json(geo_url)
            result = (geo.get("results") or [None])[0]
            if not result:
                continue
            forecast_url = "https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode({
                "latitude": result["latitude"],
                "longitude": result["longitude"],
                "daily": "temperature_2m_max,precipitation_probability_max",
                "forecast_days": 7,
                "timezone": "auto"
            })
            forecast = fetch_json(forecast_url)
            daily = forecast.get("daily", {})
            rows.append({
                "city": city,
                "country": result.get("country"),
                "timezone": result.get("timezone"),
                "max_temp_c_next_7d": max(daily.get("temperature_2m_max", []) or [None]),
                "max_precip_probability_next_7d": max(daily.get("precipitation_probability_max", []) or [None]),
                "source": forecast_url
            })
        except Exception as exc:
            rows.append({"city": city, "error": type(exc).__name__})
    return rows


def odds_signals():
    api_key = os.environ.get("ODDS_API_KEY")
    if not api_key:
        return [{"status": "missing ODDS_API_KEY", "note": "Bookmaker odds not fetched."}]
    url = "https://api.the-odds-api.com/v4/sports/soccer_fifa_world_cup/odds?" + urllib.parse.urlencode({
        "apiKey": api_key,
        "regions": "us,uk,eu",
        "markets": "h2h",
        "oddsFormat": "decimal"
    })
    try:
        return fetch_json(url)
    except Exception as exc:
        return [{"status": f"odds fetch failed: {type(exc).__name__}", "url": url.replace(api_key, "REDACTED")}]


def locked_results(path):
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data.get("results", data if isinstance(data, list) else [])
    except Exception:
        return []


def main():
    parser = argparse.ArgumentParser(description="Collect World Cup news, market, weather, and odds signals.")
    parser.add_argument("--out", default=str(ROOT / "assets" / "dashboard" / "data" / "signals.json"))
    parser.add_argument("--news-limit", type=int, default=8)
    args = parser.parse_args()

    groups = json.loads(GROUPS.read_text(encoding="utf-8"))["groups"]
    teams = [team for group in groups for team in group["teams"]]
    news_queries = [
        "2026 FIFA World Cup injuries suspensions lineups",
        "2026 FIFA World Cup odds favorites Polymarket",
        "2026 FIFA World Cup weather heat humidity venues",
        "2026 FIFA World Cup tactical preview teams"
    ]
    signals = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "teams": teams,
        "locked_results": locked_results(ROOT / "assets" / "dashboard" / "data" / "locked-results.json"),
        "news": [item for query in news_queries for item in google_news(query, args.news_limit // 2)],
        "polymarket": polymarket_markets("2026 FIFA World Cup winner odds"),
        "weather": weather_signals(),
        "odds": odds_signals()
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(signals, indent=2), encoding="utf-8")
    print(f"Wrote signals to {out}")


if __name__ == "__main__":
    main()
