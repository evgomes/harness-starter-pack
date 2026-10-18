#!/usr/bin/env bash
# Verificação somente leitura de prontidão do Graphify para hooks de início de sessão do Claude Code e Cursor.
# Requer Bash, Git e (para verificar a atualidade do índice) Python 3. Não instala nem altera nada.
set -u

harness="${1:-}"
if [[ "$harness" != "claude" && "$harness" != "cursor" ]]; then
  printf '%s\n' 'Uso: graphify-session-start.sh claude|cursor' >&2
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
    emit_context 'Verificação de prontidão do Graphify ignorada: Git não está disponível. Instale o Git e use a skill graphify-setup para verificar este projeto.'
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
command -v graphify >/dev/null 2>&1 || issues+=("o CLI graphify não está no PATH")
[[ -f "$repo_root/.graphifyignore" ]] || issues+=("o .graphifyignore da raiz não existe")
[[ -n "$refresh_script" ]] || issues+=("a skill de navegação Graphify e o script de atualização não estão na pasta de skills do projeto")
if ! git -C "$repo_root" check-ignore -q -- graphify-out/graph.json; then
  issues+=("o .gitignore da raiz não ignora graphify-out/")
fi

if (( ${#issues[@]} > 0 )); then
  joined="$(IFS='; '; printf '%s' "${issues[*]}")"
  emit_context "A configuração do Graphify está incompleta: ${joined}. Use a skill graphify-setup para revisar e corrigir. Este hook não alterou nada."
  exit 0
fi

if ! command -v python3 >/dev/null 2>&1; then
  emit_context 'O Graphify está configurado, mas Python 3 não está disponível para verificar a atualidade do índice. Instale Python 3 ou execute o script de atualização do PowerShell; depois, use a skill graphify antes de consultar o grafo.'
  exit 0
fi

if bash "$refresh_script" --check-only >/dev/null 2>&1; then
  exit 0
fi
emit_context 'O Graphify está configurado, mas o índice não existe ou está desatualizado. Atualize-o com a skill graphify antes de consultar o grafo.'
exit 0
