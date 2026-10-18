# Perfil React

Orientações de frontend para projetos React. Recomendações são ponto de partida: confirme manifests, configuração do framework, testes, acessibilidade e implantação antes de adotar.

## Uso com outros perfis

Escolha para app/interface React. Se o mesmo repositório contém backend ASP.NET Core e requer orientação integrada de arquitetura, convenções e spec, use ASP.NET Core + React. Mantenha contratos API/interface, autenticação e decisões entre stacks em docs/agreements/architecture.md.

## Arquitetura e convenções

- Mantenha componentes focados em apresentação/interação; coloque comportamento de domínio reutilizável em módulos explícitos quando melhorar testes e clareza.
- Autorização/validação do servidor são autoritativas. Trate browser, route guards e validação cliente como controles de conveniência não confiáveis.
- Explicite estados carregando, vazio, sucesso e erro. Evite acoplamento oculto e efeitos que duplicam estado derivado.
- Use HTML semântico e nomes acessíveis; preserve teclado, foco visível, mensagens compreensíveis e reflow responsivo.
- Registre versão React, renderização, roteamento, estado, client API e estratégia de testes no acordo de arquitetura.
- Use [templates da stack](docs/templates/README.md) para specs de interface, verificação e ameaças no cliente/browser.
- Use [ui-design-exploration](../../skills/ui-design-exploration/SKILL.md) e [templates de design](docs/templates/design-exploration.md) ao comparar direções antes da spec. Prototipe dados simulados com stack e componentes existentes.
- Para mudanças visíveis, use [browser-visual-validation](../../skills/browser-visual-validation/SKILL.md) e prefira Chrome oficial quando disponível. O [guia de navegador](../../guides/browser-testing.md) explica configurações e como relatar limitações.

## Verificações candidatas

Derive comandos dos scripts e lockfile do projeto. Não presuma gerenciador nem instale ferramentas neste perfil.

| Área | Verificações candidatas |
|---|---|
| Formatação/lint | Scripts existentes, limitados aos arquivos alterados quando possível |
| Tipos | Typecheck do projeto quando TypeScript for usado |
| Build | Build de produção e ambiente configurado |
| Testes | Unitários/componentes focados por slice; suíte completa e integração/ponta a ponta ao fim |
| Acessibilidade | Automação e verificações adequadas de teclado, foco, zoom/reflow e AT |
| Segurança | Limites cliente/servidor, exposição de dados, dependências e análise estática configurada |

Registre verificações e evidências no [acordo de qualidade/segurança](../../docs/agreements/quality-and-security.md); use [plano de verificação](../../docs/templates/verification-plan.md) para risco elevado ou entre camadas.