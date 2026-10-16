# Hook and check guidance

Hooks are harness-specific lifecycle integrations. Keep the shared guidance here tool-neutral and review each harness's current official hook documentation before adding a configuration to a consuming project.

## Initial hook set

The starter pack includes one optional Graphify session-start check. Install the script and the matching harness example only when the project uses Graphify. It checks whether the CLI, project configuration, navigation skill, and index are ready, then adds a short instruction to the agent context when something needs attention. It does not install software, write project files, access the network, or rebuild the index.

| Check | Initial placement | Why |
|---|---|---|
| Graphify readiness | Optional session-start hook for Claude Code and Cursor | Fast local checks; directs setup to the explicit `graphify-setup` skill |
| Formatting and linting | Project commands and CI; optionally an after-edit hook for fast, scoped formatters | Commands, runtimes, and safe auto-fix behavior are project-specific |
| Tests | Project workflow and CI; optionally a targeted post-edit hook | A full suite can be slow and should not run after every edit by default |
| Dependency, license, and advisory review | `dependency-review` skill plus scheduled CI | Requires registry/advisory data and an owner for findings |
| Security and accessibility review | Explicit skills plus project CI scanners | Requires changed-code context and, for some checks, human evidence |
| Shift-left code review | Explicit `shift-left-code-review` skill or review command | Model review is variable in cost and should happen at an agreed review point |

Do not install all examples blindly. Choose hooks that fit the repository's tools and lifecycle, document how to disable them, and keep slow or model-driven work outside per-edit events.

### Graphify startup hook

There are equivalent session-start scripts for PowerShell and Bash:

- [`scripts/graphify-session-start.ps1`](scripts/graphify-session-start.ps1) uses PowerShell 7 (`pwsh`) and Git on Windows, macOS, and Linux.
- [`scripts/graphify-session-start.sh`](scripts/graphify-session-start.sh) uses Bash and Git on macOS/Linux, plus Python 3 to check index freshness.

Both emit the output format expected by the selected harness:

- Claude Code: choose the [PowerShell example](adapters/claude-code.settings.example.json) or [Bash example](adapters/claude-code.settings.bash.example.json), then merge it into the project's `.claude/settings.json`.
- Cursor: choose the [PowerShell example](adapters/cursor.hooks.example.json) or [Bash example](adapters/cursor.hooks.bash.example.json), then merge it into `.cursor/hooks.json`.

The Bash hook invokes the cross-platform [`refresh-graph.sh`](../skills/graphify/scripts/refresh-graph.sh), which delegates index checks and rebuilds to the Python 3 standard-library implementation. Hook installation is opt-in and may add agent context at session start. Both hooks are read-only; use the `graphify-setup` skill for explicit setup or repair. A stale index is reported but not rebuilt automatically, because rebuilding can take time and replaces the generated `graphify-out/` directory.

For the selected example, copy the corresponding hook script into the target project's `.agents/hooks/`, then merge the example into its existing harness settings. Also copy the complete Graphify skill directory (including the platform-appropriate refresh scripts) into a supported project skill folder. Claude Code project hooks can be committed and shared; Cursor project hooks run in trusted workspaces, so review the command before enabling it.

Codex and OpenCode are not wired to this script by default. Their integration and extension models differ; use the shared skill and workflow until a project has an appropriate, maintained hook mechanism.

## What belongs in a hook

- Fast, deterministic, local checks with known inputs and clear exit behavior: formatting, linting, generated-file checks, or a narrowly scoped test command.
- A short timeout and useful output so failures help the developer act.
- An explicit opt-in path for checks that are slow, require network access, or may modify files.

## What belongs in a skill or CI instead

- Model-based code review belongs in the explicit `shift-left-code-review` skill (or a deliberate review command). Choose a strong reviewer model for architecture/security judgment; keep findings evidence-based and auditable. Do not run model review after every file edit.
- OWASP/security and WCAG/accessibility workflows need context and often manual evidence; use their skills and CI scanner gates at agreed lifecycle points.
- Dependency and license checks need registry/advisory data and a recurring schedule. Run them in approved CI or scheduled automation and route findings to an owner; an agent hook or skill cannot wake itself periodically.

## Safe integration principles

- Do not install tools, upgrade dependencies, auto-fix code, push commits, publish data, or make network requests implicitly from a hook.
- A hook should not send source code or personal data to a model or external service.
- Avoid heavyweight checks on every tool call. Prefer changed-file scope and reserve full suites for the project's agreed gates.
- Hooks report; they do not replace code review, CI, threat modeling, penetration testing, or accessibility evaluation.
- Document triggering event, command, runtime requirements, timeout, failure effect, and bypass/disable procedure.

## Authoring optional hooks

Use the [hook-authoring skill](../skills/hook-authoring/SKILL.md) and [hook contract template](../docs/templates/hook-contract.md) to plan a hook before writing harness configuration. The contract is a design checklist, not a shared configuration schema: event names, payloads, permissions, trust prompts, timeout rules, and output formats vary by harness and can change. Check the selected harness's current official documentation and record the version or review date.

Keep the implementation narrow and predictable. Define inputs, outputs, exit behavior, supported operating systems, missing-prerequisite behavior, side effects, network/data handling, secrets, and disable/removal steps. Provide a manual command for the same check and a CI counterpart when it gates delivery. Validate success, finding, missing-tool, timeout, and error paths on supported platforms. Do not silently install tools, mutate source, access the network, or weaken project security settings. Merge with existing configuration and follow harness trust/approval behavior.

Choose the lightest appropriate mechanism: explicit instructions or a skill for contextual/model-based work; a local hook for a fast deterministic check; CI or scheduled automation for authoritative or recurring checks. Avoid putting expensive model reviews, full test suites, or network-dependent audits on every edit event. See the [quality and security agreement](../docs/agreements/quality-and-security.md) for the project check catalog and blocking policy.

## Harness references

- [Claude Code hooks](https://code.claude.com/docs/en/hooks)
- [Cursor hooks](https://cursor.com/docs/hooks)
- [Cursor customization](https://cursor.com/docs/customize-cursor) (rules, skills, subagents)

Codex and OpenCode integrations evolve; check the [harness catalog](../harnesses/README.md) for their current official references before adding lifecycle hooks.
