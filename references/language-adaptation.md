# Language and framework adaptation

The framework is language-agnostic. Reviewers must discover the stack before selecting tools.

Examples (not mandatory tooling):
- Python: Ruff, mypy/pyright, pytest, coverage, Bandit, pip-audit, Semgrep, Radon, py-spy.
- JavaScript/TypeScript: ESLint, TypeScript compiler, Vitest/Jest, npm/pnpm audit, Semgrep, dependency graph tooling.
- PHP: PHPStan/Psalm, PHP-CS-Fixer/Pint, PHPUnit, Composer audit.
- Java/Kotlin: compiler warnings, Checkstyle/SpotBugs, JUnit, dependency scanners.
- Go: go vet, staticcheck, go test, govulncheck.
- Rust: clippy, cargo test, cargo audit.
- Containers/IaC: Trivy, Checkov or equivalent scanners where relevant.

Tool selection must follow project stack and available environment. Do not install tools or alter lockfiles without permission. Report commands actually executed and their results. A tool's absence is not automatically a defect; inability to verify is a limitation.
