# Plano de verificação ASP.NET Core: [mudança]

> Spec: [link] · Responsável: [nome/equipe] · Versões .NET/ASP.NET Core: [verificadas]

Use com o [plano comum](../../../../docs/templates/plano-de-verificacao.md). Comandos são exemplos: confirme SDK, solução, fonte de pacotes, infraestrutura de teste e scripts. Não declare sucesso sem execução.

Execute verificações focadas por slice e registre neste plano/handoff antes de avançar. Deixe suíte completa para após todos os slices, salvo requisito aceito. Faça uma revisão adversarial final contra spec e diff.

## Evidência específica da mudança

| Requisito/invariante | Evidência necessária | Resultado/link | Status |
|---|---|---|---|
| Comportamento API e erros | | | Não executado |
| Autorização e escopo de dados/tenant | | | Não executado |
| Invariantes de domínio | | | Não executado |
| Persistência/migração | | | Não executado |

## Build e código

| Verificação | Comando/ponto de entrada candidato | Notas/resultado |
|---|---|---|
| Formatação | dotnet format <solução> --verify-no-changes | Confirme SDK/configuração |
| Build | dotnet build <solução-ou-projeto> | Registre ambiente e warnings/erros |
| Análise estática | Analyzers/regras configurados | Distinga baseline e achados novos |
| Testes unitários | dotnet test <projeto-unitário> | Domínio/aplicação/invariantes |
| Integração | dotnet test <projeto-integração> | Provider/hospedagem real quando relevante; isole dados |
| API/contrato | Comando do projeto | Status, códigos, validação e compatibilidade |

## Dados, segurança e operação

| Preocupação | Evidência | Resultado/link | Status |
|---|---|---|---|
| EF Core, constraints e transações | Testes, SQL/query ou revisão de migração | | Não executado |
| Aplicação/rollback de migração | Revisão e banco descartável/teste | | Não executado |
| Auth, autorização e isolamento | Acesso permitido/negado, inclusive escopo objeto | | Não executado |
| Entrada, erros e limites de recursos | Testes de fronteira/revisão | | Não executado |
| Segredos, configuração, logs e dados pessoais | Revisão; redação/defaults seguros | | Não executado |
| Dependências/vulnerabilidades | Auditoria aprovada, data e escopo | | Não executado |
| Observabilidade/falhas | Logs/métricas/traces e falhas de dependência | | Não executado |

## Release e lacunas

- Verificações exigidas pelo [acordo de qualidade/segurança](../../../../docs/acordos/qualidade-e-seguranca.md):
- Verificações não executadas e motivo:
- Premissas/limitações de ambiente:
- Responsável pela implantação/recuperação:
- Exceção de risco, se houver:

Status permitidos: Aprovado, Falhou, Ignorado, Não executado ou Não aplicável.
