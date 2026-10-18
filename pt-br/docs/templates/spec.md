# Especificação de funcionalidade: <título>

> Status: Rascunho | Aceita | Em andamento | Concluída
> Responsável: <nome/equipe> · Data: <AAAA-MM-DD> · Branch: <branch conforme o repositório> · Exploração/handoff relacionado: <links>

Antes de redigir, inspecione as instruções do repositório e crie ou troque para a branch exigida pelas convenções Git. Confirme branch e estado de trabalho. A pessoa responsável deve revisar e ajustar os critérios de aceitação antes de aceitar esta spec e iniciar a implementação.

## 1. Problema e resultado

- Problema / necessidade:
- Resumo: Como <usuário/ator>, quero <capacidade> para <resultado>.
- Resultado pretendido:
- Por que agora:

## 2. Escopo

### Dentro do escopo
-

### Fora do escopo
-

## 3. Contexto e restrições

- Comportamento/arquitetura existentes relevantes:
- Referências (caminho/linha, issue ou decisão):
- Dependências e restrições:
- Fatos confirmados:
- Premissas a comprovar:

## 4. Requisitos e critérios de aceitação

| ID | Requisito / cenário | Evidência de aceitação |
|---|---|---|
| AC-01 | Dado … quando … então … | <teste, inspeção ou verificação manual> |

## 5. Design e decisões

- Design e limites propostos:
- Alternativas e trade-offs:
- Decisões aceitas e responsável:
- Perguntas em aberto / bloqueios:
- Modelo de dados, invariantes, semântica de valores nulos e migração/rollback (se aplicável):
- Compatibilidade de API/interface e comportamento de erros (se aplicável):

## 6. Segurança, privacidade, acessibilidade e operação

- Ameaças, autorização, validação de entrada, segredos e redação de logs:
- Dados pessoais e retenção/consentimento:
- Requisitos de acessibilidade e verificações manuais:
- Observabilidade, falhas, desempenho, implantação/recuperação:
- Itens não aplicáveis e motivo:

## 7. Provas e slices de implementação

Se alguma premissa precisar ser comprovada antes de confiar no plano, faça dessa prova o Slice 1. Caso contrário, Slice 1 é o primeiro slice de entrega. Os slices e seus subitens são estritamente sequenciais: não inicie outro slice antes de concluir e evidenciar todos os subitens atuais. Atualize status e handoff após cada item.

| Slice / subitem | Descrição e arquivos/contratos sob responsabilidade | Evidência de aceitação | Status | Evidência / observação |
|---|---|---|---|---|
| 1.1 | <prova ou primeiro item de entrega> | | Não iniciado | |
| 1.2 | <próximo item deste slice, se necessário> | | Não iniciado | |
| 2.1 | <inicie somente após concluir todos os itens do Slice 1> | | Não iniciado | |

## 8. Riscos e dependências

| Risco/dependência | Probabilidade/impacto | Mitigação ou decisão necessária | Responsável |
|---|---|---|---|

## 9. Verificação e release

- Testes e verificações focados por slice/subitem (registre resultados antes de avançar):
- Suíte completa a executar uma vez após todos os slices:
- Outras verificações exigidas antes da entrega conforme acordos:
- Verificações manuais / ambientes:
- Migração de dados e implantação/rollback:
- Uma revisão adversarial ao final contra a spec completa e o diff final; use modelo forte quando disponível ou revisão manual pela pessoa responsável:

## 10. Aditivos

Não altere silenciosamente o plano aceito. Registre desvios e obtenha decisão antes de implementar. Se aceitos, atualize escopo, critérios, ordem dos slices e evidências. Instruções autorizadas do desenvolvedor podem ser registradas como fonte da decisão.

| ID / data | Desvio proposto e motivo | Impacto no escopo / slices / aceitação / evidências | Decisão e fonte | Status |
|---|---|---|---|---|

## 11. Revisão dos critérios de aceitação

- [ ] A pessoa responsável revisou e ajustou os critérios.
- [ ] Os critérios são observáveis e têm plano de evidências.
- [ ] A pessoa responsável aceitou a spec antes da implementação.

## 12. Registro de alterações

| Data | Alteração | Responsável/fonte da decisão |
|---|---|---|