# PER — Performance e eficiência

**Agente responsável:** `performance-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| PER-01 | Latência | Tempo de conclusão atende às necessidades e metas definidas. |
| PER-02 | Throughput | Volume processado por unidade de tempo é adequado. |
| PER-03 | Uso de CPU | Processamento utiliza CPU de maneira eficiente. |
| PER-04 | Uso de memória | Consumo e crescimento de memória são controlados. |
| PER-05 | Alocação de objetos | Alocações e pressão de garbage collection são proporcionais. |
| PER-06 | I/O | Leitura e escrita evitam operações desnecessárias. |
| PER-07 | Operações bloqueantes | Bloqueios não prejudicam fluxos concorrentes. |
| PER-08 | Concorrência | Recursos simultâneos são utilizados adequadamente. |
| PER-09 | Processamento assíncrono | Assincronia é aplicada corretamente quando apropriada. |
| PER-10 | Algoritmos | Complexidade temporal e espacial é adequada. |
| PER-11 | Estruturas de dados | Estruturas são escolhidas conforme operações e volume. |
| PER-12 | Cache | Cache possui estratégia de uso, expiração e invalidação coerente. |
| PER-13 | Serialização | Conversão de dados evita overhead desnecessário. |
| PER-14 | Desserialização | Processamento de dados recebidos é eficiente. |
| PER-15 | Transferência de dados | Volume transferido é proporcional à necessidade. |
| PER-16 | Processamento em lote | Operações repetitivas são agrupadas quando vantajoso. |
| PER-17 | Lazy loading | Recursos são carregados quando necessários. |
| PER-18 | Eager loading | Dados relacionados são carregados evitando consultas repetidas. |
| PER-19 | N+1 queries | Consultas repetitivas desnecessárias são evitadas. |
| PER-20 | Paginação | Grandes conjuntos são processados em páginas eficientes. |
| PER-21 | Streaming | Grandes volumes podem ser processados sem carregar tudo em memória. |
| PER-22 | Gerenciamento de conexões | Pools e conexões são utilizados adequadamente. |
| PER-23 | Overhead de abstrações | Camadas não introduzem custo injustificado. |
| PER-24 | Eficiência de consultas | Consultas evitam operações e leituras desnecessárias. |
| PER-25 | Profiling | Gargalos podem ser identificados por medições. |
| PER-26 | Regressão de performance | Mudanças não degradam desempenho silenciosamente. |

## Instruções de inspeção

- Avalie cada critério PER aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
