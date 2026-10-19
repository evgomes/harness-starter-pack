# Exploração de design React: [tela ou funcionalidade]

> Status: Explorando / Protótipo pronto / Direção aceita / Encaminhado para spec · Responsável: [engenharia/design] · Data: [data] · Branch: [conforme repositório]

Use junto ao [template comum de exploração de interface](../../../../docs/templates/exploracao-de-design-de-interface.md). Confirme versão React, framework de renderização, router, design system, CSS e scripts reais. Use stack e convenções existentes, sem criar configuração paralela.

## Pesquisa e direção

- Link da exploração comum (inclua ao menos três ideias, URLs e datas):
- Opção escolhida e decisão:
- Objetivo do usuário e rota/tela:
- Estados: carregando / vazio / preenchido / erro / desabilitado / sucesso:
- Breakpoints/viewports e modelo de interação:

## Contrato do protótipo React

- Rota existente ou entrada de prévia isolada:
- Árvore de componentes e responsabilidades:
- Componentes reutilizáveis novos/alterados:
- Componentes/tokens do design system a reutilizar:
- Módulo/tipos de dados simulados e reset:
- Chamadas de rede/API excluídas:
- Considerações de renderização/hidratação:
- Comando de execução/prévia dos scripts existentes:

Mantenha dados simulados separados dos serviços de produção. Não adicione dependências nem altere comportamento API de produção sem pedido explícito.

## Estilos e temas

- Estratégia CSS existente:
- Origem/nomenclatura de tokens:
- Mecanismo de override adequado:
- Valores de componente que devem usar tokens:
- Estados demonstrados em tema claro/escuro:
- Preferência do sistema e alternância:
- Personalização (cor/fonte/densidade/outros):
- Decisão: excluir / demonstrar / requisito aceito / opção futura:
- Persistência/reset se aceita:
- Proteções: contraste, foco, movimento reduzido, cores forçadas e fallback legível:

Não presuma que customização de tema por usuário esteja no escopo. Se aceita, garanta overrides detectáveis, testáveis e acessíveis.

## Acessibilidade e interação

- Meta WCAG:
- Semântica, nomes, rótulos e relação com erros:
- Teclado, ordem/retorno/visibilidade do foco:
- Anúncios de carregamento/erro/status:
- Contraste, zoom/reflow, alvos e movimento:
- Verificações manuais/browser e automatizadas:
- AT/dispositivos não testados e limitações:

## Registro no design system/guia de estilo

Para cada componente reutilizável novo/alterado, preencha [entrada de componente](entrada-guia-de-estilo-de-componentes.md) e adicione ao local real do guia de estilo.

| Componente | Responsabilidade/variantes | Caminho de implementação | Caminho da entrada | Status |
|---|---|---|---|---|
| | | | | Planejado |

## Aprovação e passagem para spec

- Prévia/rota:
- Estados simulados:
- Direção aprovada e data:
- Mudanças/decisões pendentes:
- Comportamentos, estados, API de componentes, tema e acessibilidade para levar à spec:
- Próxima ação: criar/atualizar spec na branch correta; critérios revisados antes da implementação.
