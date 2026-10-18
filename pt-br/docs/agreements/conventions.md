# Convenções de engenharia

> Status: template inicial. Explicite escolhas do projeto; evite copiar regras que não se aplicam ao código existente.

## SOLID e design

- **Responsabilidade Única:** dê a cada módulo um motivo coeso para mudar; evite fragmentar código sem um limite real.
- **Aberto/Fechado:** estenda por abstrações estáveis quando variantes forem esperadas; não crie pontos de extensão especulativos.
- **Substituição de Liskov:** implementações preservam o contrato comportamental das abstrações.
- **Segregação de Interface:** mantenha contratos focados nas necessidades dos consumidores.
- **Inversão de Dependência:** mantenha políticas de alto nível independentes de infraestrutura substituível quando isso trouxer valor prático.

Aplique os princípios com discernimento. Prefira o design mais simples que mantenha responsabilidades claras e mudanças testáveis.

## Clean Code

- Use nomes que expressem a intenção do domínio; mantenha funções coesas e o fluxo de controle fácil de acompanhar.
- Torne estados inválidos difíceis de representar e valide entradas nos limites do sistema.
- Evite efeitos colaterais ocultos, regras duplicadas, indireção desnecessária e comentários que apenas repetem o código.
- Trate erros explicitamente; não ignore falhas nem use captura ampla sem uma razão para recuperação ou tradução.
- Alinhe código e testes aos padrões existentes, salvo quando mudar um padrão fizer parte do trabalho acordado.

## Convenções específicas do projeto

| Tópico | Convenção acordada | Justificativa / evidência |
|---|---|---|
| Nomenclatura e formatação | <regras e formatador> | <fonte> |
| Tratamento de erros | <contrato> | <fonte> |
| Logs/observabilidade | <campos, níveis, redação> | <fonte> |
| Testes | <estratégia e nomenclatura> | <fonte> |
| Contratos de API/interface/dados | <regras> | <fonte> |

## Segurança, privacidade e acessibilidade

Considere orientações OWASP e o modelo de ameaças aplicáveis. Para interfaces web, use a meta WCAG acordada e combine automação com verificações por teclado e tecnologia assistiva. Minimize dados pessoais; documente obrigações locais com responsáveis por privacidade/jurídico. Orientação genérica não determina conformidade.