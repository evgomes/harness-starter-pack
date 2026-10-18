# Contrato de hook: [nome do hook]

Use este template para projetar hook local ou de harness opcional. É um documento de planejamento neutro, não um formato universal de configuração. Traduza o comportamento acordado para a interface atual documentada pelo harness escolhido.

## Responsabilidade e suporte

- Status: Proposto / Ativo / Retirado
- Finalidade e responsável:
- Harnesses e versões suportados:
- Documentação oficial verificada em:
- Acordo de qualidade e segurança relacionado:

## Comportamento

- Gatilho e condições:
- Entradas disponíveis:
- Ação e escopo pretendidos:
- Fora do escopo:
- Comando manual equivalente:
- Contrapartida autoritativa em CI/outro processo:

## Contrato de runtime

- Runtime e versão:
- Sistemas operacionais suportados:
- Timeout:
- Códigos de saída e mensagens:
- Formato de saída e destino dos diagnósticos:
- Comportamento se faltar pré-requisito:
- Comportamento em timeout/erro interno:

## Segurança e confiabilidade

- Efeitos colaterais (arquivos, processos, rede, estado do repositório):
- A operação é idempotente?
- Concorrência / invocações repetidas:
- Dados enviados ou retidos:
- Segredos necessários e proteção:
- Configuração, instalação, atualização e remoção:
- Como desabilitar/contornar e limitações:

## Validação e adoção

- Validação em cada sistema operacional suportado:
- Comportamento esperado em sucesso, achado, pré-requisito ausente e falha:
- Mesclagem da configuração e confiança do usuário:
- Rollback / remoção:
- Limitações conhecidas:

Confirme eventos, esquema de entrada, permissões e comportamento da configuração na documentação oficial do harness antes de implementar. Não presuma que hooks compartilham esquema nem que instalar um framework seja adequado a todo repositório.