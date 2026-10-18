# Angular profile

Frontend guidance for Angular applications. Verify Angular/CLI versions, workspace layout, rendering mode, package manager, design system, and browser support against the repository. The installer copies guidance only.

## Architecture and conventions

- Follow the Angular style guide and group related code by feature or domain where that helps ownership and navigation.
- Use Angular's dependency injection and established router/forms/http abstractions; avoid custom frameworks around capabilities the project already uses.
- Keep view state and server state intentional. Make loading, empty, error, success, and permission-denied states explicit.
- Keep API contracts aligned with the backend; generated clients are optional and must be checked into the project's workflow deliberately.
- Avoid unsafe DOM APIs and trust-bypass methods. Prefer Angular template bindings and sanitization; configure CSP/Trusted Types in coordination with deployment.
- Treat accessibility as a design and verification concern: semantic HTML, keyboard operation, focus management, labels, and meaningful announcements.

## Candidate quality checks

| Area | Candidate |
|---|---|
| Unit/component tests | Angular CLI `ng test`; current Angular docs describe Vitest + jsdom for new CLI projects, while existing Karma setups remain supported. Check target version/config first. |
| Lint | `angular-eslint` with ESLint; community-maintained and match its compatibility to the Angular/ESLint versions. |
| Type/build | Angular CLI build and TypeScript/compiler diagnostics from project scripts. |
| Browser/E2E | Playwright for real-browser journeys when the repository adopts it; focus on user-visible critical flows. |
| Quality/security | Angular security guidance, dependency review, accessibility checks, and tests for route guards and server-derived authorization states. Client guards are not server authorization. |

These tools are recommendations, not installed dependencies or required policy.

## Templates

See the [template index](docs/templates/README.md). Shared [UI design exploration](../../docs/templates/ui-design-exploration.md), [verification](../../docs/templates/verification-plan.md), and accessibility skill may also apply.

## References

- [Angular style guide](https://angular.dev/style-guide)
- [Angular security best practices](https://angular.dev/best-practices/security)
- [Angular testing](https://angular.dev/guide/testing)
- [angular-eslint](https://github.com/angular-eslint/angular-eslint)
- [Playwright](https://playwright.dev/docs/intro)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
