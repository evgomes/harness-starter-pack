# Claude Code project adapter

At the start of a task, read the project's root `AGENTS.md` and the relevant files in `docs/agreements/` as the shared engineering contract. Keep this file as a short Claude Code entry point; do not duplicate the full agreement set.

When installing the starter pack, copy selected reusable skills into `.claude/skills/<skill-name>/` and preserve each skill's references, assets, and scripts. Read a skill only when the task matches its description. Configure Claude Code hooks only for deterministic checks with clear failure behavior; keep AI review as an explicit workflow skill.

The optional Graphify session-start hook has PowerShell and Bash configurations in `../../hooks/adapters/`. Install one matching hook script and configuration only when the project uses Graphify; use Bash plus Python 3.9+ on macOS/Linux, or PowerShell 7 on Windows. Follow `../../hooks/README.md` and `../../skills/graphify/SKILL.md` when checking or refreshing the index.

Before implementation, inspect project instructions and the applicable agreements. Brainstorming is optional; use it only when clarifying the problem or comparing solutions would add value. Update the handoff when work pauses or changes owners.

Official references: [Claude Code memory](https://code.claude.com/docs/en/memory), [skills](https://code.claude.com/docs/en/skills), and [hooks](https://code.claude.com/docs/en/hooks).
