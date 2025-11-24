<!--
Sync Impact Report
Version change: template -> 1.0.0
Modified principles: (template placeholders → concrete)
	- PRINCIPLE_1_NAME -> I. Readability & Clarity
	- PRINCIPLE_2_NAME -> II. Consistency & Style
	- PRINCIPLE_3_NAME -> III. DRY (Don't Repeat Yourself)
	- PRINCIPLE_4_NAME -> IV. YAGNI & Simplicity
	- PRINCIPLE_5_NAME -> V. Documentation & Discoverability
Added sections: Development Workflow (expanded), Constraints & Standards
Removed sections: none
Templates updated: ✅ .specify/templates/plan-template.md
									 ✅ .specify/templates/spec-template.md
									 ✅ .specify/templates/tasks-template.md
Follow-up TODOs: none
-->

# News API Constitution

## Core Principles

### I. Readability & Clarity (NON-NEGOTIABLE)
Code MUST be written for humans first. Clear names, straightforward control flow,
and explicit behavior are required. Avoid cleverness that obscures intent. Code
reviews MUST prioritize comprehensibility: if a reviewer cannot explain the
purpose of the code in plain language, the change MUST be revised.

Rationale: Readable code reduces onboarding time, lowers review cost, and
reduces defects over time.

### II. Consistency & Style
Projects MUST adopt and enforce a single, automated style configuration
(formatter + linter + type checking) via CI. Consistency across the codebase
enables predictable diffs, easier reviews, and faster automation.

Rules:
- Enforce formatting (e.g., `black` / `prettier`) and a linter (e.g., `ruff` / `eslint`).
- Use static typing where practical (type annotations + type checks in CI).
- Document and pin the shared style configuration in the repository.

### III. DRY — Don't Repeat Yourself
Duplication of intent is discouraged. Shared logic SHOULD be centralized as a
well-documented function/module. However, duplication that preserves clarity
is acceptable temporarily; refactor when a clear, maintainable abstraction
emerges.

Rules:
- Avoid duplicated business logic across services/modules.
- When proposing a shared abstraction, include tests and an interoperability
	plan to avoid coupling issues.

### IV. YAGNI — You Aren't Gonna Need It (Simplicity)
Implement only what is necessary to meet the agreed acceptance criteria. Do
not add features, flags, or extensibility for hypothetical future needs unless
there is strong, documented justification.

Rules:
- New abstractions MUST include a justification section in PR descriptions.
- If complexity is proposed, include measurable benefits and a migration plan.

### V. Documentation & Discoverability
Documentation is part of the product. Code MUST include concise docstrings for
public interfaces, and features MUST provide a `quickstart.md` and a short API
summary where applicable. Documentation MUST be updated in the same PR that
changes behavior.

Rules:
- Public functions/modules/classes MUST have docstrings describing behavior,
	inputs, outputs, and errors.
- Feature specs MUST include a `quickstart.md` and example(s) that allow a
	reviewer to exercise the primary user journey.

## Constraints & Standards

- Prefer Python 3.11+ idioms for this repository; use the project's declared
	runtime in CI.
- Dependencies MUST be pinned or use a lockfile; dependency updates require a
	dedicated PR demonstrating automated checks pass.
- Security-sensitive code MUST include a short security review note in the PR.
- CI gates (format + lint + type checks + tests for P1 stories) MUST pass
	before merging.

## Development Workflow

- All work MUST be proposed via a spec and a plan (`specs/` structure).
- Every PR MUST reference a spec or task ID and include a brief rationale
	mapping code changes to the project's principles (Readability, DRY, YAGNI,
	Documentation).
- Tests: For P1 user stories tests are MANDATORY and should be added in the
	same PR. Tests should be written to fail first when feasible.
- Documentation updates that affect behavior or developer UX MUST land with
	the feature PR.

## Governance

Amendments: Amendments to this constitution require a documented proposal
(spec) and a two-step approval: (1) majority approval from active maintainers
in a review, and (2) a migration plan for any breaking governance changes.

Versioning policy:
- Versions follow MAJOR.MINOR.PATCH.
- MAJOR: Backwards-incompatible governance changes (removal/renaming of
	principles or change in approval rules).
- MINOR: Addition of a new principle or material expansion of guidance.
- PATCH: Wording clarifications, typo fixes, and non-substantive edits.

Compliance:
- PRs that introduce complexity counter to these principles MUST include a
	justification and be explicitly approved by two reviewers, one of whom is a
	maintainer.

**Version**: 1.0.0 | **Ratified**: 2025-11-23 | **Last Amended**: 2025-11-23
