# Catálogo de perfis de stack

Perfis acrescentam orientações de arquitetura, convenções e verificação específicas de tecnologia aos acordos comuns. Trate recomendações como candidatas: confira manifests, código, CI, implantação e decisões da equipe. Perfis copiam orientação, não geram aplicação nem instalam pacotes.

## Perfis disponíveis

| Perfil | Papel | Ponto de partida para testes/qualidade |
|---|---|---|
| [ASP.NET Core](aspnet-core/README.md) | Backend .NET e APIs HTTP | dotnet test, dotnet format, build e auditoria de pacotes |
| [React](react/README.md) | Frontend web baseado em componentes | Runner do projeto, TypeScript se usado, ESLint, browser e acessibilidade |
| [ASP.NET Core + React](aspnet-core-react/README.md) | Full stack no mesmo repositório | Ambos perfis, contrato de API, fluxo no browser e evidência ponta a ponta |
| [Java + Spring Boot](spring-boot/README.md) | Backend Java e APIs HTTP | JUnit Jupiter/Spring Test, Checkstyle ou formatador e testes de integração |
| [Node.js + Express](node-express/README.md) | Backend Node.js e APIs HTTP | node:test ou Vitest, testes HTTP e ESLint |
| [Python + FastAPI](python-fastapi/README.md) | Backend Python para APIs | pytest + TestClient, Ruff e mypy opcional |
| [Angular](angular/README.md) | Frontend Angular | ng test, angular-eslint, browser e acessibilidade |
| [Spring Boot + Angular](spring-boot-angular/README.md) | Full stack no mesmo repositório | Ambos perfis, contrato de API, fluxo no browser e ponta a ponta |

O bundle Spring Boot + Angular inclui perfis individuais e orientação integrada de arquitetura, convenções, spec e verificação. ASP.NET Core + React segue o mesmo padrão. Escolha bundle quando as duas aplicações estiverem no mesmo repositório; perfil individual quando só uma tecnologia precisar de orientação.

## Como escolher

- Backend: ASP.NET Core, Spring Boot, Node.js + Express ou Python + FastAPI.
- Frontend: React ou Angular.
- Repositório full stack co-localizado: escolha o bundle correspondente. Os documentos integrados cobrem contratos API/interface, limites de confiança e verificação ponta a ponta.
- Se melhor representar o repositório, selecione mais de um perfil individual; bundle é conveniência, não requisito.
- O perfil Python disponível é FastAPI. Django REST Framework pode servir a projetos que aproveitem ecossistema Django, mas ainda não tem perfil próprio.

Orientações de teste, segurança e qualidade não tornam ferramentas obrigatórias nem suficientes. Siga o acordo do projeto e documentação oficial da ferramenta/versão escolhida.

## Adicionar perfil

1. Crie stacks/<nome>/README.md com escopo, variantes, pré-requisitos e opções de teste, lint, build e segurança.
2. Acrescente somente extensões de arquitetura/convenções que difiram dos acordos comuns.
3. Documente comandos candidatos com evidência/configuração; não invente versões fixas.
4. Adicione skill específica somente quando houver fluxo repetível que se beneficie.
5. Atualize o catálogo e README raiz. Mantenha conteúdo no pacote de idioma correspondente.
