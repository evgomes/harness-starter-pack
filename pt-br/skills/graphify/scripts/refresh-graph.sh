#!/usr/bin/env bash
# POSIX-shell entry point for the cross-platform Python Graphify refresh implementation.
# Usage: bash ./refresh-graph.sh [--check-only] [--force]
set -u

script_dir="$(CDPATH= cd -- "$(dirname "$0")" && pwd)"
if ! command -v python3 >/dev/null 2>&1; then
  printf '%s\n' 'Python 3 is required to run the Graphify refresh script on macOS/Linux.' >&2
  exit 1
fi
exec python3 "$script_dir/refresh-graph.py" "$@"
