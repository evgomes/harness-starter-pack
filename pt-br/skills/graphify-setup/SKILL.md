---
name: graphify-setup
description: Instale o CLI Graphify na máquina da pessoa desenvolvedora e configure o grafo local de código no repositório: ignorações, skill de navegação, registro de dependência, primeiro índice e prova com consulta. Use quando não houver grafo ou o comando estiver ausente/desatualizado.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Configuração do Graphify

A skill graphify navega pelo grafo; esta skill instala o CLI na máquina e configura o projeto. A instalação deve terminar com CLI no PATH, versão documentada, arquivos de exclusão coerentes, skills instaladas e uma consulta real comprovada.

## 1. Instale o CLI na máquina

Leia docs/agreements/dependencies.md, .gitignore, .graphifyignore, scripts de atualização existentes e pastas de skills dos harnesses. Se a configuração completa já existe, verifique command/version, PATH e evidências antes de reinstalar.

**Instale efetivamente** o pacote na ferramenta isolada da máquina do desenvolvedor; não pare em sugerir um comando:

`bash
uv tool install graphifyy
`

Se uv não estiver disponível, use pipx:

`bash
pipx install graphifyy
`

O pacote chama-se graphifyy (dois y); o comando é graphify. Prefira uv tool; use pipx como alternativa. Não instale via pip no ambiente virtual do projeto nem inclua em dependências da aplicação. É ferramenta de desenvolvimento instalada na máquina.

Se o comando não for encontrado, execute uv tool update-shell ou pipx ensurepath e abra um shell novo. Confirme com graphify --version; registre a versão instalada. Não invente uma versão.

## 2. Registre a ferramenta

Em docs/agreements/dependencies.md, na tabela de ferramentas, registre Graphify (graphifyy), versão real, finalidade e origem. Se a equipe fixar versão, documente o comando uv tool install graphifyy==<versão>.

## 3. Ignore saída e decida o que não indexar

1. .gitignore deve conter graphify-out/. Se git ls-files graphify-out listar arquivos, o grafo foi versionado: remova o tracking com git rm -r --cached graphify-out em commit próprio e informe que blobs antigos continuam no histórico.
2. Crie .graphifyignore na raiz com exclusões equivalentes ao script. Comece por:

`gitignore
graphify-out/
.claude/
.agents/
.codex/
.cursor/
.opencode/
.git/
**/node_modules/
**/dist/
**/build/
**/bin/
**/obj/
`

3. Adicione ruído da stack a todas as listas de exclusão no mesmo trabalho: .graphifyignore, $excludedFolders/$excludedFileSuffixes em refresh-graph.ps1 e EXCLUDED_FOLDERS/EXCLUDED_FILE_SUFFIXES em refresh-graph.py. Considere clientes gerados, código vendorizado, snapshots de migração, bundles minificados e fixtures grandes. Uma diferença entre listas pode fazer a verificação de atualidade reportar “stale” indefinidamente.

Graphify também respeita .gitignore; não é necessário repetir o que já está ignorado, exceto pastas de agentes normalmente versionadas que não devem ser indexadas.

## 4. Instale a skill de navegação nos harnesses escolhidos

Copie diretórios completos graphify e graphify-setup, incluindo scripts de atualização, para os locais suportados:

| Agente | Pastas |
|---|---|
| Claude Code | .claude/skills/graphify/ e .claude/skills/graphify-setup/ |
| Codex, Cursor e OpenCode | .agents/skills/graphify/ e .agents/skills/graphify-setup/ |

Preserve estrutura e arquivos existentes; faça commit das skills para que a equipe receba o mesmo processo. Se um harness só descobrir skills em sua própria pasta, copie as mesmas fontes sem criar cópias divergentes.

Garanta que instruções do agente mencionem o grafo. O starter pack já faz isso em AGENTS.md. Em outro repositório, acrescente a instrução para atualizar o grafo antes da primeira consulta e após mudanças no código.

## 5. Crie índice e prove uma consulta

Use o script de atualização do harness escolhido:

`powershell
pwsh ./.agents/skills/graphify/scripts/refresh-graph.ps1
pwsh ./.agents/skills/graphify/scripts/refresh-graph.ps1 -CheckOnly
`

`bash
bash ./.agents/skills/graphify/scripts/refresh-graph.sh
bash ./.agents/skills/graphify/scripts/refresh-graph.sh --check-only
`

No Bash/Python, mantenha Python 3.9+ disponível. O modo check-only deve indicar índice atualizado e terminar com código 0. Faça uma pergunta real:

`bash
graphify god-nodes --top 5
graphify explain "<símbolo conhecido>"
`

Confira se os hubs fazem sentido e se explain aponta ao arquivo e linha corretos. Registre versão, quantidade de arquivos indexados, hubs principais e resultado da prova. Se a contagem estiver muito distante das fontes esperadas, corrija exclusões.

## Atualização e remoção

Atualize com uv tool upgrade graphifyy ou pipx upgrade graphifyy, reconstrua com -Force/--force e repita a prova. Atualize a versão no acordo na mesma mudança. Se uma versão quebrar o script, documente erro e fixe a versão anterior até corrigir.

Para remover, exclua skills dos harnesses, graphify-out/, .graphifyignore, linha correspondente no .gitignore, registro em dependencies.md e regras em AGENTS.md/CLAUDE.md/workflow; faça isso em um commit. Remova da máquina com uv tool uninstall graphifyy se nenhuma outra ferramenta depender dele.

## Diagnóstico

| Sintoma | Causa provável e correção |
|---|---|
| check-only informa stale logo após rebuild | Alinhe .graphifyignore e exclusões dos scripts. |
| Grafo contém nós Markdown | Não use graphify update; reconstrua pelo script, que limpa a saída e usa code-only. |
| Script recusa grafo não ignorado/versionado | Conclua a etapa 3. |
| graphify não é encontrado | CLI não está no PATH do shell; atualize PATH e abra shell novo. |
| python3 ausente em macOS/Linux | Instale Python 3.9+ ou use PowerShell se disponível. |
| Extração falha em um arquivo | Caso de parser; exclua nos dois conjuntos de regras e registre/report o caso. |
| Rebuild demora minutos | Exclua artefatos de build, código vendorizado ou arquivos grandes. |