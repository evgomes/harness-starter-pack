# Acordo de fluxo de engenharia

Este acordo define um fluxo padrão reutilizável para mudanças assistidas por IA. Adapte comandos, convenções de branch, aprovações e requisitos de entrega ao repositório de destino. A arquitetura, as convenções e os padrões de código verificados prevalecem sobre orientações genéricas.

## Entenda o projeto e a solicitação

1. Inspecione instruções, estado do Git, código relevante, testes e documentação antes de propor mudanças.
2. Leia os acordos de arquitetura e convenções, além das orientações relevantes de qualidade/segurança e dependências. Aprenda padrões no código próximo. Não trate exemplos do starter pack como fatos sobre o projeto.
3. Antes de implementação substancial, resuma solicitação, escopo, premissas, evidências e ambiguidades. Pergunte somente quando escolhas pendentes mudarem materialmente o trabalho; caso contrário, declare uma premissa razoável e prossiga.
4. Exploração é opcional. Use feature brainstorming quando problema ou solução não estiverem claros e UI design exploration quando alternativas de interface precisarem de pesquisa/protótipo. Se a solução estiver clara, vá direto à spec ou a um contrato de tarefa simples.

## Especificação e aprovação

Para mudanças relevantes de comportamento, entre camadas, segurança/privacidade, dados ou com múltiplos slices, crie spec usando docs/templates/spec.md ou o template da stack. Uma mudança pequena e de baixo risco pode usar um contrato de tarefa simples quando permitido pela política local.

Antes de redigir, siga as convenções de branch e confirme branch e estado de trabalho. A spec deve registrar necessidade, resultado, escopo, comportamento/arquitetura existentes, restrições, premissas a provar, critérios de aceitação, riscos, verificação e slices ordenados. Separe fatos, sugestões e decisões. A pessoa responsável revisa e ajusta os critérios antes de aceitar a spec e iniciar a implementação.

## Provas, slices e implementação

- Identifique premissas capazes de invalidar o plano. Se alguma precisar de validação prévia, faça de Slice 1 o slice de prova e registre método/resultado. Se não houver prova necessária, Slice 1 é a primeira entrega.
- Se uma prova falhar ou mudar o design, interrompa o trabalho dependente, explique evidência e impacto e revise a spec com a pessoa responsável.
- Declare ordem de slices e subitens na spec aceita. Execute sequencialmente, subitem por subitem; não inicie o próximo slice até concluir e evidenciar todos os itens do atual.
- Mantenha cada slice coerente e revisável. Execute verificações focadas durante a implementação; execute suíte completa e barreiras gerais após todos os slices, salvo exigência do acordo ou necessidade de segurança aceita.
- Atualize checklist/evidências da spec após cada subitem. Mantenha handoff atualizado com branch, slice/subitem, decisões, caminhos alterados, verificações, riscos e próxima ação.
- Não altere silenciosamente escopo, decisões ou acordos. Registre proposta/impacto, obtenha decisão e atualize o plano.

## Subagentes e seleção de modelos

Use subagentes em paralelo somente quando a pessoa usuária pedir explicitamente. Não delegue apenas porque tarefas parecem independentes ou o paralelismo pode economizar tempo.

Quando solicitado, o agente principal mantém orquestração, escopo, decisões de arquitetura/segurança, contratos compartilhados, integração, verificação e relatório. Prefira modelo forte para orquestração e decisões ambíguas/de alto impacto. Modelo mais econômico pode executar tarefa delimitada com contrato claro e verificação independente. Defina tarefa, decisões, arquivos, resultado, evidências e handoff; confira o trabalho integrado.

## Verificação, revisão e entrega

- Use ferramentas locais determinísticas para formatação, lint, testes, auditoria de dependências e políticas. Informe comandos/resultados exatos; não afirme sucesso sem execução.
- Use plano de verificação quando houver várias camadas ou risco relevante. Faça modelagem de ameaças para identidade, dados sensíveis, limites de confiança, integrações, operações privilegiadas ou abuso.
- Para interface visível no navegador, inspecione o comportamento renderizado e informe estados/ambientes exercitados.
- Depois dos slices, faça uma única revisão adversarial da spec completa e do diff final. Use modelo forte quando disponível; caso contrário, a pessoa responsável executa a skill. Resolva achados ou registre exceções com responsável, controles e data. Revisão por IA complementa, não substitui, revisão humana e CI.
- Relate mudanças, evidências, verificações executadas/adiadas, revisão e riscos. Mantenha spec e handoff fiéis ao resultado.
