#!/usr/bin/env python3
import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEED_GROUPS = ROOT / "references" / "worldcup-2026-groups.json"


def main():
    parser = argparse.ArgumentParser(description="Create World Cup prediction data scaffolding.")
    parser.add_argument("--out", required=True, help="Output data directory")
    args = parser.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SEED_GROUPS, out / "groups.json")

    source_log = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sources": [
            {
                "name": "bootstrap groups",
                "url": str(SEED_GROUPS),
                "status": "seed",
                "note": "Replace with official live data before final predictions."
            },
            {
                "name": "FIFA standings",
                "url": "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/standings",
                "status": "refresh-required"
            },
            {
                "name": "Polymarket search",
                "url": "https://polymarket.com/search?query=World%20Cup",
                "status": "refresh-required"
            }
        ]
    }
    (out / "source-log.json").write_text(json.dumps(source_log, indent=2), encoding="utf-8")
    (out / "predictions.json").write_text(json.dumps({"matches": [], "outrights": [], "updated_at": source_log["generated_at"]}, indent=2), encoding="utf-8")
    locked_results = out / "locked-results.json"
    if not locked_results.exists():
        locked_results.write_text(json.dumps({"updated_at": source_log["generated_at"], "results": []}, indent=2), encoding="utf-8")
    print(f"Created prediction data scaffold in {out}")


if __name__ == "__main__":
    main()
