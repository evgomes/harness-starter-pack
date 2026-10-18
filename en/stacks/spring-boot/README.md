# Java + Spring Boot profile

Backend guidance for Java services built with Spring Boot. Treat the choices below as candidates: confirm the repository's Java/Spring versions, Maven or Gradle setup, CI, and deployment model first. The installer copies guidance only.

## Architecture and conventions

- Keep the application entry point in a root package above application components, so component scanning has a clear boundary. Group code by domain/feature when that matches the system; avoid prescribing a fixed layer count.
- Prefer constructor injection and explicit dependencies. Keep HTTP/controller concerns separate from business rules and persistence where those seams improve testability.
- Use Spring configuration and externalized configuration for environment-specific values; keep secrets in the deployment's secret store.
- Consider Spring Modulith only when explicit application-module boundaries solve a real modularity problem; it is not required for every service.
- Use Spring validation and security mechanisms at trust boundaries; define authorization at the resource/action level and verify it in tests.

## Candidate quality checks

| Area | Candidate |
|---|---|
| Unit and slice tests | JUnit Jupiter, AssertJ and Spring Boot test support via the project's `spring-boot-starter-test`; prefer focused test slices when a full context is unnecessary. |
| HTTP/API and integration tests | Spring MVC/WebFlux test support; optionally Testcontainers when integration behavior depends on a real database, broker, or service. |
| Formatting/lint | Checkstyle for agreed Java style rules; optionally Spotless if the project wants a formatter/linter integration. Follow existing Maven/Gradle plugins and formatting policy. |
| Static and dependency checks | Compiler warnings, project-selected static analysis, dependency vulnerability and license review; use the common quality/security agreement. |
| Runtime/operations | Spring Boot Actuator endpoints only as needed, with exposure and authorization configured for deployment. |

Testing tools are candidates, not a mandated stack. Derive commands from Maven/Gradle wrapper scripts and CI. Do not expose health or management endpoints publicly by default.

## Templates

See [template index](docs/templates/README.md) for a Java/Spring API spec outline and verification plan. Use shared [security](../../docs/templates/threat-model.md) and [verification](../../docs/templates/verification-plan.md) templates when they fit better.

## References

- [Spring Boot testing](https://docs.spring.io/spring-boot/reference/testing/)
- [Structuring your code](https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html)
- [Externalized configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html)
- [Spring Boot Actuator](https://docs.spring.io/spring-boot/reference/actuator/index.html)
- [Spring Modulith](https://docs.spring.io/spring-modulith/reference/)
- [Checkstyle](https://checkstyle.org/)
- [Testcontainers for Java](https://java.testcontainers.org/)
