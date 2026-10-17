# Feature specification: Starter pack installer

> Status: Accepted
> Owner: Repository maintainer · Date: 2026-10-16 · Branch: `codex/starter-pack-installer` · Related exploration/handoff: none

Acceptance criteria and key choices were reviewed through the developer's responses on 2026-10-16. Implementation may proceed.

## 1. Problem and outcome

- Problem / user need: The starter pack is currently applied manually, which is repetitive and makes it easy to omit agreements, stack recommendations, skills, or harness-specific files.
- User summary: As a developer, I want an interactive cross-platform installer for a new or existing repository so that I can select the relevant starter-pack content and install it consistently without accidentally losing project files.
- Intended outcome: Provide a dependency-free setup command that guides a developer through choosing a destination mode and a tailored set of English assets, previews changes, and handles existing files safely.
- Why now: The English pack has an initial set of shared agreements, templates, skills, harness adapters, and ASP.NET Core/React profiles.

## 2. Scope

### In scope

- A cross-platform installer using a runtime already needed or documented by this pack (proposed: Python 3.9+ standard library).
- Modes for scaffolding a new project directory or adding selected starter-pack assets to an existing repository.
- Interactive selections for language when available, stack profile(s), harness adapter(s), and optional skills/content.
- A polished interactive console wizard with color where supported, clear step/progress presentation, and a readable no-color fallback.
- A preview/dry-run and a clear file-by-file result.
- Safe, explicit handling of destination collisions; skip by default and offer backup-and-replace only after confirmation.
- An optional prompt to initialize Git for a new destination.
- Quick-start documentation describing manual use and installer use.

### Out of scope

- Creating the application itself with `dotnet new`, `npm create`, or another stack-specific project generator.
- Installing harnesses, models, browser tools, Graphify, external dependencies, or global configuration.
- Translating English assets or installing the unfinished `pt-br` package before it is ready.
- Automatically merging arbitrary existing Markdown instructions or changing an existing Git repository's remotes/branches.

## 3. Context and constraints

- Relevant existing behavior and architecture: English content is under `en/`; shared agreements/templates, skills, harness adapters, stack profiles, and root docs have separate folders. `pt-br/README.md` currently points to the English pack until translation is complete.
- Source references: `README.md`, `en/README.md`, `en/AGENTS.md`, `en/docs/agreements/`, `en/docs/templates/`, `en/harnesses/`, and `en/stacks/`.
- Dependencies and constraints: Cross-platform Windows/macOS/Linux; Python 3.9+; no vendor lock-in; preserve or correctly rebase relative links when copying skill directories; no third-party runtime dependency proposed.
- Confirmed facts: This repo has English content ready and separate `aspnet-core` and `react` profiles. Harness instructions are thin entry points and skills can have relative supporting resources.
- Assumptions to prove: The interactive flow and safe conflict policy are usable on supported terminals; project-local installation is preferred to global harness configuration; selected assets can be copied without rewriting their substantive guidance.

## 4. Requirements and acceptance criteria

| ID | Requirement / scenario | Acceptance evidence |
|---|---|---|
| AC-01 | Given a developer on Windows, macOS, or Linux with the documented Python runtime, when they run the installer interactively, then the same core flow and content selections are available on that platform. | Manual invocation on available platform(s), platform-neutral path tests, and documented prerequisites. |
| AC-02 | Given a new destination, when the developer selects the English package, stack profile(s), harness adapter(s), and skills, then the installer creates the directory structure, always installs all five shared agreements, common templates, and portable skill reference library, and activates only selected stacks, harnesses, and skills (plus required skill dependencies). Available profiles include ASP.NET Core, React, and an integrated ASP.NET Core + React bundle for a single repository; selecting the bundle includes its integrated guidance and both individual profiles' technology-specific guidance. `graphify` and `graphify-setup` are preselected in the skills menu but may be deselected. | File inventory comparison against selections; preserve relative links and supporting assets. |
| AC-03 | Given an existing repository, when the developer selects content, then the installer previews intended changes and preserves every existing file by default. | Run against a fixture containing tracked-looking and conflicting files; verify byte-for-byte preservation for skipped conflicts. |
| AC-04 | Given a destination path that contains files, when the developer requests preview or cancels, then no files are created, overwritten, or deleted. | Dry-run and cancellation inspection on a fixture directory. |
| AC-05 | Given one or more file conflicts, when the installer reaches conflict handling, then skipping is the default and backup-and-replace is offered only after explicit confirmation; each replaced file is backed up under a timestamped destination backup directory. | Conflict fixture verifies default action, explicit confirmation, backup contents, and restoration path. |
| AC-06 | Given malformed options, inaccessible paths, or copy errors, when installation fails, then it reports the failing path and reason, returns a non-zero status, and leaves already-existing content intact. | Simulated invalid path and write failure; inspect error output and destination. |
| AC-07 | Given a successful or partial install, when it completes, then it reports installed, skipped/conflicting, and failed files and explains the next manual step for files not automatically integrated. | Review CLI output and quick-start documentation. |
| AC-08 | Given an English-only release, when the installer asks for a language, then it does not imply the Portuguese package is complete or install it as a complete equivalent. | Interactive flow and docs inspection. |
| AC-09 | Given a supported terminal, when the wizard runs, then it presents clear colored headings, selection steps, progress, and results; when color is unsupported or disabled, all information remains readable without escape artifacts. | Inspect TTY, no-color, and non-interactive output behavior. |
| AC-10 | Given a new destination, when the developer chooses Git initialization, then the installer asks before running `git init`; declining leaves Git metadata untouched and explains how to initialize later. | Verify both choices against an isolated temporary destination. |
| AC-11 | Given an interactive terminal, when the developer chooses the destination mode or language, then they can navigate a colorized single-choice menu without typing option numbers; when choosing stacks, harnesses, or skills, they can toggle multiple items in a colorized checklist. The filesystem path remains a text entry. | Exercise keyboard selection behavior in focused tests and document key bindings; retain text fallbacks for non-interactive input. |
| AC-12 | Given the user is in any wizard step after the first, when they press Back, then the wizard returns to the previous step and preserves existing selections; required destination and language fields must be valid before the user can advance, while stack, harness, and skill selections may be empty. The review step allows going back before applying. | Focused tests for back navigation/retained selections and required path validation; inspect flow and docs. |

## 5. Design and decisions

- Proposed design and boundaries: Add a Python CLI under `scripts/` at the repository root. Treat this source repository as the asset catalog and use explicit asset mappings for copy selection. Copy the portable skills reference catalog under `skills/`, but make individual skills optional in harness-discovery directories; preselect `graphify` and `graphify-setup`. Always copy all five shared agreements and common templates. Keep all writes inside the chosen destination. Add a `--dry-run` mode and avoid non-interactive flags unless they can share the same validation and collision rules as the interactive flow.
- Alternatives considered and tradeoffs:
  - Manual copy: zero tooling cost but easy to omit files and tedious to repeat.
  - Platform-specific shell installers: familiar but duplicates behavior and increases drift across PowerShell, Bash, and macOS/Linux environments.
  - Python standard-library CLI: one implementation across supported desktop OSes; adds Python as a documented prerequisite.
  - Package manager or remote bootstrap command: convenient but introduces remote code execution and environment/dependency concerns; not proposed for the first version.
- Accepted decisions and decision owner: Use a Python standard-library CLI; always include all five common agreements and shared templates; make stacks and harnesses opt-in; make skills individually optional in harness discovery, with `graphify` and `graphify-setup` preselected; skip collisions by default and offer explicit backup-and-replace; offer Git initialization for new destinations; and use a polished color-capable console wizard. Initial decisions confirmed by the developer on 2026-10-16; skill defaults confirmed by the developer on 2026-10-17.
- Open questions / blockers: None. No-color behavior will follow standard terminal conventions and include a `--no-color` option.
- Security, privacy, accessibility, operations: Validate the destination path; do not follow symlinks outside the chosen target; do not remove files; require explicit consent before any replacement; do not fetch or execute remote code; make output understandable to screen readers and terminal users.

## 6. Proofs and implementation slices

No assumption requires an independent proof before the plan can be trusted; Slice 1 is the first delivery slice.

| Slice / subitem | Description and owned files/contracts | Acceptance evidence | Status | Evidence / note |
|---|---|---|---|---|
| 1.1 | Define asset selection manifest and target layout in `scripts/`; preserve nested skill files and relative links. | AC-02 fixture inventory and link check. | Complete | Seven focused unit tests cover selected assets, required skill dependencies, generated Claude entry point, and relative link rebasing. |
| 1.2 | Implement cross-platform interactive selection, preview, safe conflict policy, and clear results. | AC-01, AC-03 through AC-07 using isolated temporary fixtures. | Complete | Tests cover parent traversal rejection, dry-run non-creation, default skip, confirmed backup-and-replace, and optional Git initialization. Windows test run passed; macOS/Linux execution was unavailable. |
| 1.3 | Document manual and installer quick starts, prerequisites, choices, limitations, and examples. | AC-07, AC-08 and docs review. | Complete | Added `scripts/README.md` and linked it from root and English READMEs. Reviewed English-only language behavior and conflict/Git-init instructions. |
| 2.1 | Perform final integrated verification and one adversarial review against the accepted spec. | AC evidence table complete; review findings recorded. | Complete | Final review covered navigation, retained selections, required path validation, terminal fallbacks, collisions, and file safety; no blocking issues found. `git diff --check` passed. Twelve focused tests passed on Windows; other OS runtime checks remain outstanding. |
| 2.2 | Add keyboard-driven selection menus for destination mode, language, stacks, harnesses, and optional skills; retain text fallbacks. | AC-11 keyboard-selection tests and documentation review. | Complete | Single-choice menus use Up/Down and Enter; multi-select menus add Space and A. Filesystem paths remain typed/pasted. |
| 2.3 | Add back/forward navigation, preserve selections when revisiting steps, and validate required inputs before advancing. | AC-12 navigation and path validation tests; review/install step permits returning before changes are written. | Complete | Left arrow returns to prior step; right arrow/Enter continues; text prompts offer B/back. Blank required destination paths are rejected; prior path and selections are retained when revisiting. |

## 7. Verification and release

- Focused checks per slice: Run the CLI only against temporary fixture directories; inspect resulting files and collisions. Do not operate on a user's real destination during development.
- Full test suite to run once after all spec slices are implemented: repository-specific tests added for the installer, if accepted in the implementation plan.
- Other checks: Python syntax/lint checks only if adopted by the repository; markdown/local-link review for documentation.
- Manual checks: Windows PowerShell, macOS, and Linux shell environments when available; otherwise record unavailable platforms and evidence.
- One adversarial review at the end against the full spec and final diff; use a strong model when available, otherwise have the engineer run the review skill manually.

## 8. Amendments

| ID / date | Proposed deviation and reason | Impact on scope / slices / acceptance / evidence | Decision and source | Status |
|---|---|---|---|---|
| A-01 / 2026-10-17 | Preselect `graphify` and `graphify-setup` while keeping skills deselectable; make explicit that all five agreements and shared templates are always included. | Updates AC-02 and the installer selection default; no new assets or scope. Focused verification remains pending for this follow-up. | Developer request in this conversation. | Accepted; docs and implementation updated, verification not run. |
| A-02 / 2026-10-17 | Add an integrated ASP.NET Core + React stack profile for projects where both are maintained in one repository. | Adds one selectable bundle, its combined architecture/conventions guidance and full-stack spec/verification templates, plus the two standalone profiles for technology-specific guidance; updates stack catalog and installer docs. Focused verification remains pending. | Developer request in this conversation. | Accepted; docs and implementation updated, verification not run. |

## 9. Acceptance criteria review

- [x] Engineer reviewed acceptance criteria and selected defaults for Git initialization, conflicts, and skill selection.
- [x] Acceptance criteria are observable and have evidence plans.
- [x] Engineer accepted the spec before implementation began.

## 10. Change log

| Date | Change | Decision owner/source |
|---|---|---|
| 2026-10-16 | Initial draft after pushing the starter pack baseline. | Developer request |
| 2026-10-16 | Accepted installer approach and decisions; requested polished colored console wizard. | Developer replies |
| 2026-10-16 | Implemented Python wizard, safety behavior, harness/stack/skill selection, platform-aware color, docs, and focused tests; verified final changes. | Installer implementation |
| 2026-10-16 | Developer requested selecting multiple items with a checklist UI instead of typing numbers; added arrow-key navigation, Space toggle, A toggle-all, Enter confirm, Q cancel, and retained a text fallback. | Developer follow-up |
| 2026-10-16 | Developer requested keyboard selection for destination mode and language as well; added single-choice keyboard menus while retaining typed path entry. | Developer follow-up |
| 2026-10-16 | Developer requested back/forward navigation and required-step validation; added persistent wizard state, back controls, path validation, and a review choice before applying changes. | Developer follow-up |
| 2026-10-17 | Preselected `graphify` and `graphify-setup` in the skills menu while retaining the ability to deselect them; documented the always-included five agreements and shared templates. | Developer follow-up |
| 2026-10-17 | Added an integrated ASP.NET Core + React profile for a single repository and exposed it in the installer. | Developer follow-up |
