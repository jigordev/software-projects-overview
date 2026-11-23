# Finding format

## Required fields
Each finding must contain only the minimum information needed to locate and understand the issue:

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Stable identifier within this assessment, e.g. `F-SEC-001`. |
| `code` | yes | Exact catalog code, e.g. `SEC-02`. |
| `severity` | yes | `S0`–`S4`. |
| `location` | yes | Repository-relative path and line/range, symbol, config key or resource. |
| `detail` | yes | Concise factual description of the defect and its impact. |
| `fix` | yes | Minimal corrective direction, not a full implementation. |
| `evidence` | yes | Short code/config excerpt or exact observed fact; redact secrets. |
| `confidence` | yes | `high`, `medium`, or `low`. |

Optional fields: `related_codes`, `tool`, `verification`, `status`.

## Concision rules
- `detail`: usually one sentence, maximum two.
- `fix`: one direct sentence.
- `evidence`: smallest excerpt or fact that proves the issue.
- Do not include background tutorials, generic best practices, praise, speculative consequences or long remediation plans.
- Prefer `src/auth/permissions.py:41-48` over “authentication module”.
- If line numbers are unavailable, cite path plus function/class/config key.
- If a finding spans multiple locations, list only the minimal relevant locations.
- Never invent line numbers.
- Never paste secret values, tokens, passwords, private keys or sensitive personal data.

## Example
```json
{
  "id": "F-SEC-001",
  "code": "SEC-02",
  "severity": "S1",
  "location": "src/api/orders.py:84-91",
  "detail": "The endpoint returns an order by ID without verifying that it belongs to the authenticated tenant.",
  "fix": "Apply tenant-scoped authorization before returning the order.",
  "evidence": "The query filters only by order_id; no tenant/user ownership predicate is applied.",
  "confidence": "high"
}
```

## No-finding result
For a reviewed dimension with no confirmed findings, state `No confirmed findings` and list any limitations. Do not imply the dimension is perfectly secure or defect-free.
