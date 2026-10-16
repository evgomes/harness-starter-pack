# Codex adapter

Codex recognizes repository `AGENTS.md` files as project instructions. Use the shared [English instructions](../../AGENTS.md) as the source of truth, and keep any target project's root `AGENTS.md` concise with links to its own agreements. Codex can load reusable skills on demand; install project skills in `.agents/skills/<skill-name>/` and retain their relative references/scripts.

## Setup

1. Copy or adapt `en/AGENTS.md` to the target repository root.
2. Copy the selected agreement starters to `docs/agreements/` and complete them with project facts.
3. Copy each selected skill directory into `.agents/skills/`.
4. If instructions are split by directory, add scoped `AGENTS.md` files only where local rules materially differ.

Official reference: [Codex workflow guide](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex).
