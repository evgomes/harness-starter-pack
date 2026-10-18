# Perfil Spring Boot + Angular

Use este bundle quando API Java/Spring Boot e cliente Angular estiverem no mesmo repositório e uma mudança atravessar seus limites. Inclui orientação integrada e os perfis individuais [Spring Boot](../spring-boot/README.md) e [Angular](../angular/README.md). Copia orientação; não gera apps nem instala dependências.

## Decisões compartilhadas

- Defina responsável pela API, versionamento/compatibilidade, schemas de requisição/resposta, formato de erros e política de client gerado.
- Autenticação/autorização no servidor são autoritativas. Guards Angular ajudam navegação, mas não controlam acesso aos dados do backend.
- Acorde CORS, cookies/tokens, CSRF, TLS, segredos e configuração por ambiente entre as camadas de implantação.
- Alinhe estados de interface ao comportamento da API: validação, vazio, carregamento, erro, proibido e nova tentativa.
- Escolha runner de jornada browser (por exemplo Playwright) somente se útil e suportado pela CI; teste fluxos críticos de ponta a ponta.

## Verificações candidatas

Combine opções dos dois perfis: JUnit/Spring Test e política Checkstyle/formatador; testes Angular CLI (orientação atual de novos projetos usa Vitest), angular-eslint e compilação. Acrescente evidência de contrato API e browser quando cruzar camadas. Derive comandos reais de Maven/Gradle, scripts Angular CLI e CI.

## Templates

- [Prompts integrados de arquitetura](docs/agreements/architecture.md)
- [Convenções entre stacks](docs/agreements/conventions.md)
- [Spec full stack](docs/templates/spec.md)
- [Plano de verificação full stack](docs/templates/verification-plan.md)
- [Perfis individuais](../spring-boot/README.md) e [Angular](../angular/README.md)

Veja fontes oficiais nos perfis individuais e [WCAG 2.2](https://www.w3.org/TR/WCAG22/).