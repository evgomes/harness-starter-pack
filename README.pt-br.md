# Harness Starter Pack

Uma coleção de instruções reutilizáveis, skills, templates e verificações para engenharia de software assistida por IA. Há pacotes completos em inglês e português do Brasil. Ambos incluem perfis para ASP.NET Core, React, Java + Spring Boot, Node.js + Express, Python + FastAPI e Angular, além de bundles para ASP.NET Core + React e Spring Boot + Angular no mesmo repositório.

## Pacotes

- [Pacote em português (Brasil)](pt-br/README.md)
- [English starter pack](en/README.md)

## Comece aqui

### Clone e instalação

Instale [Python 3.9 ou superior](https://www.python.org/downloads/), clone o repositório, entre na pasta e execute o instalador a partir da raiz:

```powershell
git clone https://github.com/evgomes/harness-starter-pack.git
cd harness-starter-pack
py -3 scripts/install.py
```

No macOS ou Linux, use `python3 scripts/install.py`; no Windows sem o launcher `py`, use `python scripts/install.py`. Revise a prévia e as escolhas antes de aplicar os arquivos. O [guia do instalador](scripts/README.md) explica a interação, as opções e o tratamento de conflitos.

### Use o pacote

Escolha o idioma no instalador e selecione as orientações comuns, o adaptador do harness e os perfis de stack aplicáveis no pacote desse idioma (`en/` ou `pt-br/`). O pacote em inglês instala os acordos em `docs/agreements/`; o pacote em português usa `docs/acordos/` e nomes de arquivo localizados. Preencha os acordos de arquitetura, dependências, convenções e qualidade/segurança com decisões verificadas; adapte o acordo reutilizável de workflow somente quando houver necessidades de processo documentadas. Selecione templates e skills adicionais conforme necessário. Mescle as instruções com os arquivos existentes do projeto em vez de substituir regras estabelecidas. Não copie prompts de acordos como se descrevessem um repositório que ainda não foi inspecionado.

O pacote também pode ser consultado diretamente por um agente. Comece pelo `AGENTS.md` no pacote do idioma escolhido e carregue skills específicas somente quando forem pertinentes.

Para aplicar qualquer pacote de idioma de forma interativa a um projeto novo ou existente, use o [instalador multiplataforma](scripts/README.md). Ele usa apenas a biblioteca padrão do Python e oferece uma prévia com `--dry-run`.

O instalador sempre inclui os cinco acordos comuns, templates compartilhados, orientações e exemplos de hooks, guias e a biblioteca portátil de referência de skills no idioma escolhido. Ele também gera `HARNESS-README.md` na raiz do destino com um resumo dos ativos selecionados, passos de configuração e prompts de exemplo. Perfis de stack são opcionais. Se as duas aplicações estiverem no mesmo repositório, escolha ASP.NET Core + React ou Spring Boot + Angular; cada bundle inclui orientações integradas e os dois perfis individuais. Consulte os catálogos de [stacks em inglês](en/stacks/README.md) ou [português](pt-br/stacks/README.md). `graphify` e `graphify-setup` vêm pré-selecionadas como skills; escolha um harness para tornar as skills selecionadas descobríveis por ele. Consulte os catálogos de [skills em inglês](en/skills/README.md) ou [português](pt-br/skills/README.md). O instalador não instala Graphify nem dependências da aplicação.

### Depois de instalar em um projeto

Use o `HARNESS-README.md` gerado no projeto de destino como checklist de configuração para a pessoa desenvolvedora. O [template de HARNESS-README](pt-br/docs/templates/readme-do-harness.md) mostra sua estrutura. Antes de usar o workflow:

1. Confirme se os perfis de stack, adaptadores de harness, skills e caminhos de descoberta listados correspondem à configuração desejada. Resolva conflitos exibidos na prévia; arquivos existentes são ignorados por padrão, salvo autorização explícita para backup e substituição.
2. Inspecione o código, manifests, CI e configuração de implantação do projeto. Preencha `docs/acordos/arquitetura.md`, `docs/acordos/dependencias.md`, `docs/acordos/convencoes.md` e `docs/acordos/qualidade-e-seguranca.md` com decisões verificadas. Mantenha `docs/acordos/workflow.md` como padrão reutilizável, salvo necessidade documentada do projeto.
3. Revise cada perfil selecionado e decida quais recomendações de arquitetura e convenções se aplicam. Escolha bibliotecas e versões reais e defina comandos de build, testes, lint, segurança e qualidade a partir do próprio projeto. O instalador copia recomendações; não instala pacotes de framework, linters ou ferramentas de teste.
4. Confirme se o harness escolhido descobre as instruções e skills instaladas. Revise e mescle a configuração do harness com as configurações existentes do projeto.
5. Se `graphify-setup` estiver selecionada (padrão do instalador), siga `skills/configuracao-do-graphify/SKILL.md` e confirme que o CLI Graphify está instalado no ambiente de ferramentas da pessoa desenvolvedora. O CLI é uma ferramenta de desenvolvimento; o starter pack não o instala.
6. Para mudanças substanciais, comece pelo template de spec comum ou da stack e defina critérios de aceitação e evidências de verificação. Use o Slice 1 para validar premissas que precisem de prova; depois execute os slices restantes em ordem, um subitem por vez.
7. Execute as verificações de base acordadas e registre os comandos e resultados reais antes de considerar a configuração do harness concluída.

O `HARNESS-README.md` gerado resume as seleções específicas e aponta para os documentos dos perfis correspondentes. O [guia de início rápido em português](pt-br/README.md) e o [guia do instalador](scripts/README.md) detalham os ativos e o comportamento do instalador.

Para conhecer a justificativa e as referências das recomendações de workflow e dos perfis de stack, consulte [Referências e justificativas](pt-br/REFERENCIAS.md).

Para verificações visuais em aplicações web, consulte o [guia de testes em navegador](pt-br/guias/testes-de-navegador.md) e a skill opcional de [validação visual no navegador](pt-br/skills/validacao-visual-no-navegador/SKILL.md).

## Princípios de design

- Um conjunto compartilhado de acordos de engenharia, com adaptadores de harness enxutos.
- Skills para fluxos opcionais e instruções concisas para regras duráveis.
- Evidências antes de conclusões, especialmente em revisão de código e segurança.
- Configuração multiplataforma sempre que viável, com comandos específicos de plataforma documentados.
- Brainstorming é opcional; spec ou implementação direta são válidas quando a solução já estiver clara.

## Licença

Este repositório está licenciado sob a [licença MIT](LICENSE).
