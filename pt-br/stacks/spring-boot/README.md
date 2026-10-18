# Perfil Java + Spring Boot

Orientações para backend Java com Spring Boot. Trate as escolhas como candidatas: confirme versões Java/Spring, Maven/Gradle, CI e implantação. Instalador copia somente orientação.

## Arquitetura e convenções

- Mantenha classe de entrada em pacote acima dos componentes para delimitar component scanning. Agrupe por domínio/funcionalidade quando fizer sentido; não imponha número fixo de camadas.
- Prefira injeção por construtor e dependências explícitas. Separe controllers HTTP de regras de negócio e persistência quando melhorar testes.
- Use configuração Spring externalizada para valores por ambiente; mantenha segredos no armazenamento de segredos da implantação.
- Considere Spring Modulith somente quando limites modulares explícitos resolverem problema real; não é obrigatório.
- Use validação e segurança Spring nos limites de confiança; defina autorização por recurso/ação e teste-a.

## Verificações candidatas

| Área | Opção |
|---|---|
| Testes unitários/slices | JUnit Jupiter, AssertJ e Spring Boot Test; prefira slices focados quando contexto completo não for necessário. |
| HTTP/API/integração | Spring MVC/WebFlux Test; Testcontainers opcional se depender de banco, broker ou serviço real. |
| Formatação/lint | Checkstyle para regras acordadas; Spotless opcional se desejado. Siga plugins Maven/Gradle existentes. |
| Análise/dependências | Warnings de compilador, análise estática escolhida e auditoria de vulnerabilidade/licença. |
| Runtime/operação | Endpoints Spring Boot Actuator somente quando necessários, com exposição/autorização configuradas. |

São opções, não stack obrigatória. Derive comandos dos wrappers Maven/Gradle e CI. Não exponha endpoints de saúde/gestão publicamente por padrão.

## Templates e referências

Veja [templates](docs/templates/README.md) para spec Java/Spring e plano de verificação. Use [modelo de ameaças](../../docs/templates/threat-model.md) e [plano comum](../../docs/templates/verification-plan.md) quando melhor.

- [Testes Spring Boot](https://docs.spring.io/spring-boot/reference/testing/)
- [Estruturação de código](https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html)
- [Configuração externalizada](https://docs.spring.io/spring-boot/reference/features/external-config.html)
- [Actuator](https://docs.spring.io/spring-boot/reference/actuator/index.html)
- [Spring Modulith](https://docs.spring.io/spring-modulith/reference/)
- [Checkstyle](https://checkstyle.org/) e [Testcontainers Java](https://java.testcontainers.org/)