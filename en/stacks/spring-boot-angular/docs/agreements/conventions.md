# Spring Boot + Angular conventions prompts

- Keep Spring Boot and Angular ownership explicit; cross-boundary changes must state their API contract impact.
- Validate server input and authorization even when Angular also validates or hides controls.
- Keep client types and server schemas aligned through a documented manual or generated-client process.
- Test backend behavior at its narrowest useful level and validate at least the affected UI/API seam for cross-stack changes.
- Preserve accessible semantics, keyboard behavior, and visible error/empty/loading states in UI changes.
- Do not duplicate domain logic in the browser when the server is authoritative; client calculations are presentational unless explicitly agreed.
