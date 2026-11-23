# OBS — Observabilidade e diagnóstico

**Agente responsável:** `observability-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| OBS-01 | Logs estruturados | Logs têm estrutura consistente e pesquisável. |
| OBS-02 | Níveis de log | Severidades são utilizadas corretamente. |
| OBS-03 | Contexto dos logs | Eventos contêm contexto suficiente para investigação. |
| OBS-04 | Correlation ID | Requisições podem ser correlacionadas entre componentes. |
| OBS-05 | Métricas | Indicadores operacionais relevantes são coletados. |
| OBS-06 | Distributed tracing | Fluxos distribuídos podem ser acompanhados quando aplicável. |
| OBS-07 | Identificação de erros | Erros são identificáveis e categorizados. |
| OBS-08 | Alertas | Condições críticas podem gerar alertas acionáveis. |
| OBS-09 | Health checks | Estado dos componentes pode ser verificado. |
| OBS-10 | Diagnóstico de performance | Gargalos podem ser investigados por observabilidade. |
| OBS-11 | Auditoria | Operações importantes possuem histórico rastreável. |
| OBS-12 | Proteção de logs | Dados sensíveis não são expostos nos registros. |

## Instruções de inspeção

- Avalie cada critério OBS aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
