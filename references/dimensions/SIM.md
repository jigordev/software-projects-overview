# SIM — Simplicidade e complexidade

**Agente responsável:** `simplicity-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| SIM-01 | Complexidade ciclomática | Quantidade de caminhos independentes é adequada. |
| SIM-02 | Complexidade cognitiva | Esforço mental para entender o fluxo é controlado. |
| SIM-03 | Profundidade de abstração | Camadas necessárias para compreender uma operação são proporcionais. |
| SIM-04 | Indireção | Saltos entre chamadas e implementação real são limitados. |
| SIM-05 | Dependência de contexto | Compreensão não exige conhecimento externo excessivo. |
| SIM-06 | Fluxo de execução | Caminhos de execução são previsíveis. |
| SIM-07 | Quantidade de estados | Estados e transições são limitados e compreensíveis. |
| SIM-08 | Interdependência de condições | Condições não dependem de combinações excessivamente complexas. |
| SIM-09 | Abstrações desnecessárias | Abstrações não acrescentam complexidade sem benefício. |
| SIM-10 | Generalização excessiva | Soluções não resolvem cenários hipotéticos sem necessidade. |
| SIM-11 | Comportamento implícito | Funcionamento não depende excessivamente de convenções ocultas. |
| SIM-12 | Complexidade de configuração | Inicialização e configuração são simples e previsíveis. |
| SIM-13 | Complexidade de alteração | Mudanças localizadas não exigem compreender partes desproporcionais. |
| SIM-14 | Quantidade de conceitos | Conceitos necessários para entender um fluxo são controlados. |
| SIM-15 | Complexidade acidental | Dificuldades introduzidas pela implementação são minimizadas. |

## Instruções de inspeção

- Avalie cada critério SIM aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
