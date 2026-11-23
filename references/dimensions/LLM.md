# LLM — Compatibilidade com desenvolvimento por LLM

**Agente responsável:** `llm-readiness-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| LLM-01 | Descobribilidade | Agente consegue localizar onde implementar uma funcionalidade. |
| LLM-02 | Clareza estrutural | Estrutura comunica responsabilidades sem contexto excessivo. |
| LLM-03 | Consistência de padrões | Implementações semelhantes seguem padrões previsíveis. |
| LLM-04 | Explicitabilidade de contratos | Entradas, saídas e dependências estão explícitas. |
| LLM-05 | Contexto local | Componente pode ser compreendido sem carregar grande parte do projeto. |
| LLM-06 | Limites de contexto | Tarefa não exige investigar quantidade desproporcional de arquivos. |
| LLM-07 | Previsibilidade de alterações | Arquivos e contratos afetados podem ser antecipados. |
| LLM-08 | Autonomia de validação | Agente consegue executar testes e verificar resultados. |
| LLM-09 | Feedback automatizado | Erros são detectados por verificações acessíveis. |
| LLM-10 | Convenções documentadas | Agente consegue identificar padrões que deve seguir. |
| LLM-11 | Exemplos de implementação | Existem exemplos de referência consistentes. |
| LLM-12 | Contratos verificáveis | Interfaces possuem validações automatizadas. |
| LLM-13 | Isolamento de alterações | Mudanças podem permanecer em áreas relacionadas. |
| LLM-14 | Proteção contra regressões | Alterações podem ser comparadas com comportamento anterior. |
| LLM-15 | Proteção de áreas críticas | Áreas sensíveis possuem verificações específicas. |
| LLM-16 | Controle de escopo | O que pode e não pode ser modificado é identificável. |
| LLM-17 | Rastreabilidade de alterações | Motivo e escopo de mudanças podem ser registrados. |
| LLM-18 | Facilidade de reversão | Mudanças incorretas podem ser revertidas. |
| LLM-19 | Ausência de comportamento implícito | Regras não dependem de conhecimento tácito. |
| LLM-20 | Independência de memória externa | Projeto é compreensível sem conversas anteriores. |
| LLM-21 | Segurança das ferramentas | Agentes operam com permissões e ferramentas limitadas. |
| LLM-22 | Tarefas isoladas | Tarefas podem ser divididas em unidades verificáveis. |
| LLM-23 | Determinismo do ambiente | Execução e testes são reproduzíveis. |
| LLM-24 | Verificação de conformidade | Desvios de convenções são detectáveis. |

## Instruções de inspeção

- Avalie cada critério LLM aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
