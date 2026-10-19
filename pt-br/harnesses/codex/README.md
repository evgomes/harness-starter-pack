# Adaptador Codex

O Codex reconhece arquivos AGENTS.md do repositório como instruções do projeto. Use as [instruções compartilhadas](../../AGENTS.md) como fonte de verdade e mantenha AGENTS.md raiz do projeto conciso, com links para seus acordos. O Codex carrega skills reutilizáveis sob demanda; instale skills do projeto em .agents/skills/<nome-da-skill>/ e preserve referências/scripts relativos.

## Configuração

1. Copie/adapte pt-br/AGENTS.md para a raiz do repositório de destino.
2. Copie os cinco acordos para docs/acordos/. Preencha arquitetura, dependências, convenções e qualidade/segurança com fatos verificados; mantenha workflow como padrão reutilizável e adapte-o somente para processo específico documentado. Marque seções inaplicáveis com motivo, em vez de omitir arquivos.
3. Copie cada diretório de skill escolhido para .agents/skills/.
4. Se instruções forem separadas por diretório, adicione AGENTS.md com escopo somente onde regras locais diferirem materialmente.

Referência oficial: [guia de workflow Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex).
