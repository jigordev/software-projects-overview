# COD — Qualidade e legibilidade do código

**Agente responsável:** `code-quality-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| COD-01 | Clareza dos nomes | Nomes de variáveis, funções, classes e módulos comunicam intenção. |
| COD-02 | Legibilidade | O fluxo pode ser compreendido sem esforço desnecessário. |
| COD-03 | Consistência de nomenclatura | Convenções de nomes são uniformes. |
| COD-04 | Consistência de estilo | Formatação e convenções são consistentes. |
| COD-05 | Tamanho das funções | Funções têm tamanho proporcional à responsabilidade. |
| COD-06 | Tamanho das classes | Classes não acumulam responsabilidades excessivas. |
| COD-07 | Quantidade de parâmetros | Assinaturas não exigem parâmetros excessivos ou confusos. |
| COD-08 | Complexidade condicional | Ramificações são compreensíveis e controladas. |
| COD-09 | Aninhamento | Profundidade de estruturas aninhadas é controlada. |
| COD-10 | Duplicação | Lógica duplicada sem justificativa é evitada. |
| COD-11 | Código morto | Não há código sem uso ou inalcançável sem justificativa. |
| COD-12 | Código comentado | Implementações antigas não permanecem comentadas como substituto de histórico. |
| COD-13 | Tratamento de valores nulos | Valores opcionais e ausentes são tratados explicitamente. |
| COD-14 | Tipagem | Tipos esclarecem contratos e reduzem ambiguidades. |
| COD-15 | Imutabilidade | Estado não é mutado desnecessariamente. |
| COD-16 | Efeitos colaterais | Efeitos colaterais são previsíveis e controlados. |
| COD-17 | Magic numbers e strings | Valores relevantes têm significado nomeado ou documentado. |
| COD-18 | Tratamento de exceções | Exceções são tratadas no nível apropriado, sem ocultação indevida. |
| COD-19 | Retornos previsíveis | Funções possuem contratos de retorno consistentes. |
| COD-20 | Uso adequado da linguagem | Recursos idiomáticos são utilizados corretamente. |
| COD-21 | Transparência da implementação | A implementação torna o comportamento evidente. |
| COD-22 | Ausência de esperteza desnecessária | Metaprogramação e construções obscuras têm justificativa. |
| COD-23 | Consistência semântica | Nomes e abstrações correspondem ao comportamento real. |
| COD-24 | Proporcionalidade da solução | Complexidade implementada é proporcional ao problema. |

## Instruções de inspeção

- Avalie cada critério COD aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
