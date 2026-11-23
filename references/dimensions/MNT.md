# MNT — Manutenibilidade e evolutividade

**Agente responsável:** `maintainability-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| MNT-01 | Localização de funcionalidades | É fácil encontrar a implementação de uma funcionalidade. |
| MNT-02 | Localização de regras de negócio | Regras possuem local definido e consistente. |
| MNT-03 | Localização de configurações | Configurações são organizadas e descobríveis. |
| MNT-04 | Localização de comportamentos | O comportamento de componentes pode ser rastreado. |
| MNT-05 | Isolamento de alterações | Mudanças permanecem no escopo necessário. |
| MNT-06 | Previsibilidade de mudanças | Impactos de alterações podem ser antecipados. |
| MNT-07 | Facilidade de refatoração | Componentes podem ser reorganizados com segurança. |
| MNT-08 | Facilidade de extensão | Novos comportamentos são adicionados sem modificações excessivas. |
| MNT-09 | Facilidade de substituição | Implementações podem ser substituídas por contratos estáveis. |
| MNT-10 | Compatibilidade retroativa | Contratos existentes são preservados quando necessário. |
| MNT-11 | Controle de breaking changes | Mudanças incompatíveis são identificadas e controladas. |
| MNT-12 | Débito técnico | Atalhos e inconsistências acumuladas são identificáveis e geridos. |
| MNT-13 | Acoplamento temporal | Componentes não dependem de ordem implícita de execução. |
| MNT-14 | Facilidade de depuração | Problemas podem ser reproduzidos e localizados. |
| MNT-15 | Facilidade de recuperação | Correções podem ser aplicadas sem intervenções desproporcionais. |
| MNT-16 | Consistência de padrões | Novas funcionalidades podem seguir padrões existentes. |
| MNT-17 | Dependências ocultas | Dependências relevantes são explícitas. |
| MNT-18 | Facilidade de remoção | Funcionalidades obsoletas podem ser removidas com segurança. |
| MNT-19 | Migração e evolução de dados | Alterações de dados e schema são controladas. |
| MNT-20 | Custo de manutenção | Esforço de manutenção é proporcional à complexidade do sistema. |

## Instruções de inspeção

- Avalie cada critério MNT aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
