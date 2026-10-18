---
name: accessibility-review
description: Revise mudanças de interface conforme o acordo de acessibilidade do projeto e os critérios WCAG aplicáveis. Combine revisão do código, automação aprovada, teclado e tecnologia assistiva; não declare conformidade somente com base em automação.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Revisão de acessibilidade

1. Confirme padrão, versão, nível, grupos de usuários e requisitos jurisdicionais definidos pelo projeto. Se não houver, registre como decisão pendente; não afirme conformidade.
2. Inspecione estrutura semântica, nomes/rótulos, teclado, ordem/visibilidade/retorno do foco, identificação/recuperação de erros, anúncios de status, contraste, redimensionamento/reflow, movimento, tamanho dos alvos e alternativas a gestos de arrastar.
3. Quando adequado, execute verificações automatizadas aprovadas. Registre ferramenta/versão, páginas/componentes, resultado e limitações.
4. Exercite manualmente os fluxos afetados por teclado e tecnologia assistiva relevante, quando disponível. Registre navegador/AT, passos, esperado/obtido e combinações não testadas.
5. Relate falhas concretas conforme critério ou acordo aplicável, com cenário, impacto, caminho:linha ou reprodução e correção. Separe achados confirmados de riscos que exigem teste com usuários.