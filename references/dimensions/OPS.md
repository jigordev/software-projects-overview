# OPS — Entrega, implantação e operação

**Agente responsável:** `operations-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| OPS-01 | Build reproduzível | Build é previsível e repetível. |
| OPS-02 | Ambientes | Ambientes são separados adequadamente. |
| OPS-03 | Configuração externa | Configurações não ficam fixadas indevidamente no código. |
| OPS-04 | Gerenciamento de segredos | Segredos são injetados e armazenados com segurança. |
| OPS-05 | CI | Integração contínua executa verificações relevantes. |
| OPS-06 | CD | Entrega é controlada e rastreável quando aplicável. |
| OPS-07 | Quality gates | Alterações passam por verificações obrigatórias. |
| OPS-08 | Containers | Imagens e containers têm configuração adequada quando aplicável. |
| OPS-09 | Privilégios operacionais | Processos executam com privilégio mínimo necessário. |
| OPS-10 | Health checks | Serviços possuem verificações operacionais. |
| OPS-11 | Graceful deployment | Atualizações não interrompem operações indevidamente. |
| OPS-12 | Rollback | Existe estratégia de reversão. |
| OPS-13 | Versionamento | Versões publicadas são rastreáveis. |
| OPS-14 | Configuração de recursos | Limites de CPU, memória e recursos são controlados. |
| OPS-15 | Infraestrutura como código | Infraestrutura é reproduzível quando aplicável. |
| OPS-16 | Recuperação de desastres | Existe estratégia de continuidade e recuperação proporcional ao risco. |

## Instruções de inspeção

- Avalie cada critério OPS aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
- Adapte a técnica à linguagem, framework, arquitetura e domínio encontrados.
- Não presuma que uma prática é obrigatória quando o contexto não a exige.
- Para cada critério, registre estado: `assessed`, `not_assessed` ou `not_applicable`.
- Para critérios avaliados, atribua nota 0–5 somente quando houver evidência suficiente.
- Emita achado apenas quando houver deficiência concreta e impacto técnico explicável.
- Use exatamente o código da tabela. Não crie códigos derivados.
- Informe arquivo e linha/faixa quando possível; para configuração/infraestrutura, informe caminho e chave/recurso.
- Mantenha cada achado conciso: uma frase para problema e uma frase para correção mínima.
- Não repita achado já coberto por outra dimensão; indique relação cruzada se necessário.

## Evidências apropriadas

- Inspeção direta de código, configuração, schema, testes e documentação.
- Resultado de ferramentas executadas, com comando e status resumidos.
- Métricas ou experimentos apenas quando executados em condições identificadas.
- Ausência de arquivo ou configuração só é achado quando o critério e o contexto tornam sua necessidade justificável.
