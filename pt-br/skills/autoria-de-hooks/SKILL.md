---
name: autoria-de-hooks
description: Projete, implemente ou revise hook opcional de repositório/harness com comportamento explícito, padrões seguros, suporte multiplataforma e falhas verificáveis.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Autoria de hooks

Hooks são integrações opcionais, não um mecanismo universal. Mantenha a verificação portátil quando viável; crie adaptador específico somente quando o harness suportar o evento com segurança.

## Design

1. Leia acordos de qualidade/segurança, configuração existente e en/hooks/README.md.
2. Escolha o mecanismo mais leve: skill/instruções para tarefas contextuais, hook local para verificação determinística rápida ou CI/automação agendada para barreira autoritativa/recorrente.
3. Defina evento, condições, entradas, ação, escopo, saídas, timeout, código de retorno e comportamento quando falhar.
4. Registre runtime/versões, plataformas, efeitos colaterais, rede/dados, segredos, permissões, configuração, bypass e remoção em docs/templates/contrato-de-hook.md.
5. Confirme interface e segurança na documentação oficial atual do harness; não copie configuração de outro harness.
6. Mantenha instalação opt-in, mescle configuração existente e valide sucesso, achado, ferramenta ausente, timeout e erro.

Não instale ferramentas, altere código automaticamente, faça rede ou reduza controles de segurança de forma implícita.
