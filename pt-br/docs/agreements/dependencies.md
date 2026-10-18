# Acordo de dependências

> Status: template inicial. Mantenha o inventário atualizado; não afirme licença ou situação de segurança sem verificar a fonte.

## Política

- Registre pacotes diretos e transitivos relevantes de runtime/desenvolvimento, versões resolvidas, finalidade e licença.
- Antes de adicionar/atualizar, verifique saúde, licença, vulnerabilidades conhecidas, caminho de atualização e impacto transitivo.
- Não presuma que um identificador SPDX comprova conformidade; confira a licença publicada, exceções e licenciamento duplo.
- Não faça commit de auditorias com credenciais, URLs de registries privados ou dados ambientais desnecessários.
- Registre data da auditoria, ferramentas/fontes, riscos pendentes, responsável e próxima revisão.

## Inventário

| Ecossistema | Pacote | Versão resolvida | Direto/transitivo | Licença (fonte) | Finalidade | Responsável / observações |
|---|---|---|---|---|---|---|
| <NuGet/npm/etc.> | <pacote> | <versão> | <direto ou transitivo> | <SPDX / URL> | <finalidade> | <observações> |

## Registro de vulnerabilidades e atualizações

| Data | Pacote/aviso | Severidade e intervalo afetado | Decisão/mitigação | Evidência / issue | Responsável |
|---|---|---|---|---|---|
| <data> | <item> | <intervalo verificado> | <atualização, mitigação ou risco aceito com justificativa> | <link ou arquivo> | <responsável> |

## Ferramentas

| Ferramenta | Versão | Finalidade / fonte de instalação | Última verificação |
|---|---|---|---|
| <Graphify, scanner, formatador etc.> | <versão> | <finalidade e fonte de instalação> | <data> |

## Periodicidade de revisão

- Pull request: audite mudanças de dependências e atualize este arquivo na mesma alteração.
- Periódica: execute verificações de dependências/licenças a cada <periodicidade> usando <job de CI, automação agendada ou responsável>.
- Ao receber um aviso: avalie alcance, versões afetadas, explorabilidade, correções e impacto no negócio; registre risco aceito com responsável e data de revisão.

Uma skill pode orientar a revisão, mas não a executa periodicamente sem agente ou job agendado. Prefira CI ou automação agendada para relatórios recorrentes.

## Fontes adicionais

| Ferramenta/fonte | Versão ou URL | O que verifica | Último uso |
|---|---|---|---|
| <registro / scanner / fonte oficial de avisos> | <versão/link> | <escopo> | <data> |