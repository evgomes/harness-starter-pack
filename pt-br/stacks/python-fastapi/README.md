# Perfil Python + FastAPI

Orientações de backend API-first em Python com FastAPI. Confira faixa Python, servidor ASGI, gerenciador de dependências, banco e implantação no projeto. Instalador copia orientação, não ferramentas.

## Arquitetura e convenções

- Em serviços maiores, agrupe endpoints relacionados em módulos APIRouter e faça composição explícita. Separe transporte/rotas das regras de domínio quando útil.
- Use injeção de dependência FastAPI para recursos compartilhados, autenticação/autorização e serviços por requisição; prefira declarações Annotated tipadas compatíveis com a faixa Python usada.
- Defina/valide esquemas de entrada e saída; não retorne objetos de persistência ou campos sensíveis por acidente.
- Delimite async/sync intencionalmente. Handlers async para I/O assíncrono; evite bloquear event loop com I/O ou CPU síncronos.
- Trate OpenAPI gerado como contrato a revisar; documente autenticação/erros e teste autorização por objeto e ação.

## Verificações candidatas

| Área | Opção |
|---|---|
| Testes unitários/API | pytest com FastAPI TestClient (baseado em HTTPX); suporte async para comportamento realmente assíncrono. |
| Lint/formatação | Ruff. Configure regras conforme política, sem ativar tudo cegamente. |
| Tipos | mypy ou verificador escolhido pelo projeto; annotations FastAPI não provam todo comportamento de runtime/tipos. |
| Integração/segurança | Testes com banco quando necessário, auditoria de avisos/dependências, secret scan e testes de autorização/permissão/entrada/limites. |

FastAPI é o perfil existente. Django REST Framework pode servir quando ORM/admin/ecossistema Django forem úteis; requer perfil e decisões próprios.

## Templates e referências

Veja [templates](docs/templates/README.md) para spec API/verificação e o [modelo comum de ameaças](../../docs/templates/modelo-de-ameacas.md).

- [Aplicações maiores FastAPI](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [Dependências FastAPI](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Testes FastAPI](https://fastapi.tiangolo.com/tutorial/testing/)
- [Segurança FastAPI](https://fastapi.tiangolo.com/tutorial/security/)
- [Implantação FastAPI](https://fastapi.tiangolo.com/deployment/concepts/)
- [Ruff](https://docs.astral.sh/ruff/) e [mypy](https://mypy.readthedocs.io/en/stable/)
