# ARC — Arquitetura e organização estrutural

**Agente responsável:** `architecture-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| ARC-01 | Organização de diretórios | Estrutura de pastas lógica, previsível e intuitiva. |
| ARC-02 | Separação de responsabilidades | Cada módulo possui responsabilidades coerentes e delimitadas. |
| ARC-03 | Coesão dos módulos | Elementos relacionados estão agrupados no mesmo módulo ou limite. |
| ARC-04 | Acoplamento | Dependências entre módulos são controladas e proporcionais. |
| ARC-05 | Direção das dependências | Camadas internas não dependem indevidamente de detalhes externos. |
| ARC-06 | Limites arquiteturais | Fronteiras entre módulos, camadas e domínios são identificáveis. |
| ARC-07 | Independência de componentes | Componentes podem evoluir sem alterações generalizadas. |
| ARC-08 | Encapsulamento | Detalhes internos não são expostos sem necessidade. |
| ARC-09 | Contratos entre módulos | Interfaces, entradas, saídas e responsabilidades são explícitas. |
| ARC-10 | Gerenciamento de dependências | Dependências são declaradas e injetadas de forma coerente. |
| ARC-11 | Ausência de dependências circulares | Não existem ciclos arquiteturais prejudiciais. |
| ARC-12 | Consistência arquitetural | O projeto segue padrões coerentes, sem estilos conflitantes injustificados. |
| ARC-13 | Isolamento de infraestrutura | Regras de negócio não dependem diretamente de detalhes técnicos evitáveis. |
| ARC-14 | Extensibilidade arquitetural | Novas capacidades podem ser adicionadas sem reestruturação desproporcional. |
| ARC-15 | Ausência de abstrações prematuras | Abstrações possuem justificativa concreta. |
| ARC-16 | Ausência de componentes centrais excessivos | Módulos centrais não concentram responsabilidades demais. |
| ARC-17 | Gestão de dependências compartilhadas | Recursos globais têm ciclo de vida e propriedade definidos. |
| ARC-18 | Consistência entre módulos semelhantes | Funcionalidades equivalentes seguem convenções compatíveis. |

## Instruções de inspeção

- Avalie cada critério ARC aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
