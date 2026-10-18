# Prompts de modelo de ameaças React

Use como extensão ao [template comum](../../../../docs/templates/threat-model.md), não como substituto. Responda o aplicável e confira browser, servidor, renderização e implantação reais.

## Limites e componentes

- Quais rotas, componentes, armazenamento browser, renderização servidor, clients API e scripts terceiros participam?
- Que dados/operações passam servidor-browser, browser-API ou aplicação-origem externa?
- O que é código cliente público e quais controles são autoritativos no servidor?
- Há SSR, server actions, edge functions ou variáveis de build?

## Perguntas específicas React/browser

- Autenticação/autorização depende somente de UI oculta, guards, estado cliente ou controles desativados?
- Dados pessoais, tokens, API keys ou config só-servidor podem entrar no bundle/HTML/armazenamento/logs?
- Valores não confiáveis chegam a HTML, URLs/navegação, rich text ou APIs DOM inseguras?
- Destinos de redirects, links, iframes e origens externas são limitados?
- Requests obsoletas, corrida, cache, atualizações otimistas ou estado compartilhado revelam dados de outro usuário?
- Dados sensíveis aparecem em erros, analytics, telemetria, source maps, URLs ou histórico?
- Scripts/dependências/build comprometidos acessam dados da página?
- Validação cliente corresponde à do servidor sem ser confundida com autorização/integridade?
- Premissas de CSRF/cookie/CORS/tokens correspondem à topologia real?

Para cada ponto aplicável, descreva ator/ação/impacto e conecte mitigação a controles de servidor, testes, browser ou implantação. Controles cliente melhoram UX, mas não impõem confiança contra quem controla o browser.