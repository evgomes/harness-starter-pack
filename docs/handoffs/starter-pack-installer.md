# Handoff: Starter pack installer

> Updated: 2026-10-17 · Owner: Codex · Status: Developer onboarding and Graphify setup policy clarified

## Goal and active scope

- Goal: Provide a cross-platform interactive installer for the English starter pack.
- Spec / exploration: [starter-pack-installer spec](../specs/starter-pack-installer.md)
- Branch (confirm repository naming/base-branch rules): `codex/starter-pack-installer`
- Current slice: Clarify developer post-installation responsibilities and require Graphify CLI installation when `graphify-setup` is selected.
- Current subitem (do not advance until all items in current slice are complete): Align setup skill and entry-point docs with the developer's requirement. Installation flow was previously verified on Windows.

## Decisions and constraints

- Accepted decisions (include decision owner/source): Python 3.9+ standard-library implementation; always include all five common agreements and shared templates; stacks and harnesses are opt-in; skills remain individually optional, with `graphify` and `graphify-setup` preselected; conflicts skip by default and offer confirmed backup-and-replace; offer `git init` for new projects; polished color-capable console wizard. Initial decisions accepted by the developer on 2026-10-16; skill defaults requested by the developer on 2026-10-17.
- Constraints / assumptions: English package only; does not install harnesses, external tools, or applications. Runtime testing was possible only on Windows in this environment.

## Progress and changed paths

- Changed files/contracts: installer stack map and generic bundle expansion, dynamic `HARNESS-README.md` generation, a reusable manual template, root/package/installer READMEs, stack and skills catalogs, stack profiles, and reference/spec/handoff docs. Earlier installer implementation also changed `scripts/tests/test_install.py` and `.gitignore`.
- Completed follow-up: Generated overview and documentation update. Both requested installations completed without errors; unit tests and generated-link checks passed. Updated the onboarding checklist and made Graphify CLI installation a required outcome of the selected setup skill.
- Next item in sequence: Review the follow-up diff and run focused installer tests if verification is requested.

| Spec subitem | Status | Focused verification / evidence | Changed paths / note |
|---|---|---|---|
| 1.1 | Complete | Seven focused tests passed; selection, dependencies, generated entry point, and relative links covered. | `scripts/install.py`, tests |
| 1.2 | Complete | Dry run, traversal rejection, collision skip, backup-and-replace, and optional Git initialization covered by tests. | `scripts/install.py`, tests |
| 1.3 | Complete | Reviewed quick-start, prerequisites, selection behavior, limitations, and links. | `scripts/README.md`, `README.md`, `en/README.md` |
| 2.1 | Complete | Final adversarial review included back/forward navigation, retained selections, required path validation, terminal fallbacks, and file safety; no blocking issues found. `git diff --check` passed. Windows only. | Full implementation diff |
| 2.2 | Complete | Keyboard-driven single- and multi-choice menus verified by focused tests; key bindings documented. | `scripts/install.py`, `scripts/README.md`, tests |
| 2.3 | Complete | Back navigation, required destination path checks, retained selections, and review-before-apply covered by flow and tests. | `scripts/install.py`, tests |
| Follow-up 2026-10-17 | Implemented; verification pending | No focused checks run for the changed defaults or documentation in this follow-up. | `scripts/install.py`, READMEs, spec, handoff |
| Follow-up 2026-10-17 combined profile | Implemented; verification pending | No focused checks run for the new profile or installer choice. | `en/stacks/aspnet-core-react/`, `scripts/install.py`, READMEs, spec, handoff |
| Follow-up 2026-10-17 stack catalog | Implemented; verification pending | No checks run. New individual profile folders, integrated bundle, installer selection, README catalogs, and source links need review/verification. | `en/stacks/spring-boot/`, `node-express/`, `python-fastapi/`, `angular/`, `spring-boot-angular/`, `scripts/install.py`, READMEs, `REFERENCES.md` |
| Follow-up 2026-10-17 generated overview | Implemented; verified for selected stack/harness/skills | Installed Spring Boot + Angular into the supplied empty directory (62 files) and Python + FastAPI into the supplied example repository (52 files). Both generated READMEs listed correct profiles, Codex and Graphify skills; all their local links resolved. | `scripts/install.py`, `en/docs/templates/harness-readme.md`, installer docs, two destination folders |
| Follow-up 2026-10-17 onboarding clarification | Documentation updated; review pending | `HARNESS-README` remains developer-facing. Repository README now enumerates post-install agreement, harness, stack-tool, Graphify CLI, and workflow setup steps. `graphify-setup` requires the CLI to be available on the developer machine. | Root/package/installer READMEs, `en/docs/templates/harness-readme.md`, `en/skills/graphify-setup/SKILL.md` |

## Verification evidence

| Check | Command / method | Result | Date |
|---|---|---|---|
| Focused installer tests | `py -3 -m unittest discover -s scripts/tests -v` | Passed: 12 tests on Windows. | 2026-10-16 |
| Whitespace validation | `git diff --check` | Passed; only Git line-ending conversion warnings were emitted. | 2026-10-16 |
| macOS/Linux runtime | Not available in this environment | Not run; scripts use Python standard library and platform-neutral APIs with Windows VT handling. | 2026-10-16 |
| Empty destination installation | `py -3 scripts/install.py --no-color` into `harness-starter-pack-empty-test`, existing-directory mode; Spring Boot + Angular, Codex, default Graphify skills | Passed: 62 files installed, 0 skipped, 0 issues; tailored `HARNESS-README.md` generated; local README links resolve. | 2026-10-17 |
| Existing Python repository installation | `py -3 scripts/install.py --no-color` into `harness-starter-pack-non-empty-test`; Python + FastAPI, Codex, default Graphify skills | Passed: 52 files installed, 0 skipped, 0 issues; tailored `HARNESS-README.md` generated; existing README, Python sources, requirements, and `.env` remained present; local README links resolve. | 2026-10-17 |
| Installer unit suite | `python -m unittest discover -s scripts/tests -v` | Passed: 12 tests. `py -3 -m unittest ...` could not locate a registered interpreter in this shell; rerunning with the available `python` executable succeeded. | 2026-10-17 |
| Whitespace validation | `git diff --check` | Passed. | 2026-10-17 |

## Review and risks

- Findings resolved: Fixed Windows Unicode output fallback and Windows console VT API declarations; corrected the test to assert Git initialization result rather than captured input prompt. Added back navigation, path validation, selection retention, and a review step that permits returning before writing.
- Open findings / risks: Actual macOS/Linux console behavior has not been exercised on those operating systems.
- Blockers / required input: None.
- Spec amendments and decision references: A-01 records the 2026-10-17 default-selection decision; A-02 records the integrated ASP.NET Core + React profile; A-03 records the additional technology profiles and Spring Boot + Angular bundle; A-04 records the personalized installation overview; A-05 records the required Graphify CLI setup outcome. The installation-specific follow-up is verified on Windows; the latest documentation clarification still needs review.
- Final adversarial review status (one round at end): Complete; no blocking issues found.

## Next action

1. Review the uncommitted follow-up diff; no installation errors were found. Do not commit unless requested.

## Resume checklist

- [x] Read the current spec and this handoff.
- [x] Confirm branch/worktree and working tree before editing.
- [x] Confirm the engineer-reviewed spec, amendment log, and current slice/subitem.
- [x] Verify key claims against current source; do not treat this summary as proof.
- [x] Continue only the next agreed subitem; raise material contract changes and update spec amendment log before acting.
