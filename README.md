# software-projects-overview

Portable, evidence-based, multi-agent software project assessment skill.

## Contents
- `SKILL.md`: portable entry point and orchestration workflow.
- `agents/`: discovery, 15 dimension reviewers, validator and aggregator.
- `references/dimensions/`: criterion catalogs with stable codes and explanations.
- `references/`: methodology, scoring, severity, finding contract and portability.
- `schemas/`: JSON schemas for findings and consolidated assessment.
- `scripts/validate_findings.py`: standard-library validator for finding records.

## Install
Copy this folder into the skills directory recognized by the target harness:
- Codex: `.agents/skills/`
- Claude Code: `.claude/skills/`
- Cursor: `.agents/skills/` or `.cursor/skills/`

The skill contents are portable; discovery paths and agent orchestration capabilities differ by harness. See `references/harness-compatibility.md`.

## Invoke
Ask the agent to perform a full project assessment, or explicitly request targeted, incremental or reassessment mode.

## Safety
Read-only by default. No automatic code fixes, dependency installation, destructive commands, production operations or aggressive performance/security testing without explicit permission.

## Version
0.1.0 — initial framework package.
