# SEC — Segurança

**Agente responsável:** `security-reviewer.md`

## Catálogo de critérios

| Código | Critério | Explicação |
|---|---|---|
| SEC-01 | Autenticação | Identidade é validada corretamente quando aplicável. |
| SEC-02 | Autorização | Permissões são verificadas em operações protegidas. |
| SEC-03 | Controle de acesso | Acesso a recursos respeita políticas e propriedade. |
| SEC-04 | Isolamento de usuários | Usuários não acessam dados alheios indevidamente. |
| SEC-05 | Isolamento multi-tenant | Dados e operações de tenants são isolados quando aplicável. |
| SEC-06 | Validação de entrada | Entradas são validadas no limite de confiança. |
| SEC-07 | Sanitização e encoding de saída | Dados são codificados conforme o contexto de saída. |
| SEC-08 | SQL Injection | Consultas impedem injeção de comandos. |
| SEC-09 | NoSQL Injection | Consultas documentais impedem manipulação indevida. |
| SEC-10 | Command Injection | Entradas não controlam comandos do sistema operacional. |
| SEC-11 | XSS | Conteúdo não permite execução de scripts não autorizados. |
| SEC-12 | CSRF | Operações autenticadas via navegador são protegidas quando aplicável. |
| SEC-13 | SSRF | Requisições externas não alcançam recursos internos indevidos. |
| SEC-14 | Path Traversal | Caminhos não permitem acesso fora dos limites autorizados. |
| SEC-15 | Desserialização insegura | Dados serializados não provocam execução ou manipulação indevida. |
| SEC-16 | Proteção de segredos | Tokens, senhas e chaves não são expostos. |
| SEC-17 | Criptografia em trânsito | Comunicações sensíveis usam proteção adequada. |
| SEC-18 | Criptografia em repouso | Dados sensíveis recebem proteção quando necessária. |
| SEC-19 | Gerenciamento de sessões | Sessões e tokens têm ciclo de vida seguro. |
| SEC-20 | Rate limiting | Operações sujeitas a abuso possuem limites adequados. |
| SEC-21 | Proteção contra brute force | Tentativas repetidas são controladas. |
| SEC-22 | Proteção contra DoS | Recursos possuem limites e proteção contra exaustão. |
| SEC-23 | Upload de arquivos | Arquivos são validados, limitados e armazenados com segurança. |
| SEC-24 | Exposição de informações | Respostas, logs e erros não revelam dados sensíveis. |
| SEC-25 | Configuração segura | Configurações padrão não deixam controles críticos abertos. |
| SEC-26 | Headers de segurança | Headers adequados são configurados conforme o contexto. |
| SEC-27 | CORS | Origens, métodos e headers permitidos são restritos adequadamente. |
| SEC-28 | Dependências vulneráveis | Bibliotecas são verificadas contra vulnerabilidades conhecidas. |
| SEC-29 | Integridade das dependências | Procedência e integridade dos pacotes são verificáveis. |
| SEC-30 | Segurança de infraestrutura | Containers, redes, serviços e permissões são configurados com segurança. |
| SEC-31 | Segurança de APIs | Endpoints, parâmetros e operações respeitam controles de segurança. |
| SEC-32 | Segurança de integrações | Sistemas externos são acessados com credenciais e permissões adequadas. |
| SEC-33 | Proteção de dados pessoais | Dados pessoais são tratados conforme obrigações aplicáveis. |
| SEC-34 | Auditoria de operações | Ações sensíveis possuem rastreabilidade. |
| SEC-35 | Gestão de vulnerabilidades | Existe processo para identificar, priorizar e corrigir vulnerabilidades. |
| SEC-36 | Segurança em concorrência | Concorrência não permite violação de autorização ou integridade. |
| SEC-37 | Proteção de informações em memória | Segredos e dados sensíveis não são expostos ou mantidos sem necessidade. |
| SEC-38 | Limites de consumo | Requisições não provocam consumo ilimitado de recursos. |
| SEC-39 | Proteção contra alterações inseguras | Mudanças automatizadas não removem controles críticos sem detecção. |
| SEC-40 | Proteção de configurações sensíveis | Políticas e configurações críticas têm proteção contra alteração acidental. |
| SEC-41 | Validação obrigatória de mudanças | Mudanças sensíveis exigem verificações apropriadas. |
| SEC-42 | Controle de privilégios de agentes | Agentes recebem apenas permissões necessárias. |
| SEC-43 | Tratamento de conteúdo não confiável | Dados externos não são tratados como instruções privilegiadas. |
| SEC-44 | Segurança do pipeline | Build, testes e deploy não permitem execução ou publicação não autorizada. |

## Instruções de inspeção

- Avalie cada critério SEC aplicável ao projeto, usando evidências do repositório e verificações disponíveis.
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
