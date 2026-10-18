# Express API feature specification: [name]

Start with the common [spec template](../../../../docs/templates/spec.md) and add relevant details.

## API and trust boundaries

- Routes/methods, input/output schema, status/error behavior:
- Middleware order and request validation:
- Authentication, action/resource authorization, abuse/rate limits:
- Data ownership, parameterized persistence, transaction boundaries:
- Async work, external calls, timeout/retry and event-loop impact:
- Logging, redaction, and operational configuration:

## Ordered slices

Use slice 1 for proof work when an unverified runtime, library, integration, or security assumption needs validation. Otherwise record why no proof slice is needed. Resolve later slices sequentially, subitem by subitem.
