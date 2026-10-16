# React feature specification: [title]

> Status: Draft / Accepted / In progress / Complete · Owner: [name/team] · Date: [date] · Branch: [repository-compliant branch] · Related common spec or exploration: [link]

Before drafting, inspect repository Git guidance and create/switch to the appropriate feature branch. Confirm branch and working-tree state. Use this with the shared [specification template](../../../../docs/templates/spec.md); retain the shared template's change log and common requirements. Keep only stack prompts relevant to the change. Confirm actual React version, rendering framework, router, package scripts, and browser support from the repository. The engineer must review and adjust acceptance criteria before accepting the spec and implementation starts.

## Problem and user outcome

- User need and intended outcome:
- User summary: As a <user/actor>, I want <capability> so that <outcome>.
- Current behavior and source evidence (route, component, test, or screenshot):
- In-scope user journeys and explicit non-goals:
- Supported browsers, devices, viewport sizes, and rendering modes:

## Scope and context

### In scope
-

### Out of scope
-

- Relevant repository architecture and source references:
- Confirmed facts:
- Assumptions / proof needed:
- Constraints and dependencies:

## Acceptance criteria

Use observable user scenarios and identify their evidence. The engineer reviews and adjusts these before accepting the spec.

| ID | Requirement / scenario | Acceptance evidence | Engineer reviewed? |
|---|---|---|---|
| AC-01 | Given … when … then … |  | No |

- [ ] Engineer reviewed and adjusted acceptance criteria.
- [ ] Engineer accepted the spec before implementation begins.

## Interaction and state

- Entry point, route, navigation, and deep-link behavior:
- User actions and expected visible results:
- Loading, empty, success, error, disabled, and retry states:
- Form fields, client-side feedback, server validation, and error association:
- State ownership, persistence, URL state, and reset behavior:
- Keyboard interaction, focus movement/return, and announced status changes:

## Data and integration

- API operations and request/response contracts:
- Authentication context and server-authoritative authorization:
- Data freshness, caching, cancellation, race handling, and optimistic updates:
- Personal/sensitive data displayed, stored, logged, or sent to browser storage:
- Failure and offline behavior:

## Design, accessibility, and security

- Existing design system/components to reuse and responsive behavior:
- Semantic structure, accessible names, labels, instructions, and error messages:
- Keyboard and focus expectations; contrast/zoom/reflow expectations:
- Trust boundaries: browser code and client-side validation are not authoritative:
- XSS/output handling, unsafe URLs/HTML, secrets, and sensitive data exposure:
- Relevant threat model and [quality/security agreement](../../../../docs/agreements/quality-and-security.md):

## Ordered slices

If any assumption could invalidate the plan, make proving it Slice 1. Otherwise Slice 1 is the first delivery slice. Complete every subitem in order and record status/evidence in both this spec and the handoff before advancing.

| Slice / subitem | Description and owned files/contracts | Acceptance evidence | Status | Evidence / note |
|---|---|---|---|---|
| 1.1 | `<proof, or first delivery item>` |  | Not started |  |
| 1.2 | `<next item in this slice, if needed>` |  | Not started |  |
| 2.1 | `<only after every Slice 1 item is complete>` |  | Not started |  |

## Amendments

Stop before implementing a deviation from this accepted plan or applicable engineering agreements. Record its reason and impact, obtain the engineer's decision, update affected slices and evidence, then continue. An explicit developer instruction can be recorded as the decision source.

| ID / date | Deviation and reason | Impact on scope / slices / criteria / evidence | Decision and source | Status |
|---|---|---|---|---|

## Verification and release

- Focused tests/checks and evidence for each subitem before advancing:
- Full test suite, run after all slices are complete:
- Other required full checks from project agreements:
- Manual/browser/device checks and rollout/recovery:
- One final adversarial review against the full spec and final diff (strong model if available, otherwise engineer-run review skill):

## Change log

| Date | Change | Decision owner / source |
|---|---|---|

## Acceptance evidence

- Observable behavior for each important scenario:
- Relevant [verification plan](verification-plan.md):
- Open decisions, assumptions, and owners:
