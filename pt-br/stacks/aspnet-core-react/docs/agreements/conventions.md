# Prompts de convenções ASP.NET Core + React

Sugestões para repositório com ambas stacks. Mantenha somente o que se aplica e registre escolhas no acordo comum docs/agreements/conventions.md.

## Limites e contratos

- Mantenha tipos de domínio/aplicação do servidor independentes de DTO HTTP e modelos de interface, salvo geração deliberada de contratos.
- Mantenha mapeamento/transporte na fronteira ASP.NET Core. Componentes React focam apresentação/interação; comportamento cliente reutilizável fica em módulos explícitos.
- Valide entradas não confiáveis no servidor. Validação cliente pode espelhar regras para melhorar UX, nunca substituir servidor.
- Use nomes e serialização estabelecidos. Evite transformações implícitas difíceis de rastrear.

## Fluxos e falhas

- Explicite carregando, vazio, sucesso e erro; evite effects que dupliquem estado derivado ou escondam ciclo de requisição.
- Mapeie erros/validação do servidor para feedback claro e acessível. Não exponha stack traces, exceções internas ou dados sensíveis.
- Explicite retry, cancelamento, submissão duplicada e respostas obsoletas quando afetarem correção.
- Use HTML semântico, nomes acessíveis, teclado, foco visível, erros compreensíveis e reflow responsivo.

## Segurança e dados

- Trate estado/requisições do browser como não confiáveis. ASP.NET Core aplica autorização e propriedade do recurso em cada operação protegida.
- Siga autenticação documentada. Não armazene credenciais/segredos duradouros no browser/logs sem design explícito revisado.
- Minimize dados enviados à UI e remova segredos/tokens/dados pessoais desnecessários dos logs e relatórios.

## Mudanças e evidências

- Prefira slices verticais que entreguem comportamento coerente entre API/UI; coloque prova/experimento de compatibilidade necessário no Slice 1.
- Para mudanças entre stacks, identifique testes servidor, UI/componentes, contrato/integração e browser/ponta a ponta.
- Mantenha atualização de contrato API, tipos cliente e exemplos sincronizados na mesma mudança quando pertencem ao repositório.
- Antes de dependência nova em qualquer stack, siga acordo comum de dependências e revise manutenção, licença/termos, risco transitivo e vulnerabilidade.