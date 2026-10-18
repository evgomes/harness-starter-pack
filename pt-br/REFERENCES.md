# Referências e justificativas

Este guia reúne materiais que informam os workflows e perfis de stack do pacote. As referências ajudam a compreender e avaliar práticas; elas não tornam o pacote dependente de fornecedor, framework, produto, arquitetura ou ferramenta de workflow. Quando houver divergência, priorize os acordos do repositório de destino e a documentação oficial vigente.

**Links verificados em:** 2026-10-17. Recomendações sobre produtos, modelos, APIs e frameworks podem mudar; confira a versão e a aplicabilidade da fonte antes de usá-las.

## Como estas referências informam o pacote

| Tema | Justificativa refletida neste repositório |
|---|---|
| Specs e critérios de aceitação | Combine uma descrição revisável da necessidade, escopo, contexto, decisões, evidências e trabalho ordenado antes da implementação. Esclareça ambiguidades e verifique consistência, sem tratar a primeira versão como autoridade final. |
| Handoffs e contexto | Registre decisões, progresso, evidências e próxima ação em um artefato conciso e inspecionável, para que uma nova sessão recupere o estado relevante sem reproduzir todo o histórico. Handoff é memória explícita do projeto, não cache de prompt. |
| Slices e checklists | Divida o trabalho em itens ordenados e acompanhados de evidências. Durante a implementação, verifique o comportamento alterado no menor escopo útil e, ao concluir a funcionalidade, execute as verificações amplas necessárias. Checklist registra progresso; por si só, não prova resultado. |
| Subagentes e trabalho paralelo | O pacote permite subagentes paralelos somente quando a pessoa desenvolvedora solicita explicitamente. Quando houver delegação, delimite o trabalho e considere o custo de coordenação e verificação. |
| .NET e React | Use orientações oficiais da plataforma para informar arquitetura e padrões de código, e confira as versões, a estrutura e as convenções do projeto de destino. Os exemplos são alternativas a avaliar, não blueprints obrigatórios. |
| Cache de prompts | Cache pode reutilizar processamento de conteúdo repetido. Não remove tokens do contexto nem atua como memória semântica. Comportamento, controles, retenção, preços e condições de cache variam por provedor. |
| Seleção de modelos | Escolha conforme dificuldade, risco, contexto, nível de qualidade, latência e custo; valide a escolha em tarefas representativas. Evite rankings permanentes e tabelas de preço em orientações duráveis, pois modelos e condições mudam. |

## Specs, checklists, slices e handoffs

- [GitHub Spec Kit: início rápido de Spec-Driven Development](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) — exemplo de esclarecimento de requisitos, criação de specs e planos, validação de checklists, ordenação de tarefas e verificação de consistência. Spec Kit é opcional, não requisito deste pacote.
- [GitHub Spec Kit: Agentic SDD](https://github.github.com/spec-kit/reference/agentic-sdd.html) — referência sobre a relação entre spec, plano, tarefas, implementação e verificações de convergência.
- [OpenAI Cookbook: Iterating development workflows with Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex) — exemplo de decisões por fase e arquivos de contexto para permitir a retomada de trabalhos longos. Os assets de workflow são convenções opcionais, não requisitos do Codex.
- [Google Testing Blog: Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html) — modelo influente para separar testes isolados e rápidos de testes maiores de integração e sistema. Adapte categorias e política de execução à suíte do projeto.
- [Context Engineering for AI Agents: Memory, Compaction, and How to Save Tokens](https://fronteiralabs.com.br/en-us/articles/context-engineering-for-ai-agents-memory-compaction-and-how-to-save-tokens/11) — explica contexto, memória e cache; compactação e seu risco de perda de contexto; handoffs, recuperação e diferença entre cache e redução de contexto.
- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — discute contexto como conjunto de trabalho limitado, estratégias de recuperação e isolamento da pesquisa de subagentes quando a delegação fizer sentido.

Os assets correspondentes são os templates de [spec](docs/templates/spec.md), [handoff](docs/templates/handoff.md) e [plano de verificação](docs/templates/verification-plan.md), junto às regras de sequência no [acordo de workflow](docs/agreements/workflow.md).

## Subagentes e execuções paralelas

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — compara workflows simples, roteamento, paralelização e padrões de orquestrador e trabalhadores; recomenda ajustar a complexidade à tarefa.
- [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — relato prático sobre definição de subtarefas focadas e síntese de resultados paralelos.
- [OpenAI Cookbook: Iterating development workflows with Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex) — exemplo de limites entre fases e transferência de contexto em tarefas de código.

Essas fontes descrevem padrões possíveis. O [acordo de workflow](docs/agreements/workflow.md) local é deliberadamente mais conservador: subagentes só são usados quando a pessoa desenvolvedora solicita, e worktrees/paralelismo não são pressupostos.

## Java e Spring Boot

- [Testes no Spring Boot](https://docs.spring.io/spring-boot/reference/testing/) — documenta suporte inicial de testes, JUnit Jupiter, AssertJ e módulos de teste focados.
- [Estruturação do código](https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html) — orientações para localização de pacotes e ponto de entrada da aplicação.
- [Configuração externa](https://docs.spring.io/spring-boot/reference/features/external-config.html) e [Actuator](https://docs.spring.io/spring-boot/reference/actuator/index.html) — recursos de configuração e operações; exposição e tratamento de segredos dependem das decisões de implantação.
- [Spring Modulith](https://docs.spring.io/spring-modulith/reference/) — suporte opcional a módulos para aplicações que se beneficiem de limites explícitos entre módulos de domínio.
- [Checkstyle](https://checkstyle.org/) e [Testcontainers para Java](https://java.testcontainers.org/) — ferramentas candidatas para estilo e testes de integração; verifique compatibilidade e necessidade no projeto.

O [perfil Spring Boot](stacks/spring-boot/README.md) sugere testes com JUnit/Spring, formatação e análises estáticas escolhidas pelo projeto e testes opcionais de integração com containers, sem exigir arquitetura, Maven ou Gradle específicos.

## Node.js e Express

- [Segurança do Express em produção](https://expressjs.com/en/advanced/best-practice-security/) — validação de entrada, TLS, Helmet, cookies seguros, limitação de taxa e revisão de dependências.
- [Desempenho e confiabilidade do Express](https://expressjs.com/en/advanced/best-practice-performance/) e [event loop do Node.js](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop) — práticas de confiabilidade e impacto de trabalho bloqueante no event loop.
- [Test runner do Node.js](https://nodejs.org/api/test.html), [ESLint](https://eslint.org/docs/latest/use/getting-started), [typescript-eslint](https://typescript-eslint.io/getting-started/), [Vitest](https://vitest.dev/guide/) e [Supertest](https://github.com/ladjs/supertest) — opções de testes e lint para avaliar conforme runtime e configuração de pacotes.

O [perfil Node.js + Express](stacks/node-express/README.md) separa verificações unitárias e HTTP e chama atenção para validação de entrada, autorização, configuração segura de sessão, risco de dependências e responsividade do event loop.

## Python e FastAPI

- [Aplicações maiores](https://fastapi.tiangolo.com/tutorial/bigger-applications/) e [dependências](https://fastapi.tiangolo.com/tutorial/dependencies/) — roteadores modulares e declarações de dependência reutilizáveis.
- [Testes no FastAPI](https://fastapi.tiangolo.com/tutorial/testing/) — abordagem com pytest e `TestClient` baseada em HTTPX.
- [Segurança no FastAPI](https://fastapi.tiangolo.com/tutorial/security/) e [conceitos de implantação](https://fastapi.tiangolo.com/deployment/concepts/) — mecanismos do framework e decisões de implantação a avaliar no contexto.
- [Ruff](https://docs.astral.sh/ruff/) e [mypy](https://mypy.readthedocs.io/en/stable/) — opções para lint/formatação e análise estática de tipos.

O [perfil Python + FastAPI](stacks/python-fastapi/README.md) oferece FastAPI como perfil e trata Django REST Framework como alternativa que exige orientações específicas próprias.

## Angular

- [Guia de estilo Angular](https://angular.dev/style-guide), [boas práticas de segurança](https://angular.dev/best-practices/security) e [testes](https://angular.dev/guide/testing) — orientações oficiais atuais. O runner padrão pode variar conforme a geração do Angular CLI e o workspace; confira antes de alterá-lo.
- [angular-eslint](https://github.com/angular-eslint/angular-eslint) — integração comunitária com ESLint; confira a matriz de suporte em relação às versões do projeto.
- [Playwright](https://playwright.dev/docs/intro) e [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — ferramenta candidata para testes em navegador real e padrão normativo de acessibilidade.

O [perfil Angular](stacks/angular/README.md) enfatiza templates e sanitização, estados de interação acessíveis, testes unitários/de componentes, lint e verificação em navegador real para fluxos críticos.

## .NET e ASP.NET Core

- [Documentação de arquitetura .NET da Microsoft](https://learn.microsoft.com/dotnet/architecture/) — catálogo de guias de arquitetura e material de referência para aplicações .NET.
- [Arquitetar aplicações web modernas com ASP.NET Core e Azure](https://learn.microsoft.com/dotnet/architecture/modern-web-apps-azure/) — discussão de arquitetura de ponta a ponta e implementação de referência. Trate a arquitetura como exemplo e valide os padrões com o produto e o framework atuais.
- [Arquiteturas comuns de aplicações web](https://learn.microsoft.com/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures) — discute estruturas monolíticas e em camadas, direção de dependências e trade-offs de Clean Architecture.
- [Princípios de arquitetura](https://learn.microsoft.com/dotnet/standard/modern-web-apps-azure-architecture/architectural-principles) — separação de responsabilidades e princípios de manutenibilidade.
- [Boas práticas ASP.NET Core](https://learn.microsoft.com/aspnet/core/fundamentals/best-practices) — considerações específicas de desempenho e runtime; selecione a versão da documentação compatível com a aplicação.

O [perfil ASP.NET Core](stacks/aspnet-core/README.md) e seus documentos de [arquitetura](stacks/aspnet-core/docs/agreements/architecture.md) e [convenções](stacks/aspnet-core/docs/agreements/conventions.md) transformam conceitos pertinentes em perguntas para validar contra um projeto real; não exigem Clean Architecture nem uma quantidade fixa de projetos.

## React

- [React: Thinking in React](https://react.dev/learn/thinking-in-react) — decomposição de interfaces em componentes, identificação de estados visuais e derivação de estado mínimo a partir do fluxo de dados.
- [React: Managing state](https://react.dev/learn/managing-state) — organização e compartilhamento de estado e como evitar estado redundante.
- [React: Sharing state between components](https://react.dev/learn/sharing-state-between-components) — escolha de um proprietário comum de estado quando componentes precisam se coordenar.
- [React: Reusing logic with custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks) — quando extrair lógica focada e reutilizável com estado.
- [MDN: Usar propriedades customizadas CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties) — valores reutilizáveis e sobrescritas pela cascata para tokens de design CSS.
- [W3C: Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — critérios normativos de acessibilidade; verificações automatizadas não substituem a avaliação dos critérios aplicáveis e dos fluxos de usuário.

O [perfil React](stacks/react/README.md), o [template de exploração de interface](docs/templates/ui-design-exploration.md) e os [templates de design React](stacks/react/docs/templates/README.md) incentivam reutilização do design system existente, estados explícitos, dados simulados, avaliação de temas/tokens e evidências de acessibilidade.

## SOLID, qualidade de código e práticas de engenharia

- [Clean Code: A Handbook of Agile Software Craftsmanship, 2ª edição](https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship-2nd-edition/P200000013239/9780135398579), de Robert C. Martin — referência editorial sobre legibilidade, nomes, funções, testes, heurísticas de design e princípios SOLID. Avalie as recomendações no contexto; não as trate como regras obrigatórias.
- [Google Engineering Practices: Code Review](https://google.github.io/eng-practices/review/) — orientações publicadas de revisão sobre design, comportamento, complexidade, testes, nomes, estilo e documentação. É um exemplo útil, não um processo obrigatório para toda equipe.
- [Microsoft Framework Design Guidelines](https://learn.microsoft.com/dotnet/standard/design-guidelines/) — orientações de design de APIs e bibliotecas .NET. O escopo são bibliotecas .NET e a página sinaliza que parte do conteúdo pode estar desatualizada; confirme recomendações relevantes na documentação atual.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — orientações de segurança de aplicações, mantidas e organizadas por tema. Escolha as folhas de referência que correspondam aos riscos do produto; uma lista genérica não determina segurança ou conformidade.

O [acordo comum de convenções](docs/agreements/conventions.md) usa SOLID e Clean Code como estímulos à clareza e testabilidade e desaconselha abstrações especulativas. O [acordo de qualidade e segurança](docs/agreements/quality-and-security.md) e a [skill de revisão de segurança](skills/security-review/SKILL.md) relacionam práticas de segurança aos riscos e evidências do projeto.

## Validação em navegador

- [Chrome DevTools para agentes](https://developer.chrome.com/docs/devtools/agents) e o [guia de configuração](https://developer.chrome.com/docs/devtools/agents/get-started) explicam como inspecionar e interagir com um Chrome ativo por MCP e ferramentas relacionadas. Integrações de navegador podem expor conteúdo e sessões autenticadas; use perfis isolados e dados de teste.
- [Configuração de navegador do Playwright](https://playwright.dev/docs/browsers) diferencia o Chromium gerenciado dos canais do Chrome com marca e descreve instalação/seleção. Prefira o runner e o navegador que o projeto já usa; não presuma que uma dependência nova é necessária.
- [Guia de Browser da OpenAI](https://learn.chatgpt.com/docs/browser) documenta o Browser integrado à superfície do aplicativo desktop e o diferencia do Codex CLI/IDE.
- [Claude Code Desktop](https://code.claude.com/docs/en/desktop) documenta pré-visualização e verificação local no painel Code, diferente da experiência de conversa do Claude Desktop.
- [Browser do Cursor](https://cursor.com/docs/agent/tools/browser) documenta o navegador nativo do agente, incluindo inspeção visual e recursos de console/rede.
- [Servidores MCP do OpenCode](https://opencode.ai/docs/mcp-servers/) documenta conexão de integrações opcionais de navegador por MCP.

O [guia de testes de navegador](guides/browser-testing.md) explica essas opções e a [skill de validação visual no navegador](skills/browser-visual-validation/SKILL.md) oferece um workflow independente de harness. Uma verificação renderizada comprova os estados exercitados, não a conformidade integral com WCAG nem a correção em todos os navegadores.

## Cache de prompts e gestão de contexto

- [API OpenAI: cache de prompts](https://developers.openai.com/api/docs/guides/prompt-caching) — comportamento e controles atuais específicos da OpenAI.
- [Anthropic: cache de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — comportamento e controles atuais específicos da Anthropic.
- [API Google Gemini: cache de contexto](https://ai.google.dev/gemini-api/docs/caching) — opções de cache de contexto específicas do Gemini.
- [Context Engineering for AI Agents](https://fronteiralabs.com.br/en-us/articles/context-engineering-for-ai-agents-memory-compaction-and-how-to-save-tokens/11) — explicação conceitual de como memória, compactação, recuperação e cache são ferramentas distintas.

Quando um contexto grande e estável se repete, cache do provedor pode reduzir latência ou custo de entrada se o produto/API oferecer esse recurso e a requisição cumprir as condições documentadas. Meça leituras, gravações e custo de cache. Não afirme que cache reduz o uso da janela de contexto, garante acerto ou muda o comportamento de um harness sem documentação desse harness. Para agentes conversacionais, instruções concisas, recuperação sob demanda, saídas limitadas de ferramentas e handoffs precisos são práticas separadas de gestão de contexto.

## Escolha de modelos por tipo de tarefa

- [OpenAI: seleção de modelos](https://developers.openai.com/api/docs/guides/model-selection) — guia dinâmico orientado a tarefas; nomes e recomendações dependem da oferta atual da OpenAI.
- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — explica o roteamento de tarefas comuns/simples para modelos eficientes e a escalada de tarefas que requerem mais raciocínio.
- [Anthropic: visão geral dos modelos](https://platform.claude.com/docs/en/models/overview) — modelos e especificações Claude atuais.
- [API Google Gemini: modelos](https://ai.google.dev/gemini-api/docs/models) — recursos e disponibilidade dos modelos Gemini.
- [OpenAI: boas práticas de raciocínio](https://developers.openai.com/api/docs/guides/reasoning-best-practices) — orientações sobre modelos e raciocínio específicas da API OpenAI.

Use um conjunto repetível de tarefas reais do projeto. Avalie correção, qualidade das evidências, aderência às instruções, regressões, correções na revisão, latência e custo total. Para uma tarefa delimitada, mantenha a opção mais rápida/econômica que atenda consistentemente ao nível exigido; use raciocínio mais forte em trabalhos ambíguos, de alto impacto, arquiteturais ou de revisão adversarial. Reavalie diante de mudanças em modelos, harnesses ou preços. Não copie nomes, preços ou configurações atuais específicas de provedores para acordos neutros como regras permanentes.

## Notas sobre o uso das fontes

- A documentação oficial de produto/framework é a melhor referência para comportamento atual e específico de implementação. Confira versão e data.
- Pesquisas e artigos de engenharia ajudam a explicar trade-offs, mas não estabelecem automaticamente uma prática universal.
- Exemplos são evidências a considerar, não instruções para copiar sem contexto do repositório.
- Use os acordos locais de arquitetura, qualidade/segurança e workflow como registro de decisões. Adicione referências quando informarem uma escolha real e registre essa escolha no acordo ou spec correspondente.
