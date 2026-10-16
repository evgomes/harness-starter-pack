# Harness adapters

The repository-level `en/AGENTS.md` and shared skills are canonical. These files explain each harness's instruction discovery and provide a thin adapter or setup note. Review the official docs before using optional integration features because paths and lifecycle behavior can change.

| Harness | Adapter | Primary project instructions | Shared skills |
|---|---|---|---|
| Codex | [README](codex/README.md) | `AGENTS.md` | `.agents/skills/` |
| Claude Code | [CLAUDE.md](claude-code/CLAUDE.md) | `CLAUDE.md` plus `AGENTS.md` per project policy | `.claude/skills/` |
| Cursor | [Rule](cursor/rules/harness-starter.mdc) | `AGENTS.md` or scoped `.cursor/rules/*.mdc` | `.agents/skills/` or `.cursor/skills/` |
| OpenCode | [Example config](opencode/opencode.example.json) | `AGENTS.md` | `.agents/skills/` |

## Official documentation

- [Codex workflow guide](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex)
- [Claude Code memory](https://code.claude.com/docs/en/memory), [skills](https://code.claude.com/docs/en/skills), and [hooks](https://code.claude.com/docs/en/hooks)
- [Cursor rules](https://cursor.com/docs/context/rules-for-ai) and [skills](https://cursor.com/docs/skills)
- [OpenCode rules](https://docs.opencode.ai/docs/rules/) and [skills](https://docs.opencode.ai/docs/skills/)
- [OpenAI Browser guide](https://learn.chatgpt.com/docs/browser) (desktop app surface only; not Codex CLI/IDE)
- [Claude Code Desktop](https://code.claude.com/docs/en/desktop)
- [Cursor Browser](https://cursor.com/docs/agent/tools/browser)
- [OpenCode MCP servers](https://opencode.ai/docs/mcp-servers/)
- [Chrome DevTools for agents](https://developer.chrome.com/docs/devtools/agents/get-started) for an optional Chrome-specific MCP integration

Keep harness adapters concise. Do not copy the entire shared guidance into every harness-specific file.

For visual checks, see the cross-harness [browser testing guide](../guides/browser-testing.md) and optional [browser visual validation skill](../skills/browser-visual-validation/SKILL.md). Check current official documentation before installing or configuring an integration.

The optional Claude Code and Cursor Graphify session-start hook examples are documented in [hook guidance](../hooks/README.md). Choose one runtime-specific example, install its matching script, and follow the Graphify skill's freshness instructions; the examples do not install Graphify or rebuild the index. For new harness integrations, use the [hook contract template](../docs/templates/hook-contract.md) and verify the harness's current official hook documentation.
