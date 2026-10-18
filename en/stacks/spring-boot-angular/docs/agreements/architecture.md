# Spring Boot + Angular architecture prompts

Record verified project decisions in the common architecture agreement. Use these prompts only where the API and UI share a repository.

- Which application owns each business rule and datum? Keep authorization and validation that protect data on the server.
- What API schema, versioning/compatibility, error format, and client generation policy connect Angular to Spring Boot?
- How are deployment environments, origins/CORS, TLS, cookies/tokens, CSRF, secrets, and service URLs configured?
- How does the UI represent server validation, auth expiry, permission denial, empty/loading/error states, and retries?
- Which tests provide API integration and browser end-to-end evidence, and where do these run in CI?
- Which backend/frontend changes must be deployed together, and what compatibility window is required?
