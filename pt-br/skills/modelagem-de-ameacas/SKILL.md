---
name: modelagem-de-ameacas
description: Crie/atualize modelo de ameaças delimitado e baseado em evidências, ligando cenários a mitigações e verificações. Use para identidade, dados sensíveis, limites de confiança, integrações, uploads e operações privilegiadas.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Modelagem de ameaças

Use este fluxo opcional quando uma mudança tiver risco relevante de segurança/privacidade. Mantenha o modelo proporcional; mudanças focadas podem exigir poucos cenários concretos. Checklist não equivale a garantia de segurança.

## Reúna contexto

1. Leia spec, acordo de arquitetura, qualidade/segurança e modelo de ameaças existente.
2. Delimite mudança, ativos, atores, pontos de entrada, limites de confiança, dados e integrações.
3. Confirme fatos no código, configuração e implantação; identifique premissas e informações desconhecidas.

## Modele cenários

- Use STRIDE, casos de abuso ou outro método como apoio; adapte ao sistema.
- Escreva cada cenário com precondição, ação, limite afetado e impacto.
- Relacione mitigação e evidência de verificação; não trate controles nominais como prova.
- Considere autorização por objeto/ação, abuso, privacidade, disponibilidade, segredo e dependências conforme o contexto.
- Registre riscos residuais, responsáveis, decisão e exceções aprovadas.

Use docs/templates/modelo-de-ameacas.md, vincule-o à spec e peça revisão da pessoa responsável. Reavalie se arquitetura, dados, identidade, implantação ou integração mudarem.
