# Full-stack feature specification: <title>

> Status: Draft | Accepted | In progress | Complete
> Owner: <name/team> · Date: <YYYY-MM-DD> · Branch: <repository-compliant branch> · Related exploration/handoff: <links>

Use this template for work that changes a user flow across a React UI and ASP.NET Core API. Inspect the repository's shared instructions and agreements first. Verify the actual runtime, API, UI, persistence, and deployment conventions before accepting the design.

## 1. Problem and outcome

- User need and intended outcome:
- User-visible flow(s):
- Why now:

## 2. Scope and context

### In scope
-

### Out of scope
-

- Existing UI/API behavior and evidence:
- Relevant architecture and conventions:
- Dependencies, constraints, and assumptions to prove:

## 3. Requirements and acceptance criteria

| ID | User scenario / requirement | Acceptance evidence |
|---|---|---|
| AC-01 | Given … when … then … | `<server, UI, contract, or manual evidence>` |

Include loading, empty, success, validation, authorization, and failure states that apply to the flow.

## 4. Cross-stack design

- React route, components, state ownership, and accessibility behavior:
- API endpoints, request/response contracts, validation, and error mapping:
- Domain rules, persistence, authorization, and data ownership:
- Authentication, privacy, logging/redaction, and trust boundaries:
- Compatibility, deployment order, and rollback considerations:
- Alternatives and accepted decisions, with owner/source:

## 5. Proofs and implementation slices

If any assumption must be proved before the rest of the plan can be trusted, Slice 1 is for those proofs. Otherwise, Slice 1 is the first delivery slice. Resolve slices sequentially and resolve each slice's subitems in order; do not start a later slice until all current subitems have evidence.

| Slice / subitem | Vertical behavior and owned contracts | Acceptance evidence | Status | Evidence / note |
|---|---|---|---|---|
| 1.1 | `<proof, or first end-to-end delivery item>` | | Not started | |
| 1.2 | `<next ordered subitem>` | | Not started | |
| 2.1 | `<begin after Slice 1 is complete>` | | Not started | |

## 6. Verification and release

- Focused backend tests/checks for each slice:
- Focused frontend tests/checks for each slice:
- API contract/integration and browser/end-to-end evidence:
- Accessibility, security, privacy, and operational checks:
- Full required checks after all slices are complete:
- One final review against the accepted spec and final diff:

## 7. Risks, amendments, and change log

| Risk or amendment | Impact / mitigation | Owner / decision source | Status |
|---|---|---|---|
| | | | |

| Date | Change | Decision owner/source |
|---|---|---|
