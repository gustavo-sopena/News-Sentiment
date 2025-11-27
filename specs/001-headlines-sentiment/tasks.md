---
description: "Tasks for Headlines Sentiment Chart feature"
---

# Tasks: Headlines Sentiment Chart

**Input**: Design documents from `/specs/001-headlines-sentiment/` (`spec.md`, `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`)

## Phase 1: Setup (Shared Infrastructure)

Purpose: Project initialization, tooling, and docs required before any implementation.

- [ ] T001 Create project structure `src/headlines_sentiment/`, `tests/unit/`, `tests/integration/`, `data/` (create directories and placeholder __init__ files)
- [ ] T002 Initialize `requirements.txt` with minimal deps: `requests`, `matplotlib` and dev deps: `pytest`, `ruff`
- [ ] T003 [P] Add `pyproject.toml` with formatting/lint config (black/ruff settings) at `pyproject.toml`
- [ ] T004 [P] Add CI workflow ` .github/workflows/ci.yml` to run `ruff` and `pytest`
- [ ] T005 Create `README.md` and update `specs/001-headlines-sentiment/quickstart.md` with example commands

---

## Phase 2: Foundational (Blocking Prerequisites)

Purpose: Core modules, tests, and contracts that all user stories depend on.

- [ ] T006 Create NewsAPI client skeleton in `src/headlines_sentiment/fetcher.py` (functions: `fetch_headlines(category, page_size)`)
- [ ] T007 [P] Create sentiment module skeleton in `src/headlines_sentiment/sentiment.py` (functions: `score_headline(text) -> (sentiment, score)`)
- [ ] T008 [P] Create plotting module skeleton in `src/headlines_sentiment/plot.py` (functions: `plot_counts(counts, out_path)`)
- [ ] T009 Implement CLI entrypoint `src/headlines_sentiment/__main__.py` that parses args: `--category`, `--sample`, `--out`, `--csv`
- [ ] T010 [P] Add basic logging/error handling configuration in `src/headlines_sentiment/logging_config.py`
- [ ] T011 Create unit test placeholders: `tests/unit/test_sentiment.py`, `tests/unit/test_fetcher.py`
- [ ] T012 Create integration test placeholder: `tests/integration/test_end_to_end.py` (can use recorded sample data in `data/sample_headlines.json`)
- [ ] T013 Add sample/gold dataset `data/gold/headlines_gold.csv` for basic validation and CI (small set of English headlines)

**Checkpoint**: Foundational modules exist and basic tests run (even if some tests are TODO or use mocked data).

---

## Phase 3: User Story 1 - Generate sentiment chart (Priority: P1) 🎯 MVP

Goal: Implement end-to-end flow: fetch headlines → analyze sentiment → output bar chart PNG (and CSV).

Independent Test: Run CLI with `--category technology --sample 50` and verify `chart.png` and `counts.csv` are produced and counts match sentiment output.

### Tests (MANDATORY for P1)

- [ ] T014 [P] [US1] Add unit tests for lexicon scoring in `tests/unit/test_sentiment.py`
- [ ] T015 [P] [US1] Add integration test that runs CLI against `data/sample_headlines.json` in `tests/integration/test_end_to_end.py`

### Implementation

- [ ] T016 [US1] Implement NewsAPI adapter in `src/headlines_sentiment/fetcher.py` using `requests` (honor `NEWSAPI_KEY` env var)
- [ ] T017 [US1] Implement lexicon scoring logic in `src/headlines_sentiment/sentiment.py` and include a small wordlist at `src/headlines_sentiment/data/lexicon.json`
- [ ] T018 [P] [US1] Implement plotting logic in `src/headlines_sentiment/plot.py` to create a bar chart PNG (`matplotlib`) and write CSV (`csv` module)
- [ ] T019 [US1] Wire CLI to run fetcher → sentiment → plot end-to-end in `src/headlines_sentiment/__main__.py`
- [ ] T020 [US1] Add error handling for API errors and rate limits, surface user-friendly messages (update `src/headlines_sentiment/fetcher.py` and `__main__.py`)
- [ ] T021 [US1] Add unit tests for fetcher and CLI argument parsing in `tests/unit/test_fetcher.py`, `tests/unit/test_cli.py`

**Checkpoint**: Running `python -m headlines_sentiment --category technology --sample 50 --out chart.png --csv counts.csv` produces expected files and tests pass.

---

## Phase 4: User Story 2 - Adjustable sample & refresh (Priority: P2)

Goal: Allow users to change the sample size and refresh results quickly.

Independent Test: Run CLI with different `--sample` values (20/50/100) and verify outputs match the requested sample size (or show returned count if fewer available).

- [ ] T022 [US2] Add `--sample` handling and validation in `src/headlines_sentiment/__main__.py`
- [ ] T023 [P] [US2] Add optional in-memory caching module `src/headlines_sentiment/cache.py` with TTL to avoid re-fetching within short intervals
- [ ] T024 [US2] Add tests for sample-size behavior and caching in `tests/unit/test_cli_params.py` and `tests/unit/test_cache.py`

---

## Phase 5: User Story 3 - Export & share (Priority: P3)

Goal: Allow exporting the chart as PNG and downloading raw counts as CSV.

Independent Test: Use CLI flags to generate PNG and CSV and verify file contents and format.

- [ ] T025 [US3] Implement `--csv` output generation (counts + metadata) in `src/headlines_sentiment/plot.py`
- [ ] T026 [US3] Implement `--out` PNG export and allow `--out-format` if needed in CLI
- [ ] T027 [US3] Add tests verifying CSV format and PNG file generation in `tests/unit/test_export.py`

---

## Phase N: Polish & Cross-Cutting Concerns

- [ ] T028 [P] Documentation updates: `docs/` plus update `specs/001-headlines-sentiment/quickstart.md` to final usage examples
- [ ] T029 [P] Code cleanup and refactoring (apply `ruff` fixes and formatting)
- [ ] T030 [P] Add more unit tests and increase coverage (target 80%+ for core modules)
- [ ] T031 Security: Add short security notes and checks for handling API keys (update `README.md` and `specs/001-headlines-sentiment/research.md`)
- [ ] T032 Create `CHANGELOG.md` and bump version in repository metadata if used

---

## Dependencies & Execution Order

- Phase 1 (Setup) must complete before Phase 2 (Foundational).
- Phase 2 must complete before any user story implementation (Phases 3–5).
- Within each story: Tests → Models/Modules → CLI/Endpoint → Integration.

### User Story Completion Order

1. US1 (P1) - MVP (blocks release)
2. US2 (P2)
3. US3 (P3)

### Parallel Opportunities

- Tasks marked `[P]` can be worked on in parallel (different files, low coupling). Examples: `T003`, `T004`, `T007`, `T008`, `T018`, `T023`, `T028`, `T029`.
- Different user stories (US1, US2, US3) can be implemented in parallel after foundational phase completes.

## Parallel Execution Example

Run in parallel:

- `T003` (style config) and `T004` (CI) and `T002` (requirements) — independent setup tasks.
- `T007` (sentiment module) and `T006` (fetcher skeleton) and `T008` (plot skeleton) — implementers can work concurrently.

## Implementation Strategy

- MVP First: Complete Phase 1 → Phase 2 → Phase 3 (US1) end-to-end. Validate with unit + integration tests and the quickstart example.
- Incremental Delivery: After MVP, deliver US2 and US3 in separate iterations, each with tests and docs.
- Keep abstractions minimal: follow YAGNI and DRY guidelines from the constitution — centralize shared logic only when duplication appears and is proven painful.

---

## Format Validation

All tasks follow the required checklist format: `- [ ] T### [P?] [US?] Description with file path`.
