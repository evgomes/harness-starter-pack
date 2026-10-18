# Acordo de qualidade e segurança

Este acordo define como tornar verificações de qualidade e segurança repetíveis. Não determina scanner, provedor de CI, framework de hooks ou limite numérico. Registre ferramentas, comandos, limites e responsáveis escolhidos aqui ou na configuração pertinente.

## Princípios

- Valide comportamento com testes e evidências observáveis. Um relatório limpo não prova que o sistema é seguro ou correto.
- Prefira verificações determinísticas, explicáveis e acionáveis. Mantenha feedback rápido perto da mudança e faça verificações amplas em CI ou fluxos agendados.
- Em sistemas legados, diferencie achados novos da dívida existente e acompanhe a linha de base para evitar regressões ocultas.
- Use SOLID e Clean Code como perguntas de design e revisão, conforme o contexto, não como pontuação mecânica.
- Não imponha cobertura ou complexidade universal. Defina limites adequados, explique exceções e impeça a piora da linha de base.
- Trate saídas de ferramentas e revisões humanas/de modelo como fontes de evidência distintas. Confirme achados relevantes no código, configuração e requisitos.
- Mantenha hooks locais rápidos e úteis. CI ou outro processo protegido/auditável é a barreira autoritativa; hooks locais podem ser ignorados ou indisponíveis.
- Não alegue conformidade/certificação a partir de um subconjunto de verificações. Se útil, selecione requisitos versionados de estruturas como OWASP ASVS.

## Catálogo de validação do projeto

Para cada linha aplicável, registre comando real ou ponto de entrada estável, acionamento, política de bloqueio, responsável e local das evidências. Remova linhas inaplicáveis e adicione verificações específicas.

| Área | Finalidade | Comando/ponto de entrada | Acionamento local | Acionamento em CI/agendado | Bloqueio / responsável |
|---|---|---|---|---|---|
| Build e validação de tipos | Detectar erros de compilação e tipos | | | | |
| Testes automatizados | Verificar comportamento nos níveis pertinentes | | | | |
| Cobertura | Indicar comportamento não testado e tendências | | | | |
| Formatação, lint e análise estática | Manter estilo e defeitos comuns consistentes | | | | |
| Complexidade e duplicação | Identificar código difícil ou repetido | | | | |
| Segurança do código | Encontrar padrões que possam causar vulnerabilidades | | | | |
| Dependências e atualizações | Encontrar pacotes vulneráveis/desatualizados/sem manutenção | | | | |
| Licenças | Conferir obrigações conforme política do projeto | | | | |
| Segredos e configuração | Detectar credenciais expostas e padrões inseguros | | | | |
| Acessibilidade | Validar expectativas WCAG e fluxos relevantes | | | | |
| Outras verificações | | | | | |

## Política de limites e achados

Para cobertura, complexidade, duplicação e análise estática, registre escopo medido, limite e utilidade, distinção entre achados novos e legados, achados que bloqueiam merge e aprovadores de exceção, e onde relatórios/evidências são mantidos.

Não otimize métricas em detrimento de design legível ou testes significativos. Um limite convida à investigação; não substitui julgamento de engenharia.

Para segurança, registre scanner/método, limites de cobertura, severidade, responsável pela triagem e expectativa de correção. Confirme relatórios relevantes; avalie limites de confiança, autorização, dados, falhas e abuso que automação talvez não detecte.

## Modelagem de ameaças e aceitação de riscos

Use a skill threat-modeling para mudanças que introduzam ou alterem autenticação, autorização, dados sensíveis, integrações, uploads, operações privilegiadas, limites de confiança ou comportamentos sujeitos a abuso. Registre um modelo delimitado com docs/templates/threat-model.md e vincule-o à spec.

Registre riscos aceitos com docs/templates/risk-exception.md, incluindo responsável, controles compensatórios e data de revisão/expiração. A exceção documenta uma decisão do projeto; não estabelece conformidade legal/regulatória.

## Acordos relacionados

- [Arquitetura](architecture.md)
- [Dependências](dependencies.md)
- [Convenções](conventions.md)
- [Workflow](workflow.md)
- [Plano de verificação](../templates/verification-plan.md)

## Referências

- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
- [OWASP Software Supply Chain Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html)