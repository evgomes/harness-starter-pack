# Perfil de convenções ASP.NET Core

São sugestões padrão; mantenha somente convenções adequadas ao projeto e registre escolhas nos acordos comuns.

## Nomes e estrutura do código

- Prefira palavras de domínio completas a abreviações; mantenha termos locais e siglas padrão quando forem mais claros.
- Nomeie tipos pela responsabilidade de domínio, não pelo padrão de implementação, quando isso melhorar vocabulário compartilhado.
- Mantenha handlers pequenos: validar entrada, chamar comportamento e mapear saída. Regras de negócio ficam na lógica de aplicação/domínio.
- Use SOLID para responsabilidades coesas e dependências deliberadas. Evite abstrações, camadas e frameworks genéricos sem benefício demonstrado.
- Não esconda estado de domínio em números, strings ou booleanos mágicos; use tipos/nome explícitos.

## Async, cancelamento e persistência

- Use APIs assíncronas para I/O e propague CancellationToken em operações assíncronas por requisição quando suportado.
- Mantenha queries EF Core na camada de persistência; não retorne IQueryable para domínio/interface.
- Projete consultas ao caso de uso, selecione apenas campos necessários, evite acesso ao banco em loops e limite resultados crescentes.
- Use leitura no-tracking quando dados não forem alterados e o formato de query permitir.
- Trate migrações aplicadas como histórico imutável; crie nova migração para alterar schema.
- Centralize responsabilidade por timestamp e use UTC para instantes quando esse for o contrato. Registre estratégia de identidade/tenant/propriedade.

## Erros e logs

- Operação com falha deve retornar resposta de falha, não status de sucesso com indicador de falha. Use contrato HTTP acordado e códigos estáveis quando clients os interpretarem.
- Handlers centralizados tratam exceções inesperadas. Catch local deve recuperar, traduzir falha externa conhecida ou acrescentar contexto; evite catch-log-rethrow, captura silenciosa e captura ampla que esconda defeitos.
- Use logs estruturados com campos estáveis. Registre somente contexto necessário; remova credenciais, tokens, connection strings, chaves e dados pessoais desnecessários.
- Registre degradação/fallback tratado quando operador não conseguir explicar resultado parcial ou enganoso.

## Reflexão e comportamento dinâmico

Prefira tipos explícitos, interfaces, switches em conjuntos fechados e factories registradas. Use reflexão quando integração de framework ou teste de guarda baseado em forma justificar; documente por ser mais difícil de localizar/verificar estaticamente.

## Testes e pacotes

- Teste comportamento de negócio e invariantes relevantes, não plumbing do framework. Nomeie pelo comportamento comprovado.
- Não desative/fragilize teste só para build passar. Skip dependente de ambiente deve checar condição real e explicar como habilitar.
- Use integração quando regra depender de banco/provider/runtime real; isole dados/ambiente de desenvolvimento.
- Prefira recursos da plataforma antes de pacote novo. Confira finalidade, manutenção, licença/termos comerciais, risco transitivo e vulnerabilidades; atualize docs/agreements/dependencies.md.