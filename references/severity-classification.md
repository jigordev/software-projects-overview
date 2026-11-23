# Severity classification

- S0 Critical: credible severe compromise of confidentiality, integrity or availability; urgent containment/remediation.
- S1 High: significant security, data integrity, availability or operational risk.
- S2 Medium: meaningful maintainability, reliability, security or performance deficiency with bounded impact.
- S3 Low: localized issue with limited impact.
- S4 Informational: improvement opportunity or observation; not necessarily a defect.

Severity is based on impact, exposure, exploitability/likelihood, affected scope and available mitigations. Do not assign severity based only on code smell or tool output.

Security issues should additionally record confidence and exposure where known. Never reproduce secret values.
