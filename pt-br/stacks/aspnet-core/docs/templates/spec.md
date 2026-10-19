# Especificação de funcionalidade ASP.NET Core: [título]

> Status: Rascunho / Aceita / Em andamento / Concluída · Responsável: [nome/equipe] · Data: [data] · Branch: [conforme repositório] · Spec comum/exploração relacionada: [link]

Antes de redigir, confira regras Git e crie/troque para branch apropriada. Use junto ao [template de spec comum](../../../../docs/templates/spec.md), mantendo registro de alterações e requisitos comuns. Confirme versões, hospedagem, pacotes e arquitetura reais. A pessoa responsável revisa critérios antes de aceitar/iniciar.

## Problema e resultado

- Resultado para usuário/negócio e consumidores API:
- Resumo: Como <usuário/ator>, quero <capacidade> para <resultado>.
- Comportamento atual e evidências (endpoint, handler, serviço, teste):
- Comportamento pretendido e compatibilidade:

## Escopo e contexto

### Dentro do escopo
-

### Fora do escopo
-

- Arquitetura/referências:
- Fatos confirmados:
- Premissas/provas necessárias:
- Restrições e dependências:

## Critérios de aceitação

| ID | Requisito/cenário | Evidência | Revisado pela pessoa responsável? |
|---|---|---|---|
| AC-01 | Dado … quando … então … | | Não |

- [ ] Critérios revisados e ajustados.
- [ ] Spec aceita antes da implementação.

## API e comportamento da aplicação

- Rota, método HTTP, contrato e versionamento:
- Autenticação/autorização, inclusive escopo de recurso/tenant:
- Validação e contrato de erro (status, código estável, detalhes seguros):
- Idempotência, concorrência, paginação e ordenação:
- Cancelamento, timeout, retry e falhas externas:

## Domínio e persistência

- Conceitos, invariantes, identidade, nulos e propriedade:
- Leituras/escritas, limites de consulta, consistência e transação:
- Mapeamento/índices/constraints EF Core e migração:
- Compatibilidade, backfill, implantação e rollback:
- Estratégia de UTC e tenancy:

## Hospedagem, configuração e operação

- Registro de serviços/limites de dependência:
- Chaves de configuração e defaults seguros (sem segredo):
- Logs/redação, métricas, tracing e health/readiness:
- Limites de recurso/taxa e falhas operacionais:

## Segurança, privacidade e verificação

- Limites de confiança, classificação de dados, autorização e abuso:
- Segredos, entrada/saída, logs e retenção:
- Modelo de ameaças e acordo de qualidade/segurança:
- Evidência e plano de verificação:
- Premissas, decisões pendentes e responsáveis:

## Slices ordenados

Se premissa puder invalidar o plano, Slice 1 é para comprová-la; senão, Slice 1 é primeira entrega. Conclua cada subitem e registre status/evidências na spec e handoff antes de avançar.

| Slice/subitem | Descrição e arquivos/contratos | Evidência de aceitação | Status | Evidência/nota |
|---|---|---|---|---|
| 1.1 | <prova ou primeira entrega> | | Não iniciado | |
| 1.2 | <próximo item, se necessário> | | Não iniciado | |
| 2.1 | <somente após completar Slice 1> | | Não iniciado | |

## Aditivos

Antes de desviar do plano/acordos aceitos, registre motivo/impacto, obtenha decisão, atualize slices/evidências e prossiga. Instrução explícita do desenvolvedor pode ser fonte da decisão.

| ID/data | Desvio e motivo | Impacto | Decisão/fonte | Status |
|---|---|---|---|---|

## Verificação e release

- Testes/verificações focados por subitem:
- Suíte completa após todos os slices:
- Outras verificações exigidas:
- Ambiente/manual, migração, implantação e recuperação:
- Uma revisão adversarial final contra spec e diff (modelo forte ou skill manual):

## Registro de alterações

| Data | Mudança | Responsável/fonte |
|---|---|---|
