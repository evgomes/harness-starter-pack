---
name: graphify
description: Graph-first code discovery for this repository using a local Graphify AST index. Use for unfamiliar flows, architecture questions, callers, dependencies, the impact of changing a symbol, or the path between two symbols - anything that would otherwise mean reading whole files to find where something lives. Do not use for editing a file you already know, and never as the only evidence behind a code change.
---

# Graphify code navigation

A local AST graph of this repository, so finding code costs a bounded query instead of a broad read.
Graphify is a map, not an authority: it misses dynamic dispatch, dependency injection, reflection,
generated code, string-based registration, and anything its parser cannot resolve.

Everything stays on this machine. No API keys, no remote extraction, and no Graphify-native watchers or
hooks. A project may optionally install the starter pack's read-only harness session-start readiness
hook; that hook only checks setup and index freshness. Do not enable Graphify's own integrations or run
`graphify update` — the incremental path has proven unstable on Windows and can contaminate a code-only
manifest with Markdown nodes. The refresh scripts always do a clean, code-only rebuild.

## Requirements

- The Graphify CLI on the `PATH` — for example `uv tool install graphifyy` (the package name has two
  `y`s; the command is `graphify`). Record the version in `docs/agreements/dependencies.md` under *Tooling*.
- One refresh runtime: PowerShell 7+ (`pwsh`) for `scripts/refresh-graph.ps1`, or Python 3.9+ for
  `scripts/refresh-graph.sh` (Bash) and `scripts/refresh-graph.py`. The Bash/Python path is intended for
  macOS and Linux; the PowerShell path works on all three operating systems.
- `graphify-out/` in `.gitignore`, and a `.graphifyignore` that excludes the same paths as the script.

If any of these is missing — `graphify` not found, the script refusing to run, no `.graphifyignore` —
stop and use the `graphify-setup` skill. Do not install tools or rewrite ignore files from here.

## Keep the index fresh

Before your first graph query in a task:

```powershell
pwsh ./.claude/skills/graphify/scripts/refresh-graph.ps1
# macOS/Linux alternative:
bash ./.agents/skills/graphify/scripts/refresh-graph.sh
```

(Use the path the skill was installed to — `.agents/skills/…` in Codex and Cursor. The copies are
identical.)

It hashes the supported source files against Graphify's manifest, skips the work when nothing changed,
and rebuilds when a file was added, removed, renamed or edited. A rebuild takes seconds; a stale graph
costs a wrong answer.

Run the platform-appropriate script again **after** adding, removing, renaming or editing source, before
you finish the task, so the next session starts current. Documentation-only changes do not need a rebuild.

- `-CheckOnly` (PowerShell) or `--check-only` (Bash/Python) reports freshness and changes nothing. Exits
  `2` when stale.
- `-Force` (PowerShell) or `--force` (Bash/Python) rebuilds regardless. For repairing or benchmarking
  the graph, not for routine work.

The script refuses to run if `graphify-out/` is tracked by Git or not ignored — the graph is a local
artifact and must never be committed.

## Query discipline

Start with the cheapest operation that could answer the question.

| Question | Command |
|---|---|
| An unfamiliar concept or flow | `graphify query "<question>" --budget 800` |
| A known symbol and what touches it | `graphify explain "<symbol>"` |
| How two known things connect | `graphify path "<source>" "<target>"` |
| What a change to a symbol could break | `graphify affected "<symbol>" --depth 2` |
| Where to start in a repository you do not know | `graphify god-nodes --top 10` |

Raise the budget only when a scoped result was relevant but incomplete, and normally stay at or under
1,500 tokens. The code-only build writes no `GRAPH_REPORT.md`; for a broad architecture question, start
from `god-nodes` and `query` rather than dumping `graph.json`.

Symbol names are matched loosely (`parse_config` finds `parse_config()`). When a command answers *"No
unique node match"*, the name is ambiguous or absent: run a `query` with it and reuse the exact label it
prints.

`affected` is the start of an impact analysis, not the end of it: it follows parsed calls, imports and
inheritance in reverse, so callers through dependency injection, reflection, events or string-based
registration are missing. Pair it with a bounded `git grep` for the symbol name before declaring a change
safe.

Use the output to choose a few source locations — then **read those lines and verify** before editing or
asserting anything. Treat `EXTRACTED` edges as parser evidence and `INFERRED` or `AMBIGUOUS` edges as
hypotheses.

## When to use something else

Graphify answers "where does this live" and "what connects to what". It does not answer "every place
this string appears".

Use bounded `git grep` instead when you need an exhaustive exact match, when the construct is one the
parser does not support, or when a query returns nothing useful after you have tried the exact domain
identifiers from the request. Say why the graph was insufficient rather than silently falling back.
