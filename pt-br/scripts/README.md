# Instalador do Harness Starter Pack

O instalador copia orientações em português para uma pasta de projeto nova ou para um repositório existente. Requer [Python 3.9 ou superior](https://www.python.org/downloads/), usa somente a biblioteca padrão e funciona no Windows, macOS e Linux. Ele não cria aplicações nem instala dependências de frameworks; use o gerador da própria stack para isso.

## Executar o assistente

Clone o repositório e execute o comando apropriado para seu terminal, a partir da raiz do clone:

| Plataforma / terminal | Comando |
|---|---|
| Windows PowerShell | `py -3 scripts/install.py` |
| Windows PowerShell sem o launcher `py` | `python scripts/install.py` |
| macOS / Linux | `python3 scripts/install.py` |

O assistente pergunta se deve criar uma pasta de projeto ou adicionar orientações a um repositório existente. Em seguida, solicita o caminho e permite escolher o idioma, os perfis de stack, os harnesses e as skills opcionais. Escolha **Português (Brasil)** para instalar este pacote. Em menus de escolha única, use as setas **para cima/baixo** e **Enter**. Em menus de múltipla seleção, use **para cima/baixo** para navegar, **Espaço** para marcar/desmarcar, **A** para alternar todos e **Enter** para confirmar. Use **Seta para a esquerda** para voltar e **Seta para a direita/Enter** para avançar. As escolhas são mantidas ao voltar. No prompt de caminho, digite **B** para voltar à escolha do destino ou pressione **Enter** para manter o caminho informado. Pressione **Q** para cancelar. Terminais sem suporte a menus interativos exibem escolhas equivalentes em texto. O destino deve ser válido e o idioma precisa estar disponível para avançar; stacks, harnesses e skills podem ficar sem seleção. Ao criar uma pasta nova, o assistente oferece executar `git init` após copiar os arquivos.

Adicione `--dry-run` para ver o plano sem criar o destino nem gravar arquivos. Adicione `--no-color` para desativar cores; a variável de ambiente padrão `NO_COLOR` também as desativa. As cores são usadas somente em terminais compatíveis e nunca são a única forma de transmitir informação.

## O que é instalado

- `AGENTS.md`, os cinco acordos (`architecture.md`, `dependencies.md`, `conventions.md`, `workflow.md` e `quality-and-security.md`), os templates comuns, as orientações/exemplos de hooks e os guias são sempre copiados.
- Um `HARNESS-README.md` é gerado na raiz do destino. Ele resume as stacks, os harnesses e as skills selecionados, apresenta uma lista de configuração específica para o projeto e inclui prompts de exemplo. A estrutura vem do [template de HARNESS-README](../docs/templates/harness-readme.md). Se esse arquivo já existir, vale o tratamento normal de conflito: ele é ignorado por padrão ou pode ser substituído após confirmação e backup.
- A biblioteca portátil de skills é copiada para `skills/`. Ela serve como catálogo de referência e não ativa automaticamente todas as skills em um harness.
- Os perfis de stack escolhidos são copiados para `stacks/`, e as orientações dos harnesses escolhidos para `harnesses/`. Consulte o [catálogo de stacks](../stacks/README.md) para conhecer os perfis e verificações candidatos. Para aplicações no mesmo repositório, escolha ASP.NET Core + React ou Spring Boot + Angular; cada bundle inclui orientações integradas e os dois perfis individuais. O instalador copia orientações e templates, não código de aplicação nem dependências de framework.
- `graphify` e `graphify-setup` vêm selecionadas por padrão no menu de skills e podem ser desmarcadas. As demais são opcionais; uma skill de apoio pode ser incluída automaticamente quando outra skill depende dela.
- As skills escolhidas são copiadas para as pastas de descoberta dos harnesses selecionados: `.agents/skills/` para Codex, Cursor e OpenCode; `.claude/skills/` para Claude Code. Se nenhum harness for escolhido, as skills permanecem somente na biblioteca portátil `skills/`. Algumas skills incluem outras skills referenciadas para manter os materiais relacionados disponíveis.
- O [catálogo de skills](../skills/README.md) resume cada skill, seu uso, os padrões do instalador e as dependências entre skills.
- Quando escolhidos, são incluídos regras do Cursor e configuração de exemplo do OpenCode. O Claude Code recebe um `CLAUDE.md` de entrada na raiz. O Codex usa o `AGENTS.md` compartilhado.

Depois da instalação, revise as instruções raiz e ajuste `docs/agreements/` ao projeto real. Se um arquivo já existir, o assistente o ignora por padrão. Ele pode fazer backup e substituí-lo individualmente após confirmação, armazenando o original em `.harness-starter-backups/<timestamp>/`. O instalador não exclui arquivos.

Comece pelo `HARNESS-README.md` gerado no destino. Complete e verifique os acordos do projeto, confirme que o harness descobre as instruções e skills, decida quais recomendações de ferramentas das stacks adotar e registre comandos reais de build, testes, lint e segurança antes de usar o workflow em mudanças de código. Quando `graphify-setup` estiver selecionada (padrão), conclua a configuração indicada pela skill e instale o CLI Graphify no ambiente de ferramentas da pessoa desenvolvedora. O CLI não é uma dependência da aplicação e o instalador do starter pack não o instala. Consulte também o [checklist pós-instalação](../../README.md#após-instalar-em-um-projeto).

O assistente não instala harnesses ou ferramentas, não baixa código remoto, não altera configurações globais, não cria código de aplicação, não altera remotes do Git e não sobrescreve arquivos existentes sem confirmação. Uma configuração de harness já existente pode conter ajustes próprios; avalie o backup e mescle os ajustes necessários à configuração instalada.

## Limitações

- Para projetos que usam mais de um harness, selecione cada um. Os arquivos compartilhados de skills podem ser copiados para mais de uma pasta de descoberta.
- A pasta `skills/` contém a biblioteca de referência. Uma skill pré-selecionada só fica disponível para descoberta quando um harness compatível com skills de projeto também é selecionado.
- As cores do terminal respeitam o suporte do terminal, `NO_COLOR` e `--no-color`; elas são decorativas e não carregam informação exclusiva.

## Alternativa manual

Consulte o [início rápido do pacote em português](../README.md) e copie somente os acordos, templates, perfil de stack, adaptador de harness e skills necessários. Mescle as instruções e configurações existentes do harness em vez de substituí-las sem revisão.
