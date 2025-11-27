# Phase 1 — Data Model

Entities derived from the spec:

- Headline
  - id: string (generated or source-provided)
  - source: string (e.g., NewsAPI)
  - category: string
  - title: string
  - published_at: datetime
  - url: string

- SentimentResult
  - headline_id: string (FK to Headline.id)
  - sentiment: enum {Positive, Neutral, Negative, Unknown}
  - score: float (optional raw score from lexicon scoring)

- ChartSummary
  - category: string
  - sample_size: integer
  - counts: object {positive: int, neutral: int, negative: int, unknown: int}
  - generated_at: datetime

Validation rules:
- Headline.title: required, non-empty, string length < 1024
- published_at: ISO-8601 datetime when available; may be null if not provided
- sentiment: one of the allowed enum values

State transitions:
- Raw Headline -> SentimentResult (after scoring)
- SentimentResult aggregated -> ChartSummary (read-only snapshot)
