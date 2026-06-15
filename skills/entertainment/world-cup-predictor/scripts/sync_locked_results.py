#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "assets" / "dashboard" / "data" / "locked-results.json"


def parse_result(raw):
    parts = raw.split("|")
    if len(parts) < 8:
        raise ValueError("--add format: match_id|round|group|home|away|home_score|away_score|source")
    match_id, round_name, group, home, away, home_score, away_score, source = parts[:8]
    return {
        "match_id": match_id,
        "round": round_name,
        "group": group or None,
        "teams": [home, away],
        "final_score": {"home": int(home_score), "away": int(away_score)},
        "status": "finished",
        "source": source,
        "locked_at": datetime.now(timezone.utc).isoformat()
    }


def key_for(result):
    if result.get("match_id"):
        return f"id:{result['match_id']}"
    teams = result.get("teams", [])
    return "teams:" + "|".join(sorted(teams))


def main():
    parser = argparse.ArgumentParser(description="Maintain finished World Cup match results for settled dashboard rows.")
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    parser.add_argument("--from-json", help="JSON file containing an array of finished match results")
    parser.add_argument("--add", action="append", default=[], help="Add one result: match_id|round|group|home|away|home_score|away_score|source")
    args = parser.parse_args()

    out = Path(args.out)
    existing = []
    if out.exists():
        data = json.loads(out.read_text(encoding="utf-8"))
        existing = data.get("results", data if isinstance(data, list) else [])

    incoming = []
    if args.from_json:
        data = json.loads(Path(args.from_json).read_text(encoding="utf-8"))
        incoming.extend(data.get("results", data if isinstance(data, list) else []))
    incoming.extend(parse_result(item) for item in args.add)

    merged = {key_for(item): item for item in existing}
    for item in incoming:
        item.setdefault("status", "finished")
        item.setdefault("locked_at", datetime.now(timezone.utc).isoformat())
        merged[key_for(item)] = item

    payload = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "results": sorted(merged.values(), key=lambda item: item.get("match_id", ""))
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {len(payload['results'])} locked results to {out}")


if __name__ == "__main__":
    main()
