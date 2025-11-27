# Phase 0 — Research: Headlines Sentiment Chart

Decision: Use NewsAPI.org for headlines, implement a CLI Python tool, and
use a lexicon-based sentiment analyzer.

Rationale:
- NewsAPI.org: Provides consistent, structured JSON responses and category
  filters which simplify parsing and reduce early integration work. Using a
  single provider (with pluggable adapters later) accelerates the prototype.
- CLI Python tool: Fast to implement and lightweight. The user requested a
  minimal-dependency solution and selected CLI; this also supports automation
  and reproducible runs in CI.
- Lexicon-based sentiment: No heavy ML or external inference dependencies,
  deterministic and easy to unit test. Good for initial iteration and
  sufficient for trend-level analysis.

Alternatives considered:
- Public RSS feeds: No API key required, but feeds vary widely in structure and
  category naming. Considered but deferred for initial implementation.
- Pretrained ML model / cloud inference: Higher accuracy but requires more
  infra and increases maintenance burden. Recommended as a follow-up if
  lexicon accuracy is insufficient.

Implementation notes:
- Store API key in `NEWSAPI_KEY` environment variable.
- Use `requests` for HTTP; respect rate limits and implement basic retry
 /backoff and informative error messages.
- Prepare a small English lexicon (positive/negative word lists) and
  thresholding for classification. Mark non-English headlines as Unknown using
  a lightweight language-detection heuristic.
