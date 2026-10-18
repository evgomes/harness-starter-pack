# Perfil ASP.NET Core + React

Use quando backend ASP.NET Core e frontend React estiverem no mesmo repositório e uma mudança puder cruzar seus limites. Acrescenta orientação integrada e templates full stack. A seleção no instalador inclui também os perfis individuais. Não gera aplicação nem instala dependências.

O instalador coloca este perfil em stacks/aspnet-core-react/. Escolha-o em vez de selecionar ambos perfis individuais; eles serão incluídos junto com o combinado. O perfil combinado foca decisões compartilhadas API/interface. Confira cada orientação no projeto antes de adotar.

## Acordos

- [Prompts integrados de arquitetura](docs/agreements/architecture.md): contratos API/interface, limites de confiança, dados e implantação.
- [Convenções integradas](docs/agreements/conventions.md): mudanças entre backend e frontend.
- Mantenha autoritativos os acordos compartilhados de [arquitetura](../../docs/agreements/architecture.md), [convenções](../../docs/agreements/conventions.md), [dependências](../../docs/agreements/dependencies.md) e [qualidade/segurança](../../docs/agreements/quality-and-security.md).

## Templates

- [Spec full stack](docs/templates/spec.md) para mudanças visíveis que cruzam API/interface.
- [Plano de verificação full stack](docs/templates/verification-plan.md) para evidências backend, frontend, contrato e ponta a ponta.
- Use templates comuns de [spec](../../docs/templates/spec.md), [verificação](../../docs/templates/verification-plan.md) e [ameaças](../../docs/templates/threat-model.md) quando forem mais adequados.

## Verificações candidatas

Escolha comandos da solução, manifests, scripts, CI e implantação reais. Evidências típicas: build/testes .NET focados, typecheck/lint/build/testes de componentes, contratos de API e fluxo no browser/ponta a ponta. Não presuma gerenciador, versão ou ferramenta de teste apenas com base no perfil.