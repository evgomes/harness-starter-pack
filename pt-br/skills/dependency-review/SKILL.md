---
name: dependency-review
description: Revise inventário, licenças, manutenção, vulnerabilidades conhecidas, oportunidades de atualização e riscos de dependências. Use em mudanças de dependência ou revisão periódica; esta skill não agenda revisões.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Revisão de dependências

## Comece pelas evidências do projeto

1. Leia docs/agreements/dependencies.md e identifique ecossistemas, manifests, lockfiles, registries, política, responsável e periodicidade.
2. Inspecione manifests e lockfiles. Diferencie dependências diretas e transitivas; não deduza versões resolvidas a partir de intervalos.
3. Use fontes de pacotes e scanners aprovados. Registre comandos, versões das ferramentas, fontes de dados, data, escopo e limitações.

## Avalie

- Confirme pacote, versão resolvida, finalidade, licença publicada, manutenção, origem e dependências transitivas relevantes.
- Consulte fontes oficiais de avisos/registries para vulnerabilidades; registre intervalo afetado, exposição, correção disponível e evidências.
- Para atualização, considere compatibilidade, impacto, changelog, testes e caminho de rollback. Não atualize apenas para eliminar um número do scanner sem compreender o efeito.
- Não assuma que SPDX garante conformidade jurídica. Sinalize dual licensing, exceções e obrigações que dependem do contexto para revisão do responsável do projeto.
- Separe achados confirmados de alertas que precisam de validação. Nunca inclua credenciais ou dados de ambiente em relatórios versionados.

## Registre e encaminhe

Atualize o inventário, as decisões, os riscos aceitos, o responsável e a próxima revisão no acordo de dependências. Abra itens de acompanhamento com pacote/versão, evidência, impacto, mitigação, responsável e prazo. A skill não executa auditorias recorrentes sozinha; use CI/automação agendada.