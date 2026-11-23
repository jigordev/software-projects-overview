# DOC — Documentação e conhecimento

**Agente responsável:** `documentation-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| DOC-01 | README | Projeto possui orientação clara e atualizada. |
| DOC-02 | Instalação | Ambiente pode ser configurado seguindo instruções. |
| DOC-03 | Execução | Projeto pode ser executado sem conhecimento prévio excessivo. |
| DOC-04 | Arquitetura | Estrutura e decisões arquiteturais são explicadas. |
| DOC-05 | APIs | Contratos e endpoints são documentados quando aplicável. |
| DOC-06 | Configurações | Variáveis e configurações são documentadas. |
| DOC-07 | Banco de dados | Modelos e relacionamentos importantes são compreensíveis. |
| DOC-08 | Processos internos | Fluxos complexos possuem documentação útil. |
| DOC-09 | Decisões técnicas | Decisões relevantes registram contexto e justificativa. |
| DOC-10 | Convenções | Padrões de desenvolvimento estão definidos. |
| DOC-11 | Troubleshooting | Problemas comuns possuem orientações de diagnóstico. |
| DOC-12 | Atualização | Documentação acompanha o código. |
| DOC-13 | Exemplos | Existem exemplos úteis de utilização. |
| DOC-14 | Onboarding | Novo mantenedor consegue iniciar sem depender exclusivamente de terceiros. |
| DOC-15 | Conhecimento distribuído | Conhecimento não está concentrado em uma única pessoa. |

## Instruções de inspeção

- Avalie cada critério DOC aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
