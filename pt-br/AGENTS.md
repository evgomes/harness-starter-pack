# Instruções compartilhadas para agentes

Este arquivo é uma base para projetos de software. Adapte-o ao repositório real antes de confiar nele. As decisões específicas do projeto em docs/agreements/ têm precedência sobre sugestões genéricas.

## Primeiros passos

1. Inspecione instruções do repositório, estado do Git, código-fonte relevante, testes e documentação existente.
2. Leia somente as partes dos acordos aplicáveis à tarefa; não carregue todas as skills por padrão. Para mudanças de comportamento, segurança, qualidade ou dependências, consulte quality-and-security.md e dependencies.md.
3. Para um fluxo de código desconhecido, use Graphify se disponível. Antes da primeira consulta, atualize o índice ou confirme que está atual com pwsh <caminho-da-skill>/scripts/refresh-graph.ps1 ou bash <caminho-da-skill>/scripts/refresh-graph.sh (macOS/Linux, requer Python 3). Atualize-o após mudanças no código e antes de concluir. Se o hook de início de sessão apontar configuração ausente ou índice desatualizado, siga graphify-setup ou graphify; nunca consulte um grafo desatualizado. Confira os resultados no código e nos testes. Use busca exata para verificações exaustivas.
4. Antes de uma implementação substancial, declare entendimento, escopo, premissas e evidências.

## Escolha um fluxo proporcional

- **Exploração opcional:** use feature-brainstorming se problema, solução ou restrições estiverem pouco claros. Ignore-a quando a pessoa já souber o que deseja.
- **Exploração de interface:** use ui-design-exploration para pesquisar pelo menos três ideias e prototipar com a stack real e dados simulados. Após a escolha, leve as decisões para a spec.
- **Entenda, depois especifique:** leia acordos de arquitetura/convenções e padrões próximos no código. Antes de redigir uma spec, siga as regras Git e crie/troque para a branch necessária. Para mudanças relevantes, entre camadas, de segurança/privacidade/dados ou com vários slices, use docs/templates/spec.md ou o template da stack. Inclua necessidade, escopo, contexto, premissas, critérios de aceitação, riscos, verificação e slices ordenados. A pessoa responsável revisa os critérios antes da implementação.
- **Prova primeiro:** quando uma premissa precisar de validação, Slice 1 deve ser o slice de prova. Caso contrário, Slice 1 é o primeiro slice de entrega. Execute os demais em sequência, subitem por subitem, e só avance depois de concluir e evidenciar todos os subitens do slice atual.
- **Planejamento de verificação:** use docs/templates/verification-plan.md quando verificações abrangerem várias camadas ou houver risco relevante. Registre o que foi e não foi executado.
- **Modelagem de ameaças:** carregue threat-modeling quando mudanças afetarem identidade, dados sensíveis, limites de confiança, integrações, uploads, operações privilegiadas ou abuso.
- **Implementação:** mantenha mudanças revisáveis. Execute verificações focadas no slice ativo. Deixe a suíte completa para depois de todos os slices, salvo exigência do projeto. Atualize status/evidências da spec e o handoff após cada item e antes de avançar.
- **Aditivos:** não mude escopo, decisões ou acordos silenciosamente. Registre proposta, motivo e impacto; obtenha decisão e atualize o plano.
- **Handoff:** crie um handoff para implementação orientada por spec e mantenha branch, slice/subitem, evidências, bloqueios e próxima ação atualizados.
- **Revisão:** faça uma rodada adversarial ao fim da implementação completa contra requisitos e diff final. Use modelo forte quando disponível ou a skill shift-left-code-review. Não repita a revisão a cada slice.
- **Exceções:** documente riscos aceitos com responsável, controles compensatórios e data de revisão.

## Padrões de engenharia

- Siga arquitetura e perfil de stack do projeto. Use SOLID e Clean Code para clareza, testabilidade e isolamento, sem abstrações desnecessárias.
- Considere segurança, privacidade, acessibilidade, confiabilidade e integridade de dados no contrato da funcionalidade quando aplicável.
- Para interface visível no navegador, valide comportamento renderizado com Chrome oficial quando disponível; use browser-visual-validation e informe o ambiente utilizado.
- Prefira ferramentas locais determinísticas para lint, formatação, testes, auditoria e políticas. Informe comandos e resultados exatos.
- Antes de adicionar dependências, verifique finalidade, manutenção, licença, risco transitivo e segurança; atualize docs/agreements/dependencies.md.
- Nunca coloque segredos ou dados pessoais reais em prompts, handoffs, fixtures ou revisões.

## Delegação e worktrees

Use subagentes em paralelo somente quando a pessoa usuária pedir explicitamente. Quando solicitados, o agente principal mantém orquestração, escopo, arquitetura/segurança, contratos compartilhados, integração, verificação e relatório final. Prefira modelos fortes para orquestração e decisões ambíguas ou de alto impacto. Modelos de menor custo podem implementar tarefas delimitadas e verificáveis. Defina arquivos, resultado, evidências e handoff; confira o trabalho integrado. Use worktrees para isolamento quando solicitadas ou exigidas pelo fluxo.

## Relatório de conclusão

Resuma mudanças, contratos/arquivos afetados, verificações realmente executadas, achados resolvidos e limitações. Mantenha spec e handoff fiéis ao estado final.