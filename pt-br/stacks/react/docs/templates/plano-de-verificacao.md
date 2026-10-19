# Plano de verificação React: [mudança]

> Spec: [link] · Responsável: [nome/equipe] · Versões React/framework: [verificadas]

Use com o [plano comum](../../../../docs/templates/plano-de-verificacao.md). Derive comandos de scripts/lockfile; não presuma npm, bundler, framework de teste nem instale ferramentas apenas pelo template.

Execute verificações focadas por slice e registre plano/handoff antes de avançar. Deixe suíte completa para após todos os slices, salvo exigência aceita. Faça uma revisão adversarial ao final.

## Evidência específica da mudança

| Requisito/jornada | Evidência necessária | Resultado/link | Status |
|---|---|---|---|
| Fluxo principal | | | Não executado |
| Estados carregando/vazio/erro/retry | | | Não executado |
| Contrato API e validação servidor | | | Não executado |
| Teclado e tecnologia assistiva | | | Não executado |

## Build e código

| Verificação | Comando/ponto candidato | Notas |
|---|---|---|
| Formatação | Script existente | Use config do projeto |
| Lint/análise | Script existente | Separe baseline de novos achados |
| Tipos | Typecheck se TypeScript | Diagnóstico do editor não prova tipos |
| Build produção | Script existente | Registre ambiente e warnings/erros |
| Testes unitários/componentes | Script focado | Cubra transições/validação/comportamento |
| Integração/browser | Comando existente | Roteamento, API e browser pertinente |

## Acessibilidade e segurança

| Preocupação | Evidência | Resultado/link | Status |
|---|---|---|---|
| Elementos semânticos, nomes, labels e relação de erro | DOM/testes/automação aplicável | | Não executado |
| Teclado, ordem/visibilidade/gestão de foco | Teste manual e focado | | Não executado |
| Zoom/reflow, contraste e responsividade | Browser em condições alvo | | Não executado |
| Anúncios dinâmicos de status/erro | AT ou evidência manual/automática | | Não executado |
| Autorização servidor | Confirmar enforcement API; route guards não são segurança | | Não executado |
| XSS, HTML/URLs inseguros e dados browser | Revisão/testes focados | | Não executado |
| Dependências e segurança de código | Comando aprovado, data/escopo | | Não executado |

Automação detecta somente parte dos problemas. Registre evidência manual para interação/AT quando a meta exigir.

## Release e lacunas

- Verificações exigidas pelo acordo de qualidade/segurança:
- Verificações não executadas e motivo:
- Browsers/dispositivos e limitações:
- Exceção de risco, se houver:

Status permitidos: Aprovado, Falhou, Ignorado, Não executado ou Não aplicável.
