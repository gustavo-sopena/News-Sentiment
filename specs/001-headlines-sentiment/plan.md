# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a small Python CLI tool that fetches headlines for a selected category
from NewsAPI.org, runs a lexicon-based sentiment analysis on each headline,
and outputs a bar chart PNG and an optional CSV of counts. The implementation
will be minimal-dependency Python (3.11+), using `requests` for HTTP,
`matplotlib` for plotting, and the standard `csv` module for CSV output. Unit
tests will be written with `pytest` and linting with `ruff` recommended.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.11+  
**Primary Dependencies**: `requests`, `matplotlib`, `pytest` (dev), `ruff` (dev), optional `langdetect` or similar for language detection  
**Storage**: Flat CSV files for export; no DB required (N/A)  
**Testing**: `pytest` for unit and simple integration tests  
**Target Platform**: macOS / Linux (CLI script)  
**Project Type**: single project (CLI tool)  
**Performance Goals**: End-to-end for 50 headlines < 5s on a typical developer laptop  
**Constraints**: Uses NewsAPI.org (requires API key); lexicon-based sentiment scoring; must handle API rate limits and surface clear error messages.  
**Scale/Scope**: Small (single-user CLI tool, local runs), no multi-tenant or long-term storage requirements.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Gates (per News API Constitution v1.0.0):

- Code style enforced (formatter + linter) in CI.
- Type checks enabled where applicable; typing inconsistencies MUST be
  documented and justified.
- Documentation: feature must include `quickstart.md` + concise API summary
  for the primary user journey.
- Tests: P1 user stories MUST include automated tests that run in CI.
- DRY/YAGNI rationale: any proposed cross-cutting abstraction MUST include
  justification and a migration/refactor plan.

The `/speckit.plan` command SHOULD validate these gates are planned for and
flag any violations that require explicit justification in the plan.

### Constitution Re-Check (post-Phase0 research)

- **Style/Lint in CI**: Planned — we will include `ruff` in `dev-requirements` and add a CI job to run formatting/lint checks before merge.
- **Type checks**: Planned — code will include type hints for public functions and `mypy` may be added if needed; for now, `ruff`/`pyright` can be considered.
- **Documentation**: `quickstart.md` present in the feature spec directory — PASS.
- **Tests**: P1 user story requires unit tests and an integration test; tests are specified in the spec and will be added alongside implementation — PASS (planned).
- **DRY/YAGNI rationale**: Design remains minimal (single script + small modules); no cross-cutting abstractions proposed that would violate YAGNI — PASS.

Status: No gate violations identified that require complexity tracking. Proceed to Phase 1 design.

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]
```

**Structure Decision**: Single Python CLI project. Suggested layout:

```text
src/
├── headlines_sentiment/
│   ├── __main__.py   # CLI entry
│   ├── fetcher.py    # NewsAPI client
│   ├── sentiment.py  # Lexicon-based analyzer
│   └── plot.py       # matplotlib charting
tests/
├── unit/
└── integration/
``` 

This keeps the feature self-contained and easy to test.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
