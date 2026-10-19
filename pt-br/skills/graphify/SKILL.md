---
name: graphify
description: Navegação por código priorizando o grafo AST local do Graphify. Use para fluxos desconhecidos, arquitetura, chamadores, dependências, impacto de símbolos e conexões; não use como única evidência nem para editar arquivo já conhecido.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Navegação de código com Graphify

O grafo AST local ajuda a localizar código com consultas delimitadas em vez de leitura ampla. É um mapa, não uma fonte definitiva: pode não representar dispatch dinâmico, injeção de dependência, reflexão, código gerado, registros por string e construções não suportadas pelo parser.

Os dados permanecem na máquina. Não exige API ou extração remota. O projeto pode usar o hook opcional de início de sessão, somente leitura, do starter pack para conferir configuração e atualização do índice. Não habilite integrações próprias do Graphify nem execute graphify update: o caminho incremental é instável em Windows e pode contaminar o manifesto code-only com nós Markdown. Os scripts fazem rebuild limpo.

## Requisitos

- CLI Graphify no PATH. Instale pela skill configuração do Graphify e registre a versão em docs/acordos/dependencias.md.
- Runtime de atualização: PowerShell 7+ (pwsh) para refresh-graph.ps1; ou Python 3.9+ e Bash para refresh-graph.sh/refresh-graph.py. Bash é indicado para macOS/Linux; PowerShell funciona nos três sistemas.
- graphify-out/ no .gitignore e .graphifyignore alinhado às exclusões do script.

Se CLI, configuração ou script estiver ausente, pare e siga configuração do Graphify. Não instale ferramentas nem reescreva ignore files por esta skill.

## Mantenha o índice atualizado

Antes da primeira consulta da tarefa, use o script instalado no harness pertinente:

`powershell
pwsh ./.agents/skills/graphify/scripts/refresh-graph.ps1
`

`bash
bash ./.agents/skills/graphify/scripts/refresh-graph.sh
`

Use o caminho instalado para o harness. O script compara hashes das fontes suportadas com o manifesto, ignora trabalho se não houver mudança e reconstrói quando arquivos são adicionados, removidos, renomeados ou editados. Execute novamente após mudanças de código e antes de concluir. Alterações só de documentação não exigem rebuild.

- PowerShell -CheckOnly ou Bash/Python --check-only verifica atualização sem alterar; retorna 2 se obsoleto.
- -Force ou --force reconstrói sempre; use para reparo/benchmark, não no fluxo normal.
- O script recusa execução se graphify-out/ estiver versionado ou não estiver ignorado.

## Disciplina de consulta

Comece pela operação mais barata capaz de responder:

| Pergunta | Comando |
|---|---|
| Conceito/fluxo desconhecido | graphify query "<pergunta>" --budget 800 |
| Símbolo conhecido e seus contatos | graphify explain "<símbolo>" |
| Caminho entre dois elementos | graphify path "<origem>" "<destino>" |
| Impacto de mudar símbolo | graphify affected "<símbolo>" --depth 2 |
| Por onde começar no repositório | graphify god-nodes --top 10 |

Aumente o orçamento somente quando o resultado delimitado for pertinente, mas incompleto; normalmente fique até 1.500 tokens. O build code-only não gera GRAPH_REPORT.md; para arquitetura ampla, comece por god-nodes e query em vez de despejar graph.json.

Nomes de símbolos são correspondidos de modo flexível. Se surgir “No unique node match”, o nome é ambíguo ou ausente; faça query e reutilize o rótulo exato. affected inicia a análise, não a conclui: segue chamadas/imports/herança e pode não achar DI, reflexão, eventos ou registros por string. Combine com git grep delimitado antes de declarar a mudança segura.

Use o resultado para escolher alguns caminhos e leia as linhas no código antes de editar ou afirmar algo. Trate arestas EXTRACTED como evidência do parser; INFERRED/AMBIGUOUS são hipóteses.

## Quando usar outra ferramenta

Graphify responde onde algo está e o que se conecta; não encontra todas as ocorrências exatas de uma string. Use git grep delimitado para busca exaustiva, construções não suportadas ou quando consultas não ajudarem após tentar identificadores do domínio. Explique por que o grafo foi insuficiente.
