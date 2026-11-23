# DEP — Dependências e cadeia de suprimentos

**Agente responsável:** `dependencies-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| DEP-01 | Dependências necessárias | Dependências possuem justificativa de uso. |
| DEP-02 | Dependências não utilizadas | Dependências abandonadas ou sem uso são removidas. |
| DEP-03 | Versionamento | Versões são controladas adequadamente. |
| DEP-04 | Reprodutibilidade | Instalações produzem ambientes previsíveis. |
| DEP-05 | Atualizações | Existe estratégia de atualização. |
| DEP-06 | Vulnerabilidades | Dependências são verificadas quanto a vulnerabilidades. |
| DEP-07 | Licenciamento | Licenças são compatíveis com o uso pretendido. |
| DEP-08 | Manutenção externa | Dependências críticas possuem manutenção adequada. |
| DEP-09 | Dependências transitivas | Riscos de dependências indiretas são considerados. |
| DEP-10 | Lockfiles | Resolução de dependências é fixada quando aplicável. |
| DEP-11 | Integridade | Origem e integridade dos pacotes são verificáveis. |
| DEP-12 | Dependência excessiva | Funcionalidades simples não exigem bibliotecas desnecessariamente complexas. |

## Instruções de inspeção

- Avalie cada critério DEP aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
