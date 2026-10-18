# Stack profile catalog

Stack profiles add technology-specific architecture, conventions, and verification guidance to the shared agreements. Treat recommendations as candidates: verify them against the target repository's manifests, source, CI, deployment configuration, and team decisions. Profiles copy guidance only; they do not generate application code or install packages.

## Available profiles

| Profile | Role | Testing and quality starting points |
|---|---|---|
| [ASP.NET Core](aspnet-core/README.md) | .NET backend and HTTP APIs | `dotnet test`, `dotnet format`, build and package audit |
| [React](react/README.md) | Component-based web frontend | Project test runner, TypeScript check when used, ESLint, browser and accessibility checks |
| [ASP.NET Core + React](aspnet-core-react/README.md) | Same-repository full stack | Both profiles plus API contract, browser flow, and end-to-end evidence |
| [Java + Spring Boot](spring-boot/README.md) | Java backend and HTTP APIs | JUnit Jupiter / Spring test support, Checkstyle or project formatter, integration tests |
| [Node.js + Express](node-express/README.md) | Node.js backend and HTTP APIs | `node:test` or Vitest, Supertest-style HTTP tests, ESLint |
| [Python + FastAPI](python-fastapi/README.md) | Python API-first backend | pytest + FastAPI TestClient, Ruff, optional mypy / type checks |
| [Angular](angular/README.md) | Angular frontend | Angular CLI `ng test` (current new-project default uses Vitest), angular-eslint, browser and accessibility checks |
| [Spring Boot + Angular](spring-boot-angular/README.md) | Same-repository full stack | Both profiles plus API contract, browser flow, and end-to-end evidence |

The Spring Boot + Angular bundle includes the individual Spring Boot and Angular profiles plus integrated architecture, conventions, spec, and verification guidance. The ASP.NET Core + React bundle follows the same pattern. Select a bundle when both applications live in one repository; select an individual profile when only that technology needs guidance.

## Choosing a profile

- For a backend, choose one of ASP.NET Core, Spring Boot, Node.js + Express, or Python + FastAPI.
- For a frontend, choose React or Angular.
- For a co-located full-stack repository, choose the matching combined profile. Bundle-specific docs address API/UI contracts, trust boundaries, and end-to-end verification.
- Select more than one individual profile when that better represents a repository; a combined profile is a convenience with integrated guidance, not a requirement.
- Python + FastAPI is the profile currently provided. Django REST Framework can be a suitable alternative when a project specifically benefits from Django's ecosystem, but it does not have a separate starter profile yet.

Testing, security, and quality guidance is not a claim that a particular tool is mandatory or sufficient. Follow the target project's quality/security agreement and use authoritative documentation for the selected tool and version.

## Adding a profile

1. Create `stacks/<stack-name>/README.md` with scope, supported variants, prerequisites, and candidate test, lint, build, and security checks.
2. Add only the architecture and convention extensions that differ from the common agreements.
3. Document lint, build, test, security, and accessibility commands as candidates and tie each to evidence/configuration; do not invent version pins.
4. Add focused skills only when a repeatable stack-specific workflow benefits from them.
5. Update this catalog and the root English README. Keep language-specific content inside its language package.
