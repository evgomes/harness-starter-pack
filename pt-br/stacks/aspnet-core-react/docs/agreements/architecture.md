# Prompts de arquitetura ASP.NET Core + React

Confira cada prompt no repositório. Registre decisões aceitas no acordo comum docs/agreements/architecture.md.

## Limites do sistema e responsabilidades

- Identifique host ASP.NET Core, transporte API, lógica de domínio/aplicação, persistência, serviços externos e entradas React.
- Declare quem é responsável por cada invariante/decisão. Servidor é autoritativo para autorização, validação e estado persistido; controles no browser melhoram UX, mas não segurança.
- Documente unidades/ambientes de implantação, origens, roteamento/proxy e acesso da UI à API em desenvolvimento/produção.

## Contrato API/interface

- Registre base path/versionamento, autenticação, responsabilidade por DTOs, serialização, paginação e compatibilidade.
- Defina erros estáveis e identificadores de máquina quando UI tratar falhas; explique mapeamento de validação para campos/mensagens.
- Especifique estados de carregamento, vazio, sucesso, parcial e erro nos fluxos importantes, incluindo retry/cancelamento.
- Documente geração de clients/schemas compartilhados, se houver. Não compartilhe entidades de domínio do servidor diretamente com browser por padrão.

## Dados e limites de confiança

- Trace identidade/autorização da requisição até política e escopo de dados no servidor. Identifique CSRF, CORS, cookies/tokens e redirects conforme autenticação.
- Declare dados permitidos no browser, exclusão de segredos e redação de logs em ambos lados.
- Registre responsabilidade por timestamps, IDs, tenancy, concorrência e validação. Servidor persiste estado canônico; cache/otimização cliente deve reconciliar respostas.

## Impacto entre stacks

- Para mudança que altera API e UI, descreva ordem de implantação/compatibilidade, inclusive compatibilidade temporária entre versões.
- Identifique evidências de contrato, integração e ponta a ponta além de testes unitários/componentes.
- Registre observabilidade da fronteira: IDs de correlação, campos estruturados sem dados sensíveis e como relacionar falha no browser a logs do servidor.