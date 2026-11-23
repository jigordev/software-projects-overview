# Scoring system

## Criterion maturity scale
- 0 — Absent or critically deficient; severe failure is evidenced.
- 1 — Critical: highly inconsistent, unsafe or difficult to maintain.
- 2 — Basic: partially implemented; material gaps remain.
- 3 — Adequate: correct and reasonably consistent for the context.
- 4 — Advanced: well-structured, validated and controlled.
- 5 — Excellent: mature, continuously verified and supported by strong evidence.

A score of 5 is not awarded merely because a tool or document exists. Verify actual use and effectiveness.

## Criterion evidence
Record evidence strength separately:
- E0: not assessed.
- E1: limited visual/manual observation.
- E2: direct code/configuration/documentation evidence.
- E3: automated check executed and result inspected.
- E4: test, experiment, runtime measurement or reproducible validation.

Do not equate evidence level with quality score.

## Dimension score
For applicable and scored criteria:
`dimension_score = sum(criterion_score * criterion_weight) / sum(criterion_weight) * 20`
Use equal criterion weights unless a documented profile defines otherwise. Exclude not-applicable criteria. Do not silently omit not-assessed criteria: disclose coverage and confidence.

## Overall score
`overall_score = sum(dimension_score * dimension_weight) / sum(applicable_dimension_weights)`
Default dimension weights:
ARC 10, COD 9, SIM 8, MNT 10, SEC 12, TST 9, REL 8, PER 8, SCL 7, DB 6, OBS 4, DOC 3, DEP 2, OPS 2, LLM 2. Total 100.
Weights are defaults, not universal truth. Profile changes must be explicit and recorded.

## Maturity bands
- 0–39: Level 1 — Critical
- 40–59: Level 2 — Basic
- 60–74: Level 3 — Adequate
- 75–89: Level 4 — Advanced
- 90–100: Level 5 — Excellent

## Hard gates
The overall score never overrides material risk:
- Confirmed unresolved critical security issue: cannot be rated Excellent; report security status as blocked.
- Confirmed unresolved high security issue: cannot exceed Adequate unless risk is demonstrably mitigated.
- Severe data-integrity failure: cannot exceed Adequate.
- Essential tests absent or non-executable: cannot be rated Excellent.
- Insufficient evidence/coverage: classification is provisional or withheld, not assumed positive.

Apply gates contextually. A scanner alert alone is not a confirmed vulnerability; validate exploitability, exposure and compensating controls.

## Confidence and coverage
Report:
- criteria assessed / applicable;
- dimensions assessed / requested;
- evidence distribution E1–E4;
- environment and tool limitations.
Use confidence labels High / Medium / Low with a short factual reason. Do not hide low coverage behind a numeric score.
