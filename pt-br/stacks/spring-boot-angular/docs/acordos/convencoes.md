# Prompts de convenções Spring Boot + Angular

- Mantenha explícita a responsabilidade de Spring Boot e Angular; mudanças entre limites devem declarar impacto no contrato API.
- Valide entradas e autorização no servidor mesmo quando Angular também valida ou oculta controles.
- Mantenha tipos cliente e schemas servidor alinhados por processo documentado, manual ou geração.
- Teste backend no nível útil mais restrito e verifique a interface API afetada em mudanças entre stacks.
- Preserve semântica acessível, teclado e estados visíveis de erro/vazio/carregamento.
- Não duplique no browser lógica de domínio autoritativa do servidor; cálculos cliente são apresentação salvo acordo explícito.
