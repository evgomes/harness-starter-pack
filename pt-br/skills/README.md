# Catálogo de skills

As skills adicionam fluxos de trabalho opcionais e repetíveis para agentes. O instalador copia a biblioteca portátil para skills/ e, quando um harness compatível é escolhido, copia somente as skills selecionadas para a pasta de descoberta dele. O identificador da skill e o nome da pasta permanecem em inglês para compatibilidade.

| Skill | Quando usar |
|---|---|
| [accessibility-review](accessibility-review/SKILL.md) | Revisar alterações de interface com critérios WCAG aplicáveis e evidências automatizadas/manuais. |
| [browser-visual-validation](browser-visual-validation/SKILL.md) | Inspecionar em navegador interface, interações, console e evidências após mudanças visuais. |
| [dependency-review](dependency-review/SKILL.md) | Revisar inventário, licença, manutenção, vulnerabilidades e atualização de dependências. |
| [feature-brainstorming](feature-brainstorming/SKILL.md) | Explorar problema, restrições e opções antes de criar a spec, quando houver incerteza. |
| [graphify](graphify/SKILL.md) | Navegar por código desconhecido usando o índice AST local do Graphify. |
| [graphify-setup](graphify-setup/SKILL.md) | Instalar o CLI Graphify na máquina, configurar o índice do projeto e validar consultas. |
| [hook-authoring](hook-authoring/SKILL.md) | Projetar/revisar hooks opcionais com limites explícitos e operação segura. |
| [security-review](security-review/SKILL.md) | Revisar riscos de segurança concretos contra acordos e orientação OWASP aplicáveis. |
| [shift-left-code-review](shift-left-code-review/SKILL.md) | Fazer uma revisão adversarial ao fim de uma implementação completa baseada em spec. |
| [threat-modeling](threat-modeling/SKILL.md) | Modelar ameaças de mudanças que afetam dados, identidade, confiança ou abuso. |
| [ui-design-exploration](ui-design-exploration/SKILL.md) | Pesquisar/prototipar alternativas visuais antes da spec quando a direção ainda estiver em aberto. |

As skills graphify e graphify-setup vêm pré-selecionadas no instalador; as demais são opcionais. Dependências de apoio podem ser incluídas quando uma skill selecionada as referencia. Brainstorming e exploração de interface são opcionais; vá direto para uma spec ou implementação simples quando a solução já estiver clara. Skills orientam o agente, mas não substituem CI, revisão humana ou verificações determinísticas.