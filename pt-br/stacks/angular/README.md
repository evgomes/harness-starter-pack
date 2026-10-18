# Perfil Angular

Orientações de frontend Angular. Confira versões de Angular/CLI, layout do workspace, modo de renderização, gerenciador de pacotes, design system e browsers suportados no repositório. O instalador copia somente orientação.

## Arquitetura e convenções

- Siga o guia de estilo Angular e agrupe código por funcionalidade/domínio quando isso ajudar navegação e responsabilidade.
- Use injeção de dependência, router, forms e HTTP do Angular; evite criar abstrações próprias sobre recursos já usados.
- Defina intencionalmente estado de interface e servidor. Explicite carregando, vazio, erro, sucesso e acesso negado.
- Alinhe contratos de API ao backend; clients gerados são opcionais e precisam ser adotados deliberadamente no workflow.
- Evite APIs DOM inseguras e métodos de bypass de confiança. Prefira bindings/sanitização Angular; coordene CSP/Trusted Types com implantação.
- Trate acessibilidade no design e verificação: HTML semântico, teclado, foco, rótulos e anúncios úteis.

## Verificações candidatas

| Área | Opção |
|---|---|
| Testes unitários/componentes | Angular CLI ng test; docs atuais descrevem Vitest + jsdom em novos projetos CLI, mas setups Karma existentes continuam suportados. Confira versão/configuração. |
| Lint | angular-eslint + ESLint, compatíveis com versões Angular/ESLint do projeto. |
| Tipos/build | Build Angular CLI e diagnósticos do compilador/TypeScript nos scripts existentes. |
| Browser/ponta a ponta | Playwright para fluxos reais se adotado pelo repositório. |
| Qualidade/segurança | Orientação de segurança Angular, revisão de dependências, acessibilidade e testes de guards/autorizações vindas do servidor. Guards do cliente não autorizam no servidor. |

São recomendações, não dependências instaladas nem políticas obrigatórias.

## Templates

Veja o [índice de templates](docs/templates/README.md), [exploração de interface](../../docs/templates/ui-design-exploration.md), [verificação](../../docs/templates/verification-plan.md) e skill de acessibilidade.

## Referências

- [Guia de estilo Angular](https://angular.dev/style-guide)
- [Segurança Angular](https://angular.dev/best-practices/security)
- [Testes Angular](https://angular.dev/guide/testing)
- [angular-eslint](https://github.com/angular-eslint/angular-eslint)
- [Playwright](https://playwright.dev/docs/intro)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)