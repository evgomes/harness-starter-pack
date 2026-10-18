# Node.js + Express profile

Backend guidance for Node.js services using Express. Verify module system, Node runtime support policy, Express major version, package manager, TypeScript use, and deployment topology against the actual repository. This profile copies guidance only.

## Architecture and conventions

- Separate route composition, request validation, application/domain behavior, and persistence where those boundaries clarify ownership and tests.
- Use asynchronous I/O and ensure rejected promises/errors reach a centralized error handler. Do not let CPU-heavy work block the event loop.
- Validate untrusted input at the boundary, use parameterized database operations, and avoid reflecting raw errors or secrets in responses/logs.
- Define request size limits, timeouts, rate/resource limits, CORS, proxy trust, cookie/session settings, and TLS at the appropriate deployment boundary.
- Apply authorization per action/resource; do not treat route authentication as sufficient object-level authorization.

## Candidate quality checks

| Area | Candidate |
|---|---|
| Unit tests | Built-in `node:test` for a minimal dependency footprint, or Vitest where shared JS/TS tooling is desired. |
| HTTP/API tests | Supertest or the project's HTTP test client for routes, middleware, validation, and error behavior. |
| Lint/format | ESLint; add typescript-eslint if TypeScript is present. Keep formatting policy consistent with the repository. |
| Runtime checks | Node's test runner, compiler/typecheck for TypeScript, build/start smoke checks, and event-loop/performance checks for relevant workloads. |
| Security/dependencies | Package audit/advisory review, lockfile integrity, secrets scanning, input/authorization tests, Helmet headers as appropriate, and secure cookie/session configuration. |

No tool is mandatory: check the project's package scripts and Node/Express compatibility before adopting commands or middleware. Helmet helps set security headers but does not secure the whole application.

## Templates

See the [template index](docs/templates/README.md) for API specs and verification prompts. Use the common [threat model](../../docs/templates/threat-model.md) when a change affects trust boundaries.

## References

- [Express production security](https://expressjs.com/en/advanced/best-practice-security/)
- [Express performance and reliability](https://expressjs.com/en/advanced/best-practice-performance/)
- [Node.js: don't block the event loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop)
- [Node.js test runner](https://nodejs.org/api/test.html)
- [ESLint getting started](https://eslint.org/docs/latest/use/getting-started)
- [typescript-eslint getting started](https://typescript-eslint.io/getting-started/)
- [Vitest guide](https://vitest.dev/guide/)
- [Supertest](https://github.com/ladjs/supertest)
