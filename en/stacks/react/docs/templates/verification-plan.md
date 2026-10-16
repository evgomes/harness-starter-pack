# React verification plan: [change]

> Related specification: [link] · Owner: [name/team] · React / framework version: [verified versions]

Use with the common [verification-plan template](../../../../docs/templates/verification-plan.md). Derive commands from the repository's package scripts and lockfile; do not assume npm, a particular bundler, test framework, or install tools just to follow this template.

Run focused checks for each active slice and record results in both this plan and the handoff before advancing. Defer the full test suite until all spec slices are complete unless the accepted spec or project agreement requires an earlier full run. Run one adversarial review at the end against the whole spec and final diff, using a strong model if available or having the engineer run the review skill manually.

## Change-specific evidence

| Requirement / user scenario | Evidence required | Result / link | Status |
| --- | --- | --- | --- |
| Primary user flow |  |  | Not run |
| Loading, empty, error, and retry states |  |  | Not run |
| API contract and server validation response |  |  | Not run |
| Keyboard and assistive technology behavior |  |  | Not run |

## Build and code checks

| Check | Candidate command or project entry point | Notes / result |
| --- | --- | --- |
| Formatting | Existing formatter script, scoped where supported | Use repository configuration. |
| Lint / static analysis | Existing lint script | Record new findings separately from accepted baseline. |
| Type validation | Existing typecheck script when TypeScript is used | Do not infer type safety from editor diagnostics alone. |
| Production build | Existing build script | Record required environment and warnings/errors. |
| Unit / component tests | Existing focused test script | Cover state transitions, validation, and behavior rather than implementation details. |
| Integration / browser tests | Existing integration or end-to-end command | Verify routing, API interaction, and relevant browser behavior. |

## Accessibility and security

| Concern | Evidence to collect | Result / link | Status |
| --- | --- | --- | --- |
| Semantic elements, accessible names, labels, and error associations | DOM/test inspection and applicable automated checks |  | Not run |
| Keyboard operation, focus order/visibility, and focus management | Manual keyboard walkthrough and focused tests |  | Not run |
| Zoom/reflow, contrast, and responsive layouts | Manual/browser evidence at project target conditions |  | Not run |
| Dynamic status, loading, and error announcements | Assistive technology behavior or suitable automated/manual evidence |  | Not run |
| Server-side authorization assumptions | Confirm API enforcement; client route guards are not security controls |  | Not run |
| XSS, unsafe HTML/URLs, and sensitive browser data | Focused review and tests for applicable flows |  | Not run |
| Dependency and source-security checks | Project-approved command/source; record date and scope |  | Not run |

Automated accessibility checks catch only some issues. Record manual evidence for interaction and assistive technology behavior where the project's accessibility target requires it.

## Release and gaps

- Required checks from the project's [quality and security agreement](../../../../docs/agreements/quality-and-security.md):
- Checks not run, with reason:
- Browser/device coverage and limitations:
- Risk exception link, if applicable:

Allowed status values: `Passed`, `Failed`, `Skipped`, `Not run`, or `Not applicable`.
