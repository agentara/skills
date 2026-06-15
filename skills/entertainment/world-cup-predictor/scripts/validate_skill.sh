#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV="$ROOT/.venv"
VALIDATOR="/Users/taohe/.codex/skills/.system/skill-creator/scripts/quick_validate.py"

if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV"
fi

"$VENV/bin/python" -m pip install --quiet --upgrade pip PyYAML
"$VENV/bin/python" "$VALIDATOR" "$ROOT"
