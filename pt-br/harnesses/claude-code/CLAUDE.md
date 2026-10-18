# Adaptador de projeto Claude Code

No início de cada tarefa, leia AGENTS.md da raiz e os arquivos relevantes de docs/agreements/ como contrato compartilhado de engenharia. Mantenha este arquivo como ponto de entrada curto para Claude Code; não duplique os acordos completos.

Ao instalar o starter pack, copie skills escolhidas para .claude/skills/<nome-da-skill>/ e preserve referências, assets e scripts. Leia uma skill somente quando a tarefa corresponder à descrição. Configure hooks apenas para verificações determinísticas e com falha clara; revisão por IA deve permanecer como fluxo explícito.

O hook opcional de início de sessão do Graphify tem configurações PowerShell e Bash em ../../hooks/adapters/. Instale script/configuração compatível somente se o projeto usar Graphify: Bash e Python 3.9+ no macOS/Linux ou PowerShell 7 no Windows. Siga ../../hooks/README.md e ../../skills/graphify/SKILL.md para verificar/atualizar índice.

Antes de implementar, inspecione instruções e acordos aplicáveis. Brainstorming é opcional; use somente se esclarecer problema ou comparar soluções agregar valor. Atualize o handoff quando o trabalho pausar ou mudar de responsável.

Referências oficiais: [memória Claude Code](https://code.claude.com/docs/en/memory), [skills](https://code.claude.com/docs/en/skills) e [hooks](https://code.claude.com/docs/en/hooks).