# Prompts de modelo de ameaças ASP.NET Core

Use como extensão ao [template comum de ameaças](../../../../docs/templates/modelo-de-ameacas.md), não como substituto. Responda somente o aplicável e confira aplicação/configuração de hospedagem reais.

## Limites e componentes

- Quais endpoints, middleware, filtros, handlers, serviços hospedados e integrações participam?
- Onde ficam limites entre transporte HTTP, aplicação/domínio, persistência, filas e serviços externos?
- Quais identidade, esquema de autenticação, política de autorização, escopo de tenant/proprietário e identidade de serviço se aplicam?
- Quais dados atravessam redes públicas, proxies, serviços internos ou processos?

## Perguntas específicas ASP.NET Core

- Usuário autenticado pode acessar dados de outro usuário/tenant/objeto mudando ID/filtro?
- Autorização é imposta no servidor por operação/recurso, inclusive jobs e entradas alternativas?
- Binding, validação, serialização ou erros podem revelar campos sensíveis/aceitar valores inesperados?
- CORS, antiforgery, cookie, token, forwarded headers, HTTPS e proxy correspondem à hospedagem?
- Uploads/downloads, redirects, busca de URL, desserialização ou caminhos cruzam limites?
- Queries EF Core aplicam escopo, limites e tratamento seguro de concorrência/transações?
- Retry, tamanho de requisição, taxa, queries caras ou fan-out permitem esgotar recursos?
- Segredos/dados pessoais estão fora de exemplos, logs, exceções e telemetria?
- Migrações, health/readiness e jobs introduzem acesso privilegiado ou premissas inseguras?

Para cada questão aplicável, descreva cenário concreto e conecte mitigação a testes/configuração. Não presuma segurança de defaults sem conferir configuração efetiva.
