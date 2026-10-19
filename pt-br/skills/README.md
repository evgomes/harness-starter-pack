# Catálogo de skills

As skills adicionam fluxos de trabalho opcionais e repetíveis para agentes. O instalador copia a biblioteca portátil para skills/ e, quando um harness compatível é escolhido, copia somente as skills selecionadas para a pasta de descoberta dele. Os IDs internos usados pelo instalador permanecem estáveis; as pastas e referências da versão pt-br usam nomes em português quando isso faz sentido. Graphify mantém o nome oficial.

| Skill | Quando usar |
|---|---|
| [Revisão de acessibilidade](revisao-de-acessibilidade/SKILL.md) | Revisar alterações de interface com critérios WCAG aplicáveis e evidências automatizadas/manuais. |
| [Validação visual no navegador](validacao-visual-no-navegador/SKILL.md) | Inspecionar em navegador interface, interações, console e evidências após mudanças visuais. |
| [Revisão de dependências](revisao-de-dependencias/SKILL.md) | Revisar inventário, licença, manutenção, vulnerabilidades e atualização de dependências. |
| [Exploração de funcionalidades](exploracao-de-funcionalidades/SKILL.md) | Explorar problema, restrições e opções antes de criar a spec, quando houver incerteza. |
| [Navegação com Graphify](graphify/SKILL.md) | Navegar por código desconhecido usando o índice AST local do Graphify. |
| [Configuração do Graphify](configuracao-do-graphify/SKILL.md) | Instalar o CLI Graphify na máquina, configurar o índice do projeto e validar consultas. |
| [Criação de hooks](autoria-de-hooks/SKILL.md) | Projetar/revisar hooks opcionais com limites explícitos e operação segura. |
| [Revisão de segurança](revisao-de-seguranca/SKILL.md) | Revisar riscos de segurança concretos contra acordos e orientação OWASP aplicáveis. |
| [Revisão antecipada de código](revisao-antecipada-de-codigo/SKILL.md) | Fazer uma revisão adversarial ao fim de uma implementação completa baseada em spec. |
| [Modelagem de ameaças](modelagem-de-ameacas/SKILL.md) | Modelar ameaças de mudanças que afetam dados, identidade, confiança ou abuso. |
| [Exploração de design de interface](exploracao-de-design-de-interface/SKILL.md) | Pesquisar/prototipar alternativas visuais antes da spec quando a direção ainda estiver em aberto. |

As skills Graphify e Configuração do Graphify vêm pré-selecionadas no instalador; as demais são opcionais. Dependências de apoio podem ser incluídas quando uma skill selecionada as referencia. Exploração de funcionalidades e de interface são opcionais; vá direto para uma spec ou implementação simples quando a solução já estiver clara. Skills orientam o agente, mas não substituem CI, revisão humana ou verificações determinísticas.
