# Python + FastAPI profile

API-first backend guidance for Python services using FastAPI. Verify the Python support range, ASGI server, dependency manager, database, and deployment configuration against the project. The installer copies guidance only.

## Architecture and conventions

- For larger services, group related endpoints in `APIRouter` modules and compose them explicitly. Keep route transport concerns separate from domain rules where useful.
- Use FastAPI dependency injection for shared resources, authentication/authorization, and request-scoped services; prefer typed `Annotated` declarations where compatible with the project's Python range.
- Define and validate request/response schemas; avoid returning persistence objects or sensitive fields by accident.
- Make async/sync boundaries intentional. Use async handlers for async I/O, and avoid blocking the event loop with synchronous CPU or I/O work.
- Treat generated OpenAPI as a contract to review; document auth/error semantics and test authorization at object and action boundaries.

## Candidate quality checks

| Area | Candidate |
|---|---|
| Unit/API tests | pytest with FastAPI `TestClient` (HTTPX-backed); async test support for genuinely async behavior. |
| Lint and formatting | Ruff for linting and formatting. Configure rules to match project policy rather than enabling every rule blindly. |
| Type checks | mypy or another project-selected checker when typing checks are in scope; FastAPI annotations alone do not prove all runtime/type behavior. |
| Integration/security | Database-backed integration tests where needed, dependency/advisory audits, secret scanning, auth/permission/input tests, and resource-limit review. |

FastAPI is the profile implemented here. Django REST Framework can be an alternative when a project benefits from Django's ORM/admin and ecosystem; it needs its own profile and project-specific decisions.

## Templates

See the [template index](docs/templates/README.md) for API specification and verification prompts. Use the common [threat model](../../docs/templates/threat-model.md) for security-sensitive boundaries.

## References

- [FastAPI bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [FastAPI security](https://fastapi.tiangolo.com/tutorial/security/)
- [FastAPI deployment concepts](https://fastapi.tiangolo.com/deployment/concepts/)
- [Ruff](https://docs.astral.sh/ruff/)
- [mypy](https://mypy.readthedocs.io/en/stable/)
