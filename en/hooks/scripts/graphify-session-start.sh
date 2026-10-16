#!/usr/bin/env bash
# Read-only Graphify readiness check for Claude Code and Cursor session-start hooks.
# Requires Bash, Git, and (for index freshness) Python 3. Does not install or modify anything.
set -u

harness="${1:-}"
if [[ "$harness" != "claude" && "$harness" != "cursor" ]]; then
  printf '%s\n' 'Usage: graphify-session-start.sh claude|cursor' >&2
  exit 2
fi

emit_context() {
  local message="$1"
  if [[ "$harness" == "claude" ]]; then
    printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}\n' "$message"
  else
    printf '{"additional_context":"%s"}\n' "$message"
  fi
}

if ! command -v git >/dev/null 2>&1; then
  if [[ -f .graphifyignore || -d graphify-out ]]; then
    emit_context 'Graphify readiness check skipped: Git is not available. Install Git, then use the graphify-setup skill to check this project.'
  fi
  exit 0
fi

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$repo_root" ]]; then
  exit 0
fi
repo_root="$(cd "$repo_root" && pwd -P)"

refresh_script=""
for candidate in \
  "$repo_root/.agents/skills/graphify/scripts/refresh-graph.sh" \
  "$repo_root/.claude/skills/graphify/scripts/refresh-graph.sh" \
  "$repo_root/.cursor/skills/graphify/scripts/refresh-graph.sh"; do
  if [[ -f "$candidate" ]]; then
    refresh_script="$candidate"
    break
  fi
done

graphify_declared=false
[[ -f "$repo_root/.graphifyignore" || -d "$repo_root/graphify-out" || -n "$refresh_script" ]] && graphify_declared=true
if [[ -f "$repo_root/docs/agreements/dependencies.md" ]] &&
  grep -Eiq 'Graphify|graphifyy' "$repo_root/docs/agreements/dependencies.md"; then
  graphify_declared=true
fi
[[ "$graphify_declared" == true ]] || exit 0

issues=()
command -v graphify >/dev/null 2>&1 || issues+=("the graphify CLI is not on PATH")
[[ -f "$repo_root/.graphifyignore" ]] || issues+=("the root .graphifyignore is missing")
[[ -n "$refresh_script" ]] || issues+=("the Graphify navigation skill and refresh script are missing from the project skill folder")
if ! git -C "$repo_root" check-ignore -q -- graphify-out/graph.json; then
  issues+=("the root .gitignore does not ignore graphify-out/")
fi

if (( ${#issues[@]} > 0 )); then
  joined="$(IFS='; '; printf '%s' "${issues[*]}")"
  emit_context "Graphify setup is incomplete: ${joined}. Use the graphify-setup skill to review and repair it. This hook did not change anything."
  exit 0
fi

if ! command -v python3 >/dev/null 2>&1; then
  emit_context 'Graphify is configured, but Python 3 is not available to check index freshness. Install Python 3 or run the PowerShell refresh script, then use the graphify skill before querying the graph.'
  exit 0
fi

if bash "$refresh_script" --check-only >/dev/null 2>&1; then
  exit 0
fi
emit_context 'Graphify is configured, but its index is missing or stale. Refresh it with the graphify skill before querying the graph.'
exit 0
