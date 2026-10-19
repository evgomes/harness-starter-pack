# Prompts de arquitetura Spring Boot + Angular

Registre decisões verificadas no acordo comum de arquitetura. Use somente para repositórios que compartilham API e interface.

- Qual aplicação é responsável por cada regra/dado? Autorização e validação que protegem dados ficam no servidor.
- Qual schema, versionamento/compatibilidade, formato de erro e política de client conecta Angular ao Spring Boot?
- Como ambientes, origens/CORS, TLS, cookies/tokens, CSRF, segredos e URLs de serviço são configurados?
- Como a UI representa validação do servidor, expiração de autenticação, permissão negada, estados vazio/carregando/erro e retry?
- Quais testes fornecem integração API e evidência browser ponta a ponta? Onde rodam na CI?
- Quais mudanças backend/frontend precisam de implantação conjunta e qual janela de compatibilidade é necessária?
