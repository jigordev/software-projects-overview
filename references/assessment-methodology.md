# Assessment methodology

## Modes
- `full`: all 15 dimensions.
- `targeted`: explicitly selected dimensions.
- `incremental`: inspect a diff/commit and its affected context; do not claim a full-project baseline.
- `reassessment`: verify previously reported findings against the current revision.

## Phases
1. Scope and constraints.
2. Project discovery.
3. Dimension-specific inspection.
4. Finding validation and deduplication.
5. Scoring and hard-gate evaluation.
6. Report and prioritized remediation plan.

## Review principles
- Start with repository evidence; use tools to verify, not to replace reasoning.
- Prefer targeted inspection over indiscriminate full-repository reading.
- Read relevant tests and callers before judging behavior.
- Inspect configuration and deployment artifacts when the criterion requires them.
- Treat generated code, vendored dependencies, build output and fixtures according to scope; exclude them only with a stated rationale.
- A finding should identify a concrete gap, affected location, technical impact and minimal corrective direction.
- A recommendation is not a finding unless a real deficiency is evidenced.
- Record commit hash or repository state when available.

## Applicability
Use `applicable`, `not_applicable`, or `not_assessed`. Not applicable requires a rationale. Not assessed requires a reason such as missing access, unavailable environment, time/scope restriction or tool failure.

## Profiles
The catalog is universal. Profiles may adjust applicability and weights, never rewrite criterion meaning:
- API/backend
- frontend/web
- mobile
- library/SDK
- data-processing
- distributed systems/microservices
- monolith
- high-volume/high-throughput
- safety/mission-critical

Use a profile only when supported by project evidence or user instruction. Otherwise use the balanced default profile.

## Safe execution
Do not run destructive commands, production migrations, aggressive load tests, fuzzing against live targets, deployment actions, data deletion or secret-bearing commands without explicit authorization. Prefer read-only checks and local isolated test environments.
