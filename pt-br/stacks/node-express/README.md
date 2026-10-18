# Perfil Node.js + Express

Orientações de backend para serviços Node.js com Express. Confira sistema de módulos, política de runtime Node, versão principal do Express, gerenciador de pacotes, TypeScript e topologia de implantação. O perfil copia somente orientação.

## Arquitetura e convenções

- Separe composição de rotas, validação de requisição, regras de aplicação/domínio e persistência quando isso esclarecer responsabilidade e testes.
- Use I/O assíncrono e encaminhe promises rejeitadas/erros a handler centralizado. Não bloqueie event loop com trabalho pesado de CPU.
- Valide entradas não confiáveis no limite, use operações parametrizadas no banco e não exponha erros/segredos brutos em respostas/logs.
- Defina limites de tamanho, timeout, taxa/recursos, CORS, confiança em proxy, cookies/sessão e TLS no limite apropriado.
- Aplique autorização por ação/recurso; autenticar a rota não basta para autorizar o objeto.

## Verificações candidatas

| Área | Opção |
|---|---|
| Testes unitários | node:test nativo para poucas dependências ou Vitest para tooling JS/TS compartilhado. |
| HTTP/API | Supertest ou client já usado para rotas, middleware, validação e erros. |
| Lint/formatação | ESLint; typescript-eslint se TypeScript estiver presente. Siga política atual. |
| Runtime | Runner de testes, typecheck TS, smoke test de build/start e desempenho do event loop quando relevante. |
| Segurança/dependências | Auditoria de pacotes, lockfile, secrets scan, testes de entrada/autorização, Helmet quando adequado e cookies/sessão seguros. |

Ferramentas são opcionais: confira scripts e compatibilidade antes de adotar comandos/middleware. Helmet ajuda com headers, mas não protege toda aplicação.

## Templates e referências

Veja [templates](docs/templates/README.md) para specs de API/verificação e o [modelo comum de ameaças](../../docs/templates/threat-model.md).

- [Segurança em produção Express](https://expressjs.com/en/advanced/best-practice-security/)
- [Desempenho/confiabilidade Express](https://expressjs.com/en/advanced/best-practice-performance/)
- [Não bloqueie o event loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop)
- [Runner Node.js](https://nodejs.org/api/test.html)
- [ESLint](https://eslint.org/docs/latest/use/getting-started), [typescript-eslint](https://typescript-eslint.io/getting-started/), [Vitest](https://vitest.dev/guide/) e [Supertest](https://github.com/ladjs/supertest)