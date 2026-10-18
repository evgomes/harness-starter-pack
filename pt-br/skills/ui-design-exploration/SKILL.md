---
name: ui-design-exploration
description: Explore e prototipe uma interface quando a pessoa quiser escolher direção visual antes de uma spec. Pesquise pelo menos três ideias, prototipe dados simulados com a stack do app e encaminhe decisões aceitas para a spec.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Exploração de design de interface

Use esta skill opcional quando o problema do usuário está claro, mas a solução visual/interativa precisa de alternativas. Ignore-a quando design e comportamento já estiverem definidos. É pesquisa e protótipo; não transforme isso silenciosamente em implementação de produção.

## 1. Inspecione projeto e delimite exploração

Leia instruções, design system/guia de estilo, acessibilidade, perfil de stack, rotas e componentes existentes. Confirme framework e ferramentas reais no repositório; não suponha que a stack esperada já está instalada. Combine escopo, rota de demonstração, dados simulados, estados e exclusões de produção.

## 2. Pesquise direções de design

Pesquise pelo menos três ideias materialmente diferentes. Registre URL, data de acesso, padrão observado, adequação e trade-offs. Use fontes diretas e não copie marca ou design distintivo por inteiro.

## 3. Proponha e prototipe

Apresente hierarquia e interação de opções, encaixe no design system, acessibilidade, responsividade, benefícios, riscos e questões em aberto. Após a pessoa escolher, implemente somente protótipo isolado com dados fictícios e rotas de demonstração; sem integração com API/backend salvo aprovação. Use os componentes existentes e registre componentes reutilizáveis.

Considere tema claro/escuro e preferência do sistema quando fizerem parte do produto; siga tokens e mecanismo de override existentes. Teste foco, teclado, contraste, zoom/reflow, estados de erro/carregamento, motion reduzido e cores forçadas conforme aplicável.

## 4. Apresente evidências e faça handoff

Forneça execução, rota, estados simulados, capturas/prévia, verificações realizadas e limitações. Registre direção aceita e decisão da pessoa responsável em docs/templates/ui-design-exploration.md. Leve contratos de interação, comportamento, componentes, dúvidas e aceitação para a spec. Não implemente funcionalidade de produção sem aceite.