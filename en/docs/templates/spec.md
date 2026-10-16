# Feature specification: <title>

> Status: Draft | Accepted | In progress | Complete
> Owner: <name/team> · Date: <YYYY-MM-DD> · Branch: <repository-compliant branch> · Related exploration/handoff: <links>

Before drafting, inspect repository instructions and create or switch to the feature branch required by its Git conventions. Confirm branch and working-tree state. The engineer must review and adjust the acceptance criteria before accepting this spec and starting implementation.

## 1. Problem and outcome

- Problem / user need:
- User summary: As a <user/actor>, I want <capability> so that <outcome>.
- Intended outcome:
- Why now:

## 2. Scope

### In scope
-

### Out of scope
-

## 3. Context and constraints

- Relevant existing behavior and architecture:
- Source references (path/line, issue, or decision):
- Dependencies and constraints:
- Confirmed facts:
- Assumptions to prove:

## 4. Requirements and acceptance criteria

| ID | Requirement / scenario | Acceptance evidence |
|---|---|---|
| AC-01 | Given … when … then … | `<test, inspection, or manual check>` |

## 5. Design and decisions

- Proposed design and boundaries:
- Alternatives considered and tradeoffs:
- Accepted decisions and decision owner:
- Open questions / blockers:
- Data model, invariants, null semantics, and migration/rollback (if applicable):
- API/UI compatibility and error behavior (if applicable):

## 6. Security, privacy, accessibility, operations

- Threats, authorization, input validation, secrets, logging/redaction:
- Personal data and retention/consent considerations:
- Accessibility requirements and manual checks:
- Observability, failure modes, performance, rollout/recovery:
- Not applicable items and reason:

## 7. Proofs and implementation slices

If any assumption must be proved before the rest of the plan can be trusted, make that proof Slice 1. Otherwise Slice 1 is the first delivery slice. Slices and their subitems are strictly sequential: do not begin a later slice until all current subitems are complete with evidence. Update each status and the handoff immediately after completing an item.

| Slice / subitem | Description and owned files/contracts | Acceptance evidence | Status | Evidence / note |
|---|---|---|---|---|
| 1.1 | `<proof, or first delivery item>` | | Not started | |
| 1.2 | `<next item in this slice, if needed>` | | Not started | |
| 2.1 | `<only begin after all Slice 1 items are complete>` | | Not started | |

## 8. Risks and dependencies

| Risk/dependency | Likelihood/impact | Mitigation or decision needed | Owner |
|---|---|---|---|

## 9. Verification and release

- Focused tests and checks for each slice/subitem (record results before moving on):
- Full test suite to run once after all spec slices are implemented:
- Other required full checks before delivery, per project agreements:
- Manual checks / environments:
- Data migration and rollout/rollback:
- One adversarial review at the end against the full spec and final diff; use a strong model when available, otherwise have the engineer run the review skill manually:

## 10. Amendments

Do not silently change the accepted plan. Before implementing a deviation, record it here and obtain the engineer's decision. If accepted, update affected scope, acceptance criteria, slice ordering, and verification evidence before proceeding. Authorized developer instructions can be recorded as the decision source.

| ID / date | Proposed deviation and reason | Impact on scope / slices / acceptance / evidence | Decision and source | Status |
|---|---|---|---|---|

## 11. Acceptance criteria review

- [ ] Engineer reviewed and adjusted acceptance criteria.
- [ ] Acceptance criteria are observable and have evidence plans.
- [ ] Engineer accepted the spec before implementation began.

## 12. Change log

| Date | Change | Decision owner/source |
|---|---|---|
