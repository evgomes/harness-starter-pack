# References and rationale

This guide links to material that informs the starter pack's workflows and stack profiles. The links are references for understanding and evaluating practices; they do not make the pack dependent on a vendor, framework, product, architecture, or workflow tool. Prefer the target repository's agreements and current official documentation when they differ.

**Links checked:** 2026-10-17. Product, model, API, and framework guidance can change; check the source's current version and applicability before relying on it.

## How these references inform the starter pack

| Topic | Rationale reflected in this repository |
|---|---|
| Specs and acceptance criteria | Agree on a reviewable description of user need, scope, context, decisions, evidence, and ordered work before implementation; clarify ambiguity and check consistency rather than treating the first draft as authoritative. |
| Handoffs and context | Persist decisions, progress, evidence, and next action in a concise, inspectable artifact so a new session can load the relevant state without replaying the entire history. A handoff is explicit project memory; it is not prompt cache. |
| Slices and checklists | Break work into ordered, evidence-bearing items. Test the changed behavior at the smallest useful scope during implementation, then run required broad checks at feature completion. A checklist is a progress record, not proof by itself. |
| Subagents and parallel work | The starter pack permits parallel subagents only when the developer explicitly asks; if delegated, keep work bounded and account for coordination and verification cost. |
| .NET and React | Use official platform guidance to inform architecture and coding patterns, then verify the target project's versions, structure, and conventions. Examples are alternatives to evaluate, not mandatory blueprints. |
| Prompt caching | Caching can reuse computation for repeated prompt content. It does not remove tokens from context or act as semantic memory. Cache behavior, supported controls, retention, pricing, and cache-hit conditions are provider-specific. |
| Model selection | Select by task difficulty, risk, context, quality bar, latency, and cost; validate the choice on representative work. Avoid fixed model rankings and price tables in durable project guidance because model lineups and terms change. |

## Specs, checklists, slices, and handoffs

- [GitHub Spec Kit: Spec-Driven Development quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) — one example of clarifying requirements, producing specifications and plans, validating checklists, ordering tasks, and checking consistency. Spec Kit is an optional example, not a required tool for this starter pack.
- [GitHub Spec Kit: Agentic SDD](https://github.github.com/spec-kit/reference/agentic-sdd.html) — reference for the relationships between spec, plan, tasks, implementation, and convergence checks.
- [OpenAI Cookbook: Iterating development workflows with Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex) — example of phase-specific decisions and context files to make long-running development resumable. The workflow assets are optional conventions, not Codex requirements.
- [Google Testing Blog: Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html) — an influential model for separating fast isolated tests from larger integration/system tests. Adapt test categories and execution policy to the project's suite.
- [Context Engineering for AI Agents: Memory, Compaction, and How to Save Tokens](https://fronteiralabs.com.br/en-us/articles/context-engineering-for-ai-agents-memory-compaction-and-how-to-save-tokens/11) — explains context vs memory vs cache, compaction and its context-loss risk, handoffs between sessions, retrieval, and the distinction between caching and reducing context size.
- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — discusses context as a limited working set, retrieval strategies, and keeping subagent research isolated when delegation fits the task.

The corresponding starter assets are [specification](en/docs/templates/spec.md), [handoff](en/docs/templates/handoff.md), and [verification plan](en/docs/templates/verification-plan.md), with the sequencing rules in the [workflow agreement](en/docs/agreements/workflow.md).

## Subagents and parallel runs

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — compares simple workflows, routing, parallelization, and orchestrator-worker patterns, and recommends choosing complexity based on the task.
- [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — practical account of defining focused subtasks and synthesizing results from parallel research.
- [OpenAI Cookbook: Iterating development workflows with Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex) — an example of phase boundaries and context transfer in coding-agent work.

These sources describe possible patterns; the local [workflow agreement](en/docs/agreements/workflow.md) is deliberately more conservative: subagents are used only when the developer asks, and worktrees/parallelism are not assumed.

## .NET and ASP.NET Core

- [Microsoft .NET architecture documentation](https://learn.microsoft.com/dotnet/architecture/) — catalog of architecture guides and reference material for .NET application types.
- [Architect modern web applications with ASP.NET Core and Azure](https://learn.microsoft.com/dotnet/architecture/modern-web-apps-azure/) — end-to-end architecture discussion and a reference implementation. Treat its architecture as one example; validate any pattern against the actual product and current framework.
- [Common web application architectures](https://learn.microsoft.com/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures) — discusses monolithic and layered application structures, dependency direction, and Clean Architecture tradeoffs.
- [Architectural principles](https://learn.microsoft.com/dotnet/standard/modern-web-apps-azure-architecture/architectural-principles) — separation of concerns and maintainability principles.
- [ASP.NET Core best practices](https://learn.microsoft.com/aspnet/core/fundamentals/best-practices) — framework-specific performance and runtime considerations; select the documentation version matching the target application.

The [ASP.NET Core profile](en/stacks/aspnet-core/README.md) and its [architecture](en/stacks/aspnet-core/docs/agreements/architecture.md) and [conventions](en/stacks/aspnet-core/docs/agreements/conventions.md) documents convert relevant concepts into prompts to verify against a real project; they do not require Clean Architecture or a fixed project count.

## React

- [React: Thinking in React](https://react.dev/learn/thinking-in-react) — decomposing an interface into components, identifying visual states, and deriving minimal state from data flow.
- [React: Managing state](https://react.dev/learn/managing-state) — structuring state, sharing state, and avoiding redundant state.
- [React: Sharing state between components](https://react.dev/learn/sharing-state-between-components) — choosing a common state owner when components need coordinated state.
- [React: Reusing logic with custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks) — when to extract focused reusable stateful logic.
- [MDN: Using CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties) — reusable values and cascade-based overrides for CSS design tokens.
- [W3C: Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — normative accessibility success criteria; automated checks are not a substitute for evaluating applicable criteria and user flows.

The [React profile](en/stacks/react/README.md), [UI exploration template](en/docs/templates/ui-design-exploration.md), and [React design templates](en/stacks/react/docs/templates/README.md) encourage existing design-system reuse, explicit UI states, mock data, theme/token evaluation, and accessibility evidence.

## SOLID, code quality, and engineering practices

- [Clean Code: A Handbook of Agile Software Craftsmanship, 2nd edition](https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship-2nd-edition/P200000013239/9780135398579) by Robert C. Martin — publisher reference for readable code, naming, functions, testing, design heuristics, and the SOLID principles. Treat its recommendations as design tools to evaluate in context, not mandatory rules.
- [Google Engineering Practices: Code Review](https://google.github.io/eng-practices/review/) — Google's published review guidance, including design, behavior, complexity, tests, naming, style, and documentation. It is a useful example, not a required process for every team.
- [Microsoft Framework Design Guidelines](https://learn.microsoft.com/dotnet/standard/design-guidelines/) — API and library design guidance for .NET. Its scope is .NET libraries; the page notes that some material may be out of date, so verify relevant recommendations against current framework guidance.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — maintained, topic-specific application security guidance. Select the sheets that match the product's risks; do not treat a generic checklist as a security or compliance determination.

The common [conventions agreement](en/docs/agreements/conventions.md) uses SOLID and Clean Code as prompts for clarity and testability while explicitly discouraging speculative abstractions. The [quality and security agreement](en/docs/agreements/quality-and-security.md) and [security review skill](en/skills/security-review/SKILL.md) tie security practices to the target project's risks and evidence.

## Browser validation

- [Chrome DevTools for agents](https://developer.chrome.com/docs/devtools/agents) and its [setup guide](https://developer.chrome.com/docs/devtools/agents/get-started) explain how an agent can inspect and interact with a live Chrome browser through MCP and related tooling. Browser integrations can expose page content and authenticated sessions, so use isolated profiles and test data.
- [Playwright browser configuration](https://playwright.dev/docs/browsers) distinguishes its managed Chromium build from branded Chrome channels and describes supported browser installation and selection. Use the project's existing runner and browser choice; do not assume a new dependency is needed.
- [OpenAI Browser guide](https://learn.chatgpt.com/docs/browser) documents the integrated Browser on the desktop app surface and distinguishes it from Codex CLI/IDE.
- [Claude Code Desktop](https://code.claude.com/docs/en/desktop) documents local app preview and verification in its Code tab, distinct from the separate Claude Desktop Chat experience.
- [Cursor Browser](https://cursor.com/docs/agent/tools/browser) documents its native agent browser, including visual inspection and console/network capabilities.
- [OpenCode MCP servers](https://opencode.ai/docs/mcp-servers/) documents how to connect optional browser integrations through MCP.

The [browser testing guide](en/guides/browser-testing.md) explains these choices and the [browser visual validation skill](en/skills/browser-visual-validation/SKILL.md) provides a harness-neutral workflow. A rendered browser pass is evidence for the states exercised, not proof of full WCAG conformance or cross-browser correctness.

## Prompt caching and context management

- [OpenAI API: Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching) — current OpenAI-specific cache behavior and controls.
- [Anthropic: Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — current Anthropic-specific cache behavior and controls.
- [Google Gemini API: Context caching](https://ai.google.dev/gemini-api/docs/caching) — current Gemini-specific context caching options.
- [Context Engineering for AI Agents](https://fronteiralabs.com.br/en-us/articles/context-engineering-for-ai-agents-memory-compaction-and-how-to-save-tokens/11) — a conceptual explanation of why memory, compaction, retrieval, and cache are different tools.

When repeated context is large and stable, provider-side caching may improve latency or input cost if the product/API supports it and the request matches the documented conditions. Measure actual cache reads/writes and cost. Do not claim that caching reduces the context-window footprint, guarantees a cache hit, or changes harness behavior unless that harness documents it. For conversational agents, concise instructions, on-demand retrieval, bounded tool output, and accurate handoffs are separate context-management practices.

## Choosing models for task types

- [OpenAI: Model selection](https://developers.openai.com/api/docs/guides/model-selection) — a dynamic task-oriented selection guide; names and recommendations are specific to the current OpenAI offering.
- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — explains routing easy/common tasks to efficient models and escalating work that needs more reasoning.
- [Anthropic: Models overview](https://platform.claude.com/docs/en/models/overview) — current Claude models and specifications.
- [Google Gemini API: Models](https://ai.google.dev/gemini-api/docs/models) — current Gemini model capabilities and availability.
- [OpenAI: Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices) — model/reasoning guidance specific to OpenAI's API.

Use a repeatable comparison set drawn from the project's real tasks. Score correctness, evidence quality, instruction following, regressions, review fixes, latency, and total cost. Keep the least costly/fastest option that consistently meets the required bar for a bounded task; use stronger reasoning for ambiguous, high-impact, architectural, or adversarial-review work. Re-evaluate when model, harness, or pricing changes. Do not copy current names, prices, or provider-specific settings into the vendor-neutral agreements as permanent rules.

## Source-use notes

- Official product/framework documentation is best for current, implementation-specific behavior. Check its version and date.
- Research and engineering articles can explain tradeoffs but do not automatically establish universal best practice.
- Examples are evidence to consider, not instructions to copy without repository context.
- Use the project's architecture, quality/security, and workflow agreements as the local decision record. Add a new reference only when it informs a real choice, and record that choice in the relevant agreement or spec.
