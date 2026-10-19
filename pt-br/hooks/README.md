# Orientações para hooks e verificações

Hooks são integrações de ciclo de vida específicas do harness. Mantenha esta orientação neutra quanto a ferramentas e confira a documentação oficial atual antes de configurar o projeto.

## Conjunto inicial

O pacote inclui uma verificação opcional de Graphify no início da sessão. Instale o script e exemplo correspondente somente se o projeto usar Graphify. O hook verifica CLI, configuração, skill de navegação e índice; se algo exigir atenção, acrescenta instrução curta ao contexto. Não instala software, altera arquivos, acessa rede nem reconstrói índice.

| Verificação | Uso sugerido | Motivo |
|---|---|---|
| Prontidão Graphify | Hook opcional de sessão para Claude Code/Cursor | Verificação rápida que encaminha para configuração do Graphify |
| Formatação/lint | Comandos e CI; opcionalmente após edição | Ferramentas e auto-fix dependem do projeto |
| Testes | Workflow/CI; opcionalmente teste focado pós-edição | Suíte completa pode ser lenta |
| Dependências/licenças | Skill revisão de dependências e CI agendada | Requer fonte de avisos e responsável |
| Segurança/acessibilidade | Skills e scanners CI explícitos | Requer contexto e às vezes evidência humana |
| Revisão shift-left | Skill/comando explícito | Custo variável; executar no ponto acordado |

Não instale exemplos indiscriminadamente. Escolha hooks adequados, documente como desativar e mantenha trabalho lento/modelado fora de eventos por edição.

## Hook de início Graphify

Scripts equivalentes para PowerShell e Bash:

- scripts/graphify-session-start.ps1 usa PowerShell 7 (pwsh) e Git em Windows/macOS/Linux.
- scripts/graphify-session-start.sh usa Bash/Git no macOS/Linux e Python 3 para conferir índice.

Ambos emitem formato esperado pelo harness. Claude Code: escolha exemplo PowerShell/Bash em adapters/ e mescle em .claude/settings.json. Cursor: escolha exemplo e mescle em .cursor/hooks.json.

O hook Bash chama refresh-graph.sh, que delega checagens/rebuild à biblioteca padrão Python 3. A instalação é opt-in e pode adicionar contexto de sessão. Hooks são somente leitura; use configuração do Graphify para configurar/reparar. Índice obsoleto é informado, não reconstruído automaticamente, pois o rebuild pode demorar e substituir graphify-out/.

Copie script para .agents/hooks/ e mescle o exemplo com configuração existente. Copie a skill Graphify completa com scripts de atualização para pasta de skills suportada. Hooks Claude Code podem ser versionados; hooks Cursor rodam em workspaces confiáveis, portanto revise o comando.

Codex/OpenCode não estão conectados a este script por padrão. Use skill e workflow compartilhados até haver mecanismo apropriado e mantido.

## O que pertence a um hook

- Verificações locais rápidas, determinísticas, com entradas e saídas claras.
- Timeout curto e mensagem acionável.
- Opt-in explícito quando houver demora, rede ou alteração de arquivos.

## O que deve ficar em skill ou CI

- Revisão de código por modelo: skill revisão antecipada de código, modelo forte e evidências auditáveis; nunca após toda edição.
- Workflows OWASP/WCAG precisam contexto e às vezes evidência manual.
- Auditoria de dependências/licenças precisa dados externos e recorrência; use CI/agendamento e responsáveis.

## Integração segura

Não instale/atualize ferramentas, auto-corrija código, faça push, publique dados ou acesse rede implicitamente. Não envie código/dados pessoais a serviços externos. Evite verificações pesadas em toda chamada. Hooks reportam; não substituem revisão, CI, threat modeling, pentest ou avaliação de acessibilidade. Documente evento, comando, runtime, timeout, efeito da falha e bypass.

Use skill autoria de hooks e docs/templates/contrato-de-hook.md. O contrato é checklist, não esquema compartilhado: eventos, payloads, permissões, confiança, timeout e saída variam. Consulte documentação oficial, registre versão/data e valide sucesso, achado, ferramenta ausente, timeout e erro. Mescle configuração.

Escolha mecanismo proporcional: skill para tarefa contextual, hook para checagem determinística rápida e CI/agendamento para barreira autoritativa/recorrente. Consulte acordo de qualidade/segurança.

## Referências

- [Hooks Claude Code](https://code.claude.com/docs/en/hooks)
- [Hooks Cursor](https://cursor.com/docs/hooks)
- [Personalização Cursor](https://cursor.com/docs/customize-cursor)

Integrações Codex/OpenCode evoluem; consulte catálogo/documentação oficial atual.
