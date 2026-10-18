# Adaptadores de harness

pt-br/AGENTS.md e as skills compartilhadas são a fonte deste pacote. Estes documentos explicam descoberta de instruções e configuração de cada harness. Consulte a documentação oficial antes de habilitar recursos opcionais.

| Harness | Adaptador | Instruções principais | Skills |
|---|---|---|---|
| Codex | [README](codex/README.md) | AGENTS.md | .agents/skills/ |
| Claude Code | [CLAUDE.md](claude-code/CLAUDE.md) | CLAUDE.md e AGENTS.md conforme política local | .claude/skills/ |
| Cursor | [Regra](cursor/rules/harness-starter.mdc) | AGENTS.md ou .cursor/rules/*.mdc | .agents/skills/ ou .cursor/skills/ |
| OpenCode | [Configuração de exemplo](opencode/opencode.example.json) | AGENTS.md | .agents/skills/ |

## Documentação oficial

- [Guia de workflow Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex)
- Claude Code: [memória](https://code.claude.com/docs/en/memory), [skills](https://code.claude.com/docs/en/skills), [hooks](https://code.claude.com/docs/en/hooks)
- Cursor: [regras](https://cursor.com/docs/context/rules-for-ai) e [skills](https://cursor.com/docs/skills)
- OpenCode: [regras](https://docs.opencode.ai/docs/rules/) e [skills](https://docs.opencode.ai/docs/skills/)
- [Browser OpenAI](https://learn.chatgpt.com/docs/browser) (somente desktop, não CLI/IDE)
- [Claude Code Desktop](https://code.claude.com/docs/en/desktop)
- [Browser Cursor](https://cursor.com/docs/agent/tools/browser)
- [MCP OpenCode](https://opencode.ai/docs/mcp-servers/)
- [Chrome DevTools para agentes](https://developer.chrome.com/docs/devtools/agents/get-started)

Mantenha adaptadores concisos e não duplique orientação compartilhada. Para validação visual, veja o [guia de browser](../guides/browser-testing.md) e a skill [browser-visual-validation](../skills/browser-visual-validation/SKILL.md). Exemplos de hook Graphify para Claude Code/Cursor estão em [hooks](../hooks/README.md); não instalam CLI nem reconstroem índice. Novos hooks devem usar o [contrato](../docs/templates/hook-contract.md) e documentação oficial vigente.