# Perfil de arquitetura ASP.NET Core

Confira este perfil no projeto antes de adotar. Registre versões reais de framework/runtime e arquitetura em docs/acordos/arquitetura.md.

## Responsabilidades e limites

Documente host API, transporte/endpoints, regras de aplicação/domínio, persistência, integrações externas, serviços de segundo plano e raiz de composição. Declare a responsabilidade de cada camada e direções de dependência permitidas.

### Minimal APIs e agrupamento de recursos

Se usar Minimal APIs, agrupe rotas por recurso em módulos legíveis. Cada handler valida limites, chama comportamento de aplicação/domínio e mapeia resultado para resposta de transporte. Regras de negócio ficam em tipos testáveis sem HTTP.

### Limite de persistência

EF Core controla acesso e mapeamento do banco. Mantenha expressões de consulta na camada de dados; não deixe IQueryable chegar ao domínio/apresentação. Explicite propriedade de migrações, transações e constraints. Trate migrações como código revisado; crie migração nova em vez de reescrever uma já aplicada.

## Contratos de dados/domínio

- Documente tipos de domínio na linguagem do produto. Explique significado, invariantes, mutabilidade e semântica de nulos quando não estiverem claros pelo tipo/nome.
- Evite sentinelas e literais sem explicação que codifiquem estado. Use tipo nomeado, enum ou constante quando tornar regra explícita.
- Decida identidade, responsabilidade por timestamp, serialização UTC, tenant/propriedade e escopo de unicidade junto ao modelo de dados.
- Defina validação, compatibilidade, formato de erro e identificadores estáveis de erro nas fronteiras API.

## Consultas e desempenho

Projete leituras para os dados necessários ao caso de uso. Evite N+1, materialização sem limite e tracking em consultas somente leitura quando o padrão EF Core permitir. Registre paginação/limites de listas que possam crescer.

## Segurança e operação

Documente autenticação/autorização, escopo de dados/tenant, segredos, origens permitidas, limites de requisição, logs/redação, health/readiness e observabilidade. Para identidade/tenant persistidos, defina unicidade e isolamento de leitura/escrita antes de implementar.

## Evidências e exceções

Use solução/projetos, mapas de API, registro de serviços, modelo EF, migrações, testes, configuração e implantação reais como evidência. Mantenha exceções estreitas e explique trade-offs nos acordos ou registro de decisão.
