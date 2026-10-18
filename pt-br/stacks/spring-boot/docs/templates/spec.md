# Especificação Spring Boot: [nome]

Comece pela [spec comum](../../../../docs/templates/spec.md) e acrescente perguntas aplicáveis.

## Contrato de backend

- Rotas API, schemas, status, validação e formato de erros:
- Regras de domínio e responsabilidade de módulos/pacotes:
- Mudanças de persistência, migração e limites transacionais:
- Autenticação, autorização e limites de tenant/dados:
- Configuração, serviços externos, timeout e retry:

## Slices ordenados

Reserve Slice 1 para provar pressupostos de framework, persistência, integração ou segurança que precisem de validação. Caso contrário, explique por que não há prova preliminar. Implemente slices em ordem e conclua cada subitem antes de avançar.