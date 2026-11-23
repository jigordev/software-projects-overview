# TST — Testabilidade e qualidade dos testes

**Agente responsável:** `testing-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| TST-01 | Testabilidade arquitetural | Componentes podem ser testados de forma isolada. |
| TST-02 | Isolamento dos testes | Testes não dependem indevidamente uns dos outros. |
| TST-03 | Testes unitários | Unidades e regras relevantes possuem testes. |
| TST-04 | Testes de integração | Integrações entre componentes são verificadas. |
| TST-05 | Testes de contrato | Contratos entre serviços e consumidores são validados. |
| TST-06 | Testes end-to-end | Fluxos importantes são verificados ponta a ponta. |
| TST-07 | Cobertura de cenários críticos | Operações importantes possuem cenários de teste suficientes. |
| TST-08 | Cobertura de branches | Caminhos condicionais relevantes são exercitados. |
| TST-09 | Testes de exceção | Falhas e condições inesperadas são verificadas. |
| TST-10 | Testes de borda | Valores extremos, vazios, nulos e inválidos são contemplados. |
| TST-11 | Determinismo | Testes produzem resultados reproduzíveis. |
| TST-12 | Independência de ambiente | Testes executam em ambientes controlados. |
| TST-13 | Qualidade dos asserts | Verificações validam efetivamente o comportamento esperado. |
| TST-14 | Qualidade dos mocks | Mocks não ocultam problemas reais de integração. |
| TST-15 | Testes de regressão | Correções não reintroduzem defeitos conhecidos. |
| TST-16 | Testes de concorrência | Comportamentos simultâneos são verificados quando relevantes. |
| TST-17 | Testes de segurança | Controles e cenários de segurança são testados. |
| TST-18 | Testes de performance | Operações relevantes são submetidas a medições de carga. |
| TST-19 | Tempo de execução | A suíte tem duração adequada ao ciclo de desenvolvimento. |
| TST-20 | Manutenção dos testes | Testes são claros, isolados e fáceis de modificar. |
| TST-21 | Testes de mutação | Testes detectam alterações incorretas na implementação. |
| TST-22 | Testes de migração | Alterações de schema e migrações são verificadas. |
| TST-23 | Testes de compatibilidade | Compatibilidade entre versões e contratos é validada. |
| TST-24 | Qualidade dos dados de teste | Fixtures representam cenários relevantes e controlados. |

## Instruções de inspeção

- Avalie cada critério TST aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
