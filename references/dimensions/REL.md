# REL — Confiabilidade e resiliência

**Agente responsável:** `reliability-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| REL-01 | Tratamento de falhas | Falhas são identificadas e tratadas adequadamente. |
| REL-02 | Isolamento de falhas | Uma falha não se propaga desnecessariamente. |
| REL-03 | Timeouts | Operações externas possuem limites de tempo. |
| REL-04 | Retry | Tentativas são controladas e seguras. |
| REL-05 | Backoff | Repetições usam intervalos apropriados. |
| REL-06 | Idempotência | Repetir operações não causa efeitos indevidos. |
| REL-07 | Circuit breaker | Falhas recorrentes não provocam sobrecarga contínua quando aplicável. |
| REL-08 | Fallback | Alternativas seguras existem quando justificadas. |
| REL-09 | Consistência de estado | Estado permanece válido após falhas. |
| REL-10 | Transações | Operações atômicas possuem escopo adequado. |
| REL-11 | Recuperação | O sistema recupera-se de falhas previsíveis. |
| REL-12 | Graceful shutdown | Encerramento preserva operações e recursos importantes. |
| REL-13 | Gestão de recursos | Conexões, arquivos e recursos são liberados corretamente. |
| REL-14 | Concorrência | Operações simultâneas não provocam condições de corrida. |
| REL-15 | Tolerância a indisponibilidade externa | Falhas de terceiros são tratadas sem colapsar o sistema. |
| REL-16 | Integridade dos dados | Dados não são corrompidos em cenários de falha. |
| REL-17 | Recuperação de processos | Processamentos interrompidos podem ser retomados quando necessário. |
| REL-18 | Prevenção de processamento duplicado | Eventos e tarefas duplicados não causam efeitos incorretos. |
| REL-19 | Recuperação de mensagens | Mensagens com falha são recuperáveis ou encaminhadas para tratamento. |
| REL-20 | Consistência eventual | Processos distribuídos possuem convergência definida quando aplicável. |

## Instruções de inspeção

- Avalie cada critério REL aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
