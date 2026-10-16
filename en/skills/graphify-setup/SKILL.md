---
name: graphify-setup
description: Install and wire up the Graphify code graph in a repository - installs the graphify CLI (package graphifyy), ignores graphify-out/, writes a .graphifyignore that matches the refresh script, installs the graphify navigation skill for the chosen harnesses, records the tool in docs/agreements/dependencies.md, builds the first index and proves it with a query. Use when a repository has no code graph yet, when the graphify command is missing on a machine, when a teammate clones a repository that uses the graph, when upgrading Graphify, when removing it, or when the refresh script keeps reporting the index as stale. Not for querying the graph - that is the graphify skill.
---

# Setting up Graphify in a repository

The `graphify` skill navigates a local code graph; this skill puts that graph in place and keeps the
installation honest. The end state is the same in every repository:

- the `graphify` CLI on the `PATH`, its version recorded in `docs/agreements/dependencies.md`;
- `graphify-out/` ignored by Git and never tracked;
- a `.graphifyignore` whose paths match the exclusion list at the top of the refresh script;
- the `graphify` skill (with the PowerShell and Bash/Python refresh scripts) in the skill folder of
  every agent the team uses, committed;
- a fresh index, verified by the platform-appropriate refresh script's check-only mode exiting `0`
  and by one real query.

**What this setup deliberately leaves out**, and why — say so if the user asks for any of it:

| Graphify feature | Why it is not used here |
|---|---|
| Semantic extraction (docs, papers, images through an LLM backend) | Needs an API key and sends repository content to a provider. The graph here is code-only and local |
| `graphify update`, `graphify watch`, `graphify hook install` | The incremental path has proven unstable on Windows and can mix Markdown nodes into a code-only manifest. The refresh script does a clean, verified rebuild instead, and is fast enough for that |
| `graphify claude install`, `codex install`, `cursor install`, `install --platform …` | They write always-on instructions (a `CLAUDE.md` section, an `AGENTS.md` section, `.cursor/rules/graphify.mdc`, a `PreToolUse` hook) that tell the agent to run `graphify update .` and to query the graph before *every* read. That contradicts the refresh policy and duplicates the instructions this process already ships in `AGENTS.md` and the skill |

If a repository already has any of those, list what you found and propose removing it with the matching
`graphify <platform> uninstall` / `graphify hook uninstall` — do not remove it without agreement.

---

## 0. Look before changing anything

Run these and report the result as a short table before installing or writing anything:

```bash
graphify --version                      # the CLI, and which version
pwsh --version                          # optional; needed only for the PowerShell refresh path
python3 --version                       # Python 3.9+ is needed for the Bash/Python refresh path
git rev-parse --show-toplevel           # must be inside a Git repository
git check-ignore graphify-out/graph.json # must report the ignore rule
git ls-files -- graphify-out            # must print nothing
```

Inspect `.graphifyignore` and the chosen harness skill folder (`.claude/skills/` or `.agents/skills/`);
do not assume either exists. PowerShell is required only for the `.ps1` refresh script; macOS/Linux can
use Bash and Python 3 instead.

Also look for leftovers of Graphify's own integrations: a `## graphify` section in `CLAUDE.md` or
`AGENTS.md`, `.cursor/rules/graphify.mdc`, a graphify entry under `hooks` in `.claude/settings.json`, and
`post-commit`/`post-checkout` hooks that call `graphify`.

Then do only the steps that are missing. On a machine where everything is already in place except the
CLI (a fresh clone), steps 1 and 5 are the whole job.

## 1. Install the CLI

Installing a tool on the user's machine is their call: say what you will run and wait for a yes.

```bash
uv tool install graphifyy        # preferred: isolated, upgradable, puts `graphify` on the PATH
pipx install graphifyy           # alternative when uv is not available
```

- The package is **`graphifyy`, with two `y`s**; the command is `graphify`. Do not "correct" the name to
  one `y` — that is not this project.
- Never `pip install` it into the project's own virtual environment or add it to the project's
  dependency files. It is a developer tool, like a linter installed globally, not something the
  application ships.
- If `graphify` is not found after installing, run `uv tool update-shell` (or `pipx ensurepath`) and
  open a new shell.
- For the PowerShell refresh path, PowerShell 7 is required: `winget install Microsoft.PowerShell`,
  `brew install powershell`, or the distribution's package. The macOS/Linux Bash path requires Bash and
  Python 3.9+ (standard library only).

Check with `graphify --version`, and record that version in the next step.

## 2. Record it

In `docs/agreements/dependencies.md`, under *Tooling*, keep one row:

```markdown
| Graphify (`graphifyy`) | x.y.z | Local code graph for navigation. Writes `graphify-out/`, which is git-ignored |
```

Use the version you actually installed. If the team pins a version, the install command becomes
`uv tool install graphifyy==<version>` — write that in the row's description.

## 3. Ignore the output, and decide what the graph never indexes

1. `.gitignore` must contain `graphify-out/`. If `git ls-files graphify-out` printed anything, the graph
   was committed at some point: `git rm -r --cached graphify-out` in its own commit, and tell the user
   (the old blobs stay in history — harmless for a graph, but say it).
2. `.graphifyignore` lives at the repository root. Start from this starter pack's root example, or
   write it with the same entries the refresh script excludes:

   ```gitignore
   graphify-out/
   .claude/
   .agents/
   .codex/
   .cursor/
   .opencode/
   .git/
   **/node_modules/
   **/dist/
   **/build/
   **/bin/
   **/obj/
   ```

3. Add the stack's own noise **to all exclusion lists in the same change** — `.graphifyignore`,
   `$excludedFolders` / `$excludedFileSuffixes` in `scripts/refresh-graph.ps1`, and
   `EXCLUDED_FOLDERS` / `EXCLUDED_FILE_SUFFIXES` in `scripts/refresh-graph.py`: generated clients,
   vendored code, migration snapshots, minified bundles, and large fixtures. A path indexed by one and
   enumerated by another makes the freshness check report "stale" forever.

Graphify also honours `.gitignore`, so anything already ignored there does not need repeating — except
the agent folders above, which are usually committed but must never be indexed.

## 4. Install the navigation skill for each chosen harness

Copy the complete `graphify` directory (including `scripts/refresh-graph.ps1`, `scripts/refresh-graph.sh`,
and `scripts/refresh-graph.py`) and this setup skill into the selected project skill roots. Preserve each
skill's directory structure and any existing files:

| Agent | Project skill folder |
|---|---|
| Claude Code | `.claude/skills/graphify/` and `.claude/skills/graphify-setup/` |
| Codex, Cursor, and OpenCode | `.agents/skills/graphify/` and `.agents/skills/graphify-setup/` |

Commit the skill folders so teammates receive the same refresh process. If a harness only discovers
skills in its own folder, copy the same source skills there too. Do not maintain divergent copies.

Make sure the agent instructions mention the graph — the starter pack does this in `AGENTS.md`.
In a repository without the template, add one line to whichever instruction file the agents load:
*"Refresh the code graph (`graphify` skill) before
your first graph query in a task and after changing source code."*

## 5. Build the first index and prove it

```powershell
pwsh ./.claude/skills/graphify/scripts/refresh-graph.ps1          # clean, code-only rebuild, verified
pwsh ./.claude/skills/graphify/scripts/refresh-graph.ps1 -CheckOnly   # must say "fresh" and exit 0
```

(Use whichever agent folder holds the script; the copies are identical. On macOS/Linux, use the
equivalent Bash/Python scripts:)

```bash
bash ./.agents/skills/graphify/scripts/refresh-graph.sh             # rebuild and verify
bash ./.agents/skills/graphify/scripts/refresh-graph.sh --check-only # must say "fresh" and exit 0
```

Then prove the graph answers a real question about *this* repository:

```bash
graphify god-nodes --top 5                       # the hubs — do they look like the real core?
graphify explain "<a symbol you know exists>"    # its file and line must match the source
```

Report: the Graphify version, the number of indexed files, the top hubs, and whether `explain` pointed
at the right file and line. If the indexed-file count is far from the number of source files you expect,
the exclusions are wrong — fix them now, not later.

## Upgrading

```bash
uv tool upgrade graphifyy        # or: pipx upgrade graphifyy
```

Then rebuild with `-Force` on PowerShell or `--force` on Bash/Python (a new version may change the graph format or the manifest), run the proof
in step 5 again, and update the version in `docs/agreements/dependencies.md` in the same commit. If the upgrade
breaks the script — a flag renamed, the manifest reshaped — say so with the error output, and pin the
previous version until the script is fixed.

## Removing it

Delete the `graphify` (and `graphify-setup`) skill folders from every agent folder, `graphify-out/`, the
`.graphifyignore`, the `.gitignore` line, the `dependencies.md` row, and the graph rules in `AGENTS.md` /
`CLAUDE.md` / project workflow agreement — all in one commit. Then `uv tool uninstall graphifyy` on each machine,
if nothing else uses it.

## When the refresh script misbehaves

| Symptom | Cause, and the fix |
|---|---|
| `-CheckOnly` / `--check-only` says "stale" right after a rebuild | `.graphifyignore` and the scripts' exclusions disagree. Make them match |
| "graph contains Markdown nodes" | Someone ran `graphify update` or a non-`--code-only` extract. Rebuild with the script; it starts clean |
| "Refusing to rebuild until graphify-out/ is ignored" / "contains tracked files" | Step 3 is incomplete |
| `graphify: command not found` inside the script | The CLI is not on the `PATH` of the shell that runs the refresh script. `uv tool update-shell`, then open a new shell |
| `python3: command not found` on macOS/Linux | Install Python 3.9+ or use the PowerShell refresh script if `pwsh` is available |
| Extraction fails on one file | A parser edge case. Exclude that file in both lists, note it in the commit, and report it upstream |
| Rebuild takes minutes | Something large is being indexed — usually build output or vendored code that is not ignored |
