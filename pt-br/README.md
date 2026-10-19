# Pacote de Harnesses

Coleção de instruções reutilizáveis, skills, templates e verificações para engenharia de software assistida por IA. O pacote em português do Brasil inclui perfis de ASP.NET Core, React, Java + Spring Boot, Node.js + Express, Python + FastAPI e Angular, além de bundles ASP.NET Core + React e Spring Boot + Angular para repositórios compartilhados.

## Início rápido

Para instalar o pacote em português em projeto novo ou existente, instale [Python 3.9 ou superior](https://www.python.org/downloads/), clone este repositório e execute o instalador:

```powershell
git clone https://github.com/evgomes/harness-starter-pack.git
cd harness-starter-pack
py -3 scripts/install.py
```

No macOS/Linux, use `python3 scripts/install.py`; no Windows sem o launcher `py`, use `python scripts/install.py`. O assistente permite adicionar orientações a um repositório existente ou criar uma pasta de projeto. Selecione **Português (Brasil)** na etapa de idioma. O instalador usa somente a biblioteca padrão do Python.

Para aplicação manual, leia [AGENTS.md](AGENTS.md), o [índice de acordos](docs/acordos/README.md), escolha harnesses e stacks no catálogo e copie apenas o que precisa. O pacote também foi pensado para ser consultado diretamente pelo agente; carregue skills específicas somente quando forem pertinentes.

## Conteúdo e instalação

O instalador sempre copia `AGENTS.md`, os cinco acordos, templates comuns, orientações e exemplos de hooks, guias e biblioteca portátil de skills. Gera `HARNESS-README.md` na raiz do destino com os ativos escolhidos, um checklist de configuração e prompts de exemplo. Perfis de stack são opcionais; escolha um bundle quando ambas as aplicações estiverem no mesmo repositório. Consulte o [catálogo de stacks](stacks/README.md), o [catálogo de skills](skills/README.md) e o [guia do instalador em português](scripts/README.md).

As skills `graphify` e `configuração do Graphify` vêm pré-selecionadas. Escolha ao menos um harness para instalar as skills na pasta de descoberta; sem harness, elas permanecem apenas na biblioteca de referência. A skill `configuração do Graphify` exige instalar o CLI Graphify no ambiente de ferramentas da pessoa desenvolvedora. O instalador copia a skill, mas não instala o Graphify nem dependências da aplicação.

## Após instalar em um projeto

Use HARNESS-README.md gerado no destino como checklist de configuração para a pessoa desenvolvedora. Conclua os passos antes de usar o workflow:

1. Confirme os perfis de stack, adaptadores, skills e caminhos de descoberta selecionados. Resolva os conflitos da prévia; arquivos existentes são ignorados por padrão, salvo autorização explícita para backup e substituição.
2. Inspecione o código, os manifests, a CI, a implantação e as convenções. Preencha `docs/acordos/arquitetura.md`, `docs/acordos/dependencias.md`, `docs/acordos/convencoes.md` e `docs/acordos/qualidade-e-seguranca.md` com decisões verificadas. Mantenha `docs/acordos/workflow.md` como padrão reutilizável, salvo necessidade documentada do projeto.
3. Revise os perfis. Decida quais recomendações se aplicam, escolha bibliotecas e versões e defina comandos reais de build, testes, lint, segurança e qualidade. O instalador copia recomendações; não instala frameworks, ferramentas ou pacotes.
4. Confirme que o harness escolhido descobre as instruções e skills. Mescle sua configuração com os arquivos existentes em vez de substituí-los sem revisão.
5. Se `configuração do Graphify` estiver selecionada (padrão), siga `skills/configuracao-do-graphify/SKILL.md` e instale o CLI Graphify no ambiente de ferramentas da pessoa desenvolvedora. Registre a versão em `docs/acordos/dependencias.md`.
6. Para mudanças substanciais, comece pelo template de spec comum ou da stack e defina critérios de aceitação e evidências de verificação. Use o Slice 1 para provas quando uma premissa precisar de validação; execute os slices seguintes em ordem, subitem por subitem.
7. Execute as verificações de base acordadas e registre os comandos e resultados reais.

O [template de HARNESS-README](docs/templates/readme-do-harness.md) mostra sua estrutura. O [guia do instalador](scripts/README.md) explica as escolhas, os conflitos e as limitações. Consulte [referências e justificativas](REFERENCIAS.md) para conhecer as fontes das recomendações.

## Princípios

- Um conjunto compartilhado de acordos de engenharia, com adaptadores enxutos.
- Skills para fluxos opcionais e instruções concisas para regras duráveis.
- Evidências antes de conclusões, especialmente em revisão de código e segurança.
- Configuração multiplataforma quando viável.
- Brainstorming é opcional; spec ou implementação direta são válidas quando a solução estiver clara.

## Licença

Este repositório está licenciado sob a [licença MIT](../LICENSE).
