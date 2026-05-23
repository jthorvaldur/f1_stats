#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

uv sync
uv run f1stats generate "$@"

echo ""
echo "Pages regenerated in docs/"
ls -la docs/*.html
