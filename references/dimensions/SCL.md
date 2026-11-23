# SCL — Escalabilidade

**Agente responsável:** `scalability-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| SCL-01 | Escalabilidade horizontal | Componentes podem operar em múltiplas instâncias quando necessário. |
| SCL-02 | Escalabilidade vertical | Aplicação aproveita recursos maiores adequadamente. |
| SCL-03 | Statelessness | Estado local não limita escala quando não necessário. |
| SCL-04 | Concorrência | Sistema suporta operações simultâneas dentro de seus objetivos. |
| SCL-05 | Gerenciamento de filas | Processamento assíncrono controla capacidade e backlog. |
| SCL-06 | Backpressure | Excesso de demanda é controlado. |
| SCL-07 | Distribuição de carga | Carga pode ser distribuída adequadamente. |
| SCL-08 | Particionamento de dados | Dados podem ser particionados quando necessário. |
| SCL-09 | Distribuição de processamento | Processamentos podem ser distribuídos com consistência. |
| SCL-10 | Limites de recursos | Componentes possuem limites e dimensionamento controlados. |
| SCL-11 | Isolamento de carga | Operações pesadas não prejudicam indiscriminadamente outras. |
| SCL-12 | Capacidade de crescimento | Crescimento não exige reestruturação desproporcional. |
| SCL-13 | Gerenciamento de gargalos | Gargalos podem ser identificados e tratados. |
| SCL-14 | Dependências compartilhadas | Recursos centralizados não se tornam gargalos inevitáveis. |
| SCL-15 | Distribuição de tarefas | Tarefas distribuídas evitam inconsistências. |
| SCL-16 | Tolerância a picos | Picos não comprometem estabilidade além dos limites definidos. |
| SCL-17 | Escalabilidade de armazenamento | Armazenamento acompanha o crescimento. |
| SCL-18 | Isolamento entre clientes | Um cliente não consome recursos ilimitados prejudicando outros quando aplicável. |
| SCL-19 | Escalabilidade de integrações | Integrações externas não limitam desnecessariamente o crescimento. |
| SCL-20 | Elasticidade | Recursos podem ser ajustados conforme demanda quando suportado. |

## Instruções de inspeção

- Avalie cada critério SCL aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
