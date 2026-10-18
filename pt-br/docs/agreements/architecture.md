# Acordo de arquitetura

> Status: template inicial. Substitua cada pergunta por fatos verificados neste repositório.

## Objetivo e escopo

- Objetivo do produto/sistema: <o que o sistema faz>
- Usuários e fluxos principais: <quem usa e como>
- Fora do escopo: <exclusões explícitas>

## Stack de tecnologia

| Área | Tecnologia e política de versões | Evidência / local |
|---|---|---|
| Backend/API | <framework, runtime, pacotes principais> | <arquivos de solução/projeto> |
| Frontend | <framework, linguagem, sistema de build> | <manifest/configuração> |
| Dados | <banco, persistência, migrações> | <configuração/esquema> |
| Hospedagem/implantação | <runtime, contêineres, nuvem/local> | <arquivos de implantação> |
| Testes e qualidade | <ferramentas de teste, lint e análise> | <scripts/configuração> |

## Contrato de arquitetura

Descreva componentes, responsabilidades e direções de dependência permitidas. Inclua diagrama/link quando útil. Registre limites que devem permanecer válidos, não uma lista genérica de padrões.

- <componente> é responsável por <responsabilidade>.
- <componente> pode depender de <limite>; não pode depender de <limite>.
- Interfaces/contratos públicos são definidos em <local>.
- Responsabilidade pelos dados, limites transacionais e política de migração: <decisão>.
- Autenticação, autorização e isolamento entre usuários/tenants/dados: <decisão>.

## Atributos de qualidade e restrições

Registre metas e decisões relevantes de disponibilidade, desempenho, escalabilidade, observabilidade, acessibilidade, privacidade, segurança, compatibilidade e implantação. Marque itens pendentes como perguntas em aberto em vez de inventar metas.

## Processo de mudança

Mudanças arquiteturais exigem justificativa breve, alternativas, contratos afetados, impactos de migração/implantação e atualização deste acordo quando o design aceito mudar.