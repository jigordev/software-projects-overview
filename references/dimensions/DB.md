# DB — Banco de dados e persistência

**Agente responsável:** `database-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| DB-01 | Modelagem de dados | Estruturas representam adequadamente o domínio e os acessos. |
| DB-02 | Normalização | Normalização e desnormalização são decisões conscientes. |
| DB-03 | Integridade referencial | Relacionamentos mantêm integridade. |
| DB-04 | Constraints | Restrições protegem invariantes no banco. |
| DB-05 | Índices | Índices correspondem aos padrões de consulta e escrita. |
| DB-06 | Consultas | Consultas são corretas, eficientes e previsíveis. |
| DB-07 | Plano de execução | Consultas críticas têm planos avaliados quando possível. |
| DB-08 | Transações | Transações têm limites e escopo apropriados. |
| DB-09 | Isolamento transacional | Nível de isolamento atende à consistência necessária. |
| DB-10 | Controle de concorrência | Conflitos e atualizações simultâneas são tratados. |
| DB-11 | Deadlocks | Deadlocks são prevenidos, identificados ou tratados. |
| DB-12 | Connection pooling | Conexões são gerenciadas corretamente. |
| DB-13 | Migrações | Alterações de schema são versionadas e reproduzíveis. |
| DB-14 | Compatibilidade de migrações | Alterações evitam incompatibilidade inesperada. |
| DB-15 | Integridade de escrita | Dados persistidos correspondem ao estado esperado. |
| DB-16 | Exclusão e atualização | Operações destrutivas têm proteção adequada. |
| DB-17 | Paginação | Consultas de grandes conjuntos são eficientes. |
| DB-18 | Retenção de dados | Políticas de retenção existem quando necessárias. |
| DB-19 | Backup | Estratégia de backup atende aos requisitos. |
| DB-20 | Restore | Backups podem ser restaurados e validados. |
| DB-21 | Evolução de schema | Schema acompanha a evolução da aplicação. |
| DB-22 | Uso de cache | Cache não compromete a consistência necessária. |
| DB-23 | Consultas em lote | Operações repetitivas evitam round trips excessivos. |
| DB-24 | Isolamento de dados | Dados de contextos ou clientes permanecem protegidos. |
| DB-25 | Volume de dados | Modelagem considera crescimento e distribuição dos dados. |
| DB-26 | Arquivamento | Dados históricos não prejudicam desnecessariamente operações atuais. |

## Instruções de inspeção

- Avalie cada critério DB aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
