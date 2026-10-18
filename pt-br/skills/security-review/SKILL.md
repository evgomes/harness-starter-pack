---
name: security-review
description: Faça revisão de segurança orientada por ameaças contra acordos do projeto e orientação OWASP aplicável. Combine ferramentas determinísticas; relate riscos concretos com evidências e sem alegar certificação.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Revisão de segurança

1. Leia modelo de ameaças, acordos de arquitetura/segurança, spec e regras de privacidade pertinentes. Identifique ativos, atores, limites de confiança, pontos de entrada e fluxos de dados.
2. Inspecione diff e caminhos relevantes quanto a autenticação/autorização, validação, injeção, codificação de saída, SSRF, desserialização, arquivos, criptografia/segredos, cadeia de suprimentos, logs, esgotamento de recursos e exposição de erros.
3. Em APIs, verifique autorização no servidor em cada operação protegida e escopo do objeto/dado. Considere código React do navegador não confiável; nunca coloque segredo de servidor no bundle.
4. Execute somente scanners/testes aprovados pelo projeto. Registre escopo, versão, atualidade da fonte, resultados exatos e lacunas. Scanner limpo não prova segurança.
5. Relate achados com cenário de exploração, limite afetado, impacto, evidência (caminho:linha/saída), justificativa de severidade e correção. Separe defeitos confirmados de hipóteses.