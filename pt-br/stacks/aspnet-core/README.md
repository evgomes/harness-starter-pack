# Perfil ASP.NET Core

Orientações de backend para projetos ASP.NET Core. São ponto de partida, não premissas sobre todo projeto: verifique o repositório, registre decisões aceitas nos acordos e adapte ao produto real.

## Uso com outros perfis

Escolha para backend ASP.NET Core. Se o mesmo repositório também tiver frontend React e precisar de orientação integrada de arquitetura, convenções e spec, escolha ASP.NET Core + React. Mantenha contratos API/interface e decisões compartilhadas em docs/agreements/architecture.md.

## Arquitetura e convenções

- [Perfil de arquitetura](docs/agreements/architecture.md)
- [Perfil de convenções](docs/agreements/conventions.md)
- Mantenha atualizado o [acordo de dependências](../../docs/agreements/dependencies.md).
- Use [templates da stack](docs/templates/README.md) para specs de API/domínio, plano de verificação e prompts de ameaças.

## Verificações candidatas

Confirme comandos no SDK, solução e CI instalados.

| Área | Verificação candidata |
|---|---|
| Formatação | dotnet format --verify-no-changes |
| Build | dotnet build <solução-ou-projeto> |
| Testes | dotnet test <solução-ou-projeto-de-testes>; focados nos slices e suíte completa ao fim da spec |
| Auditoria de vulnerabilidades | dotnet package list --include-transitive --vulnerable (confirme suporte do SDK/fontes de pacote) |

A listagem consulta dados de auditoria configurados; verifique suporte da fonte e saída antes de interpretar resultado vazio. Consulte a [referência Microsoft](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-list).