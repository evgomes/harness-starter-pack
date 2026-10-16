# ASP.NET Core feature specification: [title]

> Status: Draft / Accepted / In progress / Complete · Owner: [name/team] · Date: [date] · Branch: [repository-compliant branch] · Related common spec or exploration: [link]

Before drafting, inspect repository Git guidance and create/switch to the appropriate feature branch. Confirm branch and working-tree state. Use this with the shared [specification template](../../../../docs/templates/spec.md); retain the shared template's change log and common requirements. Keep only stack prompts relevant to the change. Confirm actual framework version, hosting model, packages, and architecture before making decisions. The engineer must review and adjust acceptance criteria before accepting the spec and implementation starts.

## Problem and outcome

- User/business outcome and affected API consumers:
- User summary: As a <user/actor>, I want <capability> so that <outcome>.
- Current behavior and source evidence (endpoint, handler, service, test):
- Intended behavior and compatibility requirements:

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

Use observable scenarios and identify their evidence. The engineer reviews and adjusts these before accepting the spec.

| ID | Requirement / scenario | Acceptance evidence | Engineer reviewed? |
|---|---|---|---|
| AC-01 | Given … when … then … |  | No |

- [ ] Engineer reviewed and adjusted acceptance criteria.
- [ ] Engineer accepted the spec before implementation begins.

## API and application behavior

- Route, HTTP method, request/response contract, and versioning:
- Authentication and authorization policy, including resource/tenant scope:
- Validation rules and error contract (status, stable error code, safe details):
- Idempotency, concurrency, pagination, filtering, and ordering where relevant:
- Cancellation, timeout, retry, and external failure behavior:

## Domain and persistence

- Domain concepts, invariants, identity, null semantics, and ownership:
- Data reads/writes, query bounds, consistency, transaction boundary:
- EF Core mapping, indexes/constraints, and migration plan (if applicable):
- Data compatibility, backfill, rollout, and rollback:
- UTC/timestamp and tenancy strategy:

## Hosting, configuration, and operations

- Service registration / dependency boundary:
- Configuration keys and safe defaults (no secret values):
- Logging fields, redaction, metrics, tracing, health/readiness impacts:
- Resource limits, rate limits, and operational failure modes:

## Security, privacy, and verification

- Trust boundaries, data classification, authorization and abuse scenarios:
- Secret handling, input/output handling, logging and retention:
- Relevant threat model and [quality/security agreement](../../../../docs/agreements/quality-and-security.md):
- Acceptance evidence and [verification plan](verification-plan.md):
- Explicit assumptions, open decisions, and owners:

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
- Manual/environment checks, migration, rollout, and recovery:
- One final adversarial review against the full spec and final diff (strong model if available, otherwise engineer-run review skill):

## Change log

| Date | Change | Decision owner / source |
|---|---|---|
