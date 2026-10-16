# Repository guidance

This repository is a multilingual library of AI-assisted software engineering guidance and project starter assets. English is the first complete package; Portuguese (Brazil) follows after the English structure stabilizes.

## Working here

- Read [README.md](README.md) and [en/README.md](en/README.md) to understand the library and its layout.
- Keep language packages self-contained. Do not mix English and Portuguese content in a language package.
- Treat `en/docs/agreements/` as reusable project agreement starters, not as a description of this repository's own technology stack.
- Skills should be portable, task-scoped, and progressive: keep `SKILL.md` procedural and move substantial detail into linked references or templates.
- Keep recommendations adaptable. A project’s own documented decisions and applicable law take precedence over generic starter guidance.
- Make brainstorming optional. A developer who already understands the desired change may proceed directly to a spec, or use the project's lightweight workflow for a small change.
- Separate deterministic checks from model-based review. Report evidence, avoid speculative findings, and never imply that AI review replaces human review or CI.
- Prefer strong models for architecture, security-sensitive reasoning, and final review. Delegate bounded, independent discovery or implementation when useful; use lower-cost models when the task is well specified.
- Use Git worktrees when parallel writers need isolation or when a long-running change should be separated from the active checkout. Avoid worktrees for tiny sequential changes or shared files with unresolved contracts.
## Quality bar

- Keep examples internally consistent and usable on Windows, macOS, and Linux unless a harness explicitly limits support.
- Do not invent package versions, legal conclusions, or security guarantees. Ask project owners to verify licenses and compliance obligations against authoritative sources.
- Update relevant docs/templates when changing a convention, skill, or harness adapter.
- Use conservative, opt-in hook examples. Hooks should invoke deterministic local checks and must not silently perform destructive actions, install tools, transmit source, or auto-fix findings.
