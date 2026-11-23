# Harness compatibility

## Portable core
Use only:
- `SKILL.md` with standard YAML frontmatter (`name`, `description`);
- Markdown instructions and references;
- JSON schemas;
- optional scripts that use common runtimes and standard input/output.

Avoid mandatory dependencies on:
- a vendor-specific subagent API;
- a named model or model-specific prompt syntax;
- a proprietary tool namespace;
- a specific shell or operating system;
- a fixed repository layout.

## Agent execution
The orchestrator should detect whether the harness supports subagents/delegation. If yes, dispatch dimension reviewers with isolated instructions and shared read-only context. If not, run reviewers sequentially using the same agent files. The review contract and output schema remain identical.

Do not claim parallel execution unless actual independent agents were launched.

## Installation locations
Common project-level locations:
- Codex: `.agents/skills/software-projects-overview/`
- Claude Code: `.claude/skills/software-projects-overview/`
- Cursor: `.agents/skills/software-projects-overview/` or `.cursor/skills/software-projects-overview/`

Use one canonical source directory and copy or link it into harness-specific discovery locations. Verify current official documentation for each harness version before automating installation; discovery paths and capabilities can change.

## Portability limitations
A portable `SKILL.md` does not guarantee identical subagent behavior, tool availability, permissions, context limits or automatic discovery across harnesses. The skill must degrade gracefully to sequential review and must report unavailable capabilities.
