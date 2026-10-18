---
name: shift-left-code-review
description: Faça uma revisão adversarial ao fim de uma implementação completa guiada por spec, contra spec, acordos, SOLID/Clean Code, segurança, acessibilidade, dependências e evidências. Relate achados acionáveis sem editar, salvo pedido.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Revisão de código shift-left

Para trabalho guiado por spec, execute esta revisão uma vez depois de concluir todos os slices e a verificação final. Não a repita a cada slice. Se não houver modelo forte disponível, a pessoa responsável pode executar a skill manualmente. Verificações focadas após correções são esperadas; não exigem nova rodada adversarial salvo pedido explícito.

## Entradas da revisão

Leia spec/decisões, arquitetura.md, conventions.md, quality-and-security.md, plano de verificação e orientações de stack/segurança/acessibilidade pertinentes. Inspecione diff e código relacionado. Use Graphify para localizar impacto quando útil e confirme no código/testes. Sem spec, declare contrato e lacunas existentes sem inventar requisitos.

## Revisão

1. Compare requisitos e critérios de aceitação com o comportamento e as evidências.
2. Procure defeitos concretos de corretude, arquitetura, segurança/privacidade, acessibilidade, confiabilidade, dependências, manutenção e aderência às convenções.
3. Confirme cada suspeita no código ou em resultado determinístico; descarte preferências sem regra aplicável e hipóteses sem suporte.
4. Relate cada achado com severidade justificada, cenário, impacto, evidência e correção recomendada. Separe limitações, riscos residuais e verificações que não foram possíveis.
5. Não edite a mudança durante a revisão, salvo solicitação explícita. Use docs/templates/code-review.md para registrar o relatório.