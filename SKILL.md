---
name: software-projects-overview
description: Avalia a qualidade técnica, arquitetura, manutenibilidade, simplicidade, segurança, testes, confiabilidade, performance, escalabilidade, dados, observabilidade, documentação, dependências, operação e prontidão para manutenção humana ou por LLM de projetos de software. Use quando solicitar auditoria, diagnóstico, classificação de maturidade ou revisão abrangente de um repositório.
---

# Software Projects Overview

## Missão

Executar uma avaliação técnica estruturada, baseada em evidências, de projetos de software de qualquer linguagem, framework, arquitetura ou domínio. O resultado deve ajudar mantenedores humanos e agentes de IA a compreender riscos e priorizar melhorias.

A skill é **read-only por padrão**: inspeciona e executa verificações seguras, mas não modifica código, configurações, dependências, dados ou infraestrutura. Só faça correções se o usuário solicitar explicitamente em uma tarefa separada.

## Princípios obrigatórios

1. Avalie o projeto real, não um projeto idealizado ou uma arquitetura presumida.
2. Não invente arquivos, linhas, comportamentos, testes executados ou resultados de ferramentas.
3. Todo achado deve usar um código válido do catálogo `references/dimensions/`.
4. Todo achado deve indicar localização verificável e evidência mínima suficiente.
5. Não transforme preferência pessoal em defeito. Explique impacto técnico observável.
6. Não penalize ausência de tecnologia ou padrão que não seja necessário ao contexto.
7. Diferencie `not_applicable`, `not_assessed` e `assessed`.
8. Não declare que um controle existe porque há uma dependência instalada; verifique uso e configuração.
9. Não declare segurança, performance ou escalabilidade comprovadas sem evidência apropriada.
10. Evite duplicar achados. Registre a causa raiz uma vez e referencie impactos secundários quando necessário.
11. Minimize tokens: achados curtos, específicos, sem introduções, elogios ou explicações didáticas.
12. Não exponha segredos encontrados. Informe apenas tipo e localização; nunca reproduza o valor.
13. Não execute testes destrutivos, carga agressiva, fuzzing invasivo, migrações ou comandos com efeitos persistentes sem autorização.
14. Não trate ausência de evidência como evidência de ausência. Marque como não avaliado quando a inspeção não permitir conclusão.
15. Preserve escopo: não faça refatoração nem correção durante a auditoria.

## Fluxo de execução

### 1. Entender o pedido e definir escopo

Identifique se o usuário pediu:
- `full`: auditoria completa das 15 dimensões (padrão);
- `targeted`: dimensões específicas;
- `incremental`: alterações de uma branch, commit ou diff;
- `reassessment`: reavaliação de achados anteriores.

Se o escopo não estiver claro e isso alterar materialmente o trabalho, faça uma pergunta curta. Caso contrário, use `full`.

Registre limites conhecidos: diretórios excluídos, ausência de acesso a serviços, comandos indisponíveis, ambiente sem dependências, falta de permissões ou execução proibida.

### 2. Descoberta do projeto

Leia primeiro `agents/project-discovery.md`. Identifique linguagem, frameworks, pontos de entrada, módulos, persistência, integrações, testes, CI/CD, infraestrutura, documentação e comandos de validação.

Não presuma FastAPI, Python, banco relacional ou microsserviços. Adapte a inspeção ao que for encontrado.

### 3. Planejar revisores

Para auditoria completa, considere os 15 revisores descritos em `agents/`. Para auditoria direcionada, execute somente os revisores pertinentes e informe dimensões não avaliadas.

Cada revisor deve:
- ler apenas sua instrução de agente e a referência de sua dimensão;
- usar o contexto compartilhado de descoberta;
- inspecionar o código e executar somente verificações seguras e pertinentes;
- emitir achados no formato comum;
- registrar critérios avaliados, não avaliados e não aplicáveis;
- não atribuir notas a partir de suposições.

### 4. Orquestração multiagente portável

Se o harness oferecer subagentes, delegue revisores independentes e paralelizáveis. Cada subagente recebe: objetivo, escopo, contexto de descoberta, arquivos/diretórios relevantes, instrução do revisor e formato de saída.

Se não houver subagentes, execute os mesmos revisores sequencialmente, um por vez. Não simule paralelismo nem afirme que agentes separados foram executados quando houve apenas uma execução.

Não dependa de APIs, nomes de ferramentas, sintaxe de delegação ou recursos exclusivos de um harness. Use os mecanismos disponíveis no ambiente e preserve o contrato de saída.

### 5. Validar e consolidar

Leia `agents/findings-validator.md` e `agents/assessment-aggregator.md`.
- valide códigos contra o catálogo;
- confirme que localização e evidência existem;
- remova duplicações;
- diferencie achado confirmado, suspeita e limitação de avaliação;
- consolide notas sem esconder bloqueios;
- não conte critérios não aplicáveis como zero;
- não transforme critérios não avaliados em aprovados.

### 6. Entregar relatório

Use `references/assessment-methodology.md`, `references/scoring-system.md`, `references/severity-classification.md` e `references/finding-format.md`.

O relatório deve priorizar:
1. classificação e confiança da avaliação;
2. riscos críticos/altos;
3. achados concisos por dimensão;
4. critérios não avaliados e limitações;
5. plano de correção ordenado por risco.

Não despeje logs completos nem a cadeia de raciocínio dos agentes. Apresente conclusões, evidências e justificativas técnicas concisas.

## Códigos de dimensão

| Código | Dimensão |
|---|---|
| ARC | Arquitetura e organização estrutural |
| COD | Qualidade e legibilidade do código |
| SIM | Simplicidade e complexidade |
| MNT | Manutenibilidade e evolutividade |
| SEC | Segurança |
| TST | Testabilidade e qualidade dos testes |
| REL | Confiabilidade e resiliência |
| PER | Performance e eficiência |
| SCL | Escalabilidade |
| DB | Banco de dados e persistência |
| OBS | Observabilidade e diagnóstico |
| DOC | Documentação e conhecimento |
| DEP | Dependências e cadeia de suprimentos |
| OPS | Entrega, implantação e operação |
| LLM | Compatibilidade com desenvolvimento por LLM |

Os códigos completos e suas explicações estão nas tabelas dos arquivos `references/dimensions/<PREFIX>.md`. Nunca crie códigos fora do catálogo sem uma alteração versionada do framework.

## Saída mínima

O relatório consolidado deve incluir:
- identificação do projeto e escopo;
- dimensões avaliadas e não avaliadas;
- pontuação por dimensão e nota geral, se houver evidência suficiente;
- maturidade e bloqueios;
- achados com código, severidade, localização, detalhe e correção mínima;
- limitações da avaliação;
- data/referência do commit ou estado inspecionado, se disponível.

## Referências sob demanda

- Processo: `references/assessment-methodology.md`
- Pontuação: `references/scoring-system.md`
- Severidade: `references/severity-classification.md`
- Achados: `references/finding-format.md`
- Regras universais: `references/universal-rules.md`
- Adaptação tecnológica: `references/language-adaptation.md`
- Portabilidade: `references/harness-compatibility.md`
- Critérios: `references/dimensions/<PREFIX>.md`
