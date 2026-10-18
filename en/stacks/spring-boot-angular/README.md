# Spring Boot + Angular profile

Use this bundle when a Java/Spring Boot API and Angular client are maintained in one repository and a change can cross their boundary. The installer includes this integrated guidance plus the individual [Spring Boot](../spring-boot/README.md) and [Angular](../angular/README.md) profiles. Guidance only; it does not generate either application or install dependencies.

## Shared decisions

- Define API ownership, versioning/compatibility, request and response schemas, error format, and any generated-client policy.
- Model server-side authentication and authorization as authoritative. Angular route guards improve navigation UX but do not enforce access to backend data.
- Agree how CORS, cookies/tokens, CSRF, TLS, secrets, and environment configuration work across the deployment boundary.
- Keep UI states aligned with API behavior, including validation, empty, loading, error, forbidden, and retry states.
- Select one browser journey runner (for example Playwright) only if useful and supported by repository CI; test critical user flows end to end.

## Candidate quality checks

Use the backend and frontend profile recommendations together: Spring's JUnit/Spring test support and Checkstyle/formatter policy; Angular CLI component tests (current new-project guidance uses Vitest), angular-eslint, and compiler checks. Add API contract and browser journey evidence when a change crosses the boundary. Resolve actual commands from Maven/Gradle, Angular CLI scripts, and CI.

## Templates

- [Integrated architecture prompts](docs/agreements/architecture.md)
- [Cross-stack conventions](docs/agreements/conventions.md)
- [Full-stack specification](docs/templates/spec.md)
- [Full-stack verification plan](docs/templates/verification-plan.md)
- Individual profiles: [Spring Boot](../spring-boot/README.md), [Angular](../angular/README.md)

## References

See the linked official framework and tool sources in the individual profile guides. For web accessibility criteria, see [WCAG 2.2](https://www.w3.org/TR/WCAG22/).
