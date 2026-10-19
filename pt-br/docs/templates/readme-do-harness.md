# Visão geral da configuração do harness

Este projeto recebeu orientações de engenharia assistida por IA do Harness Starter Pack conforme as escolhas feitas na instalação. O documento resume os ativos instalados e o que configurar antes de usar o fluxo. O instalador não instala frameworks, dependências de aplicação, produtos de harness ou ferramentas externas.

No uso manual, substitua marcadores {{...}} pelos ativos escolhidos e remova seções inaplicáveis. O instalador preenche essas seções.

## Resumo da instalação

{{INSTALLATION_SUMMARY}}

### Orientações compartilhadas

- [AGENTS.md](AGENTS.md): instruções compartilhadas e ponto de entrada do workflow.
- [Acordos](docs/acordos/README.md): arquitetura, dependências, convenções, workflow e qualidade/segurança. Preencha acordos locais antes de considerar recomendações como decisões.
- [Templates](docs/templates/README.md): specs, planos de verificação, modelos de ameaças, handoffs e artefatos opcionais.
- hooks/ e guias/: orientações e exemplos opcionais; hooks não são habilitados silenciosamente.
- skills/: biblioteca portátil. Somente skills escolhidas são copiadas para descoberta pelo harness.

### Perfis de stack escolhidos

{{STACK_PROFILES}}

### Harnesses escolhidos

{{HARNESSES}}

### Skills escolhidas

{{SKILLS}}

## Checklist antes do uso regular

1. Leia este arquivo, AGENTS.md e os adaptadores listados. Confirme como o agente descobre instruções e skills.
2. Inspecione estrutura, manifests, CI, implantação e convenções reais. Preencha arquitetura, dependências, convenções e qualidade/segurança em docs/acordos/ com decisões verificadas. Mantenha workflow compartilhado como padrão, adaptando somente processos documentados.
3. Revise cada perfil e prompts de arquitetura/convenções. Decida o que se aplica, registre decisões nos acordos raiz e vincule documentos que forem mantidos.
4. Defina bibliotecas/versões, comandos de build/teste, linters, verificações de segurança/dependências e barreiras de CI conforme o projeto. Recomendações não são ferramentas instaladas.
5. Se configuração do Graphify estiver selecionada, conclua skills/configuracao-do-graphify/SKILL.md e instale CLI no ambiente da pessoa desenvolvedora. É ferramenta de desenvolvimento, não dependência de aplicação; instalador copia instruções, não o CLI.
6. Antes de mudança substancial, use spec comum ou da stack. Se premissa exigir prova, Slice 1 é prova; depois siga os demais em ordem, um subitem por vez. Registre verificações focadas e suíte completa ao fim.

### Acompanhamento por stack

{{STACK_SETUP}}

## Prompts de exemplo

> Leia HARNESS-README.md, AGENTS.md e acordos aplicáveis. Inspecione manifests e CI reais. Informe itens pendentes do checklist; não trate recomendações de perfis como decisões adotadas.

> Quero implementar [funcionalidade]. Inspecione código e acordos concluídos. Elabore uma spec com template pertinente, identifique premissas que exigem prova e proponha slices ordenados com aceitação/verificação. Não implemente até eu revisar a spec.

Para mudança pequena e clara, siga o caminho leve do workflow.

## Manutenção

Atualize este overview quando harnesses, skills, stacks ou decisões de configuração mudarem. Se arquivo existente colidir, o instalador o ignora salvo aprovação para backup/substituição. Revise a prévia e mescle overview com conteúdo local.
