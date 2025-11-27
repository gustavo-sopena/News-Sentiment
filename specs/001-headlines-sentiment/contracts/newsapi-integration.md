# Contracts: NewsAPI Integration (informal)

Purpose: Document the expected interaction with the external NewsAPI.org
service for fetching headlines.

Endpoint (example):

- GET https://newsapi.org/v2/top-headlines
  - Query params: `category` (string), `pageSize` (int), `apiKey` (string via header or env)
  - Response (success): JSON object containing `articles` array, where each
    article includes at minimum `title`, `publishedAt`, `url`, and `source`.

Minimal adapter contract (pseudo-schema):

Request:

{
  "category": "technology",
  "pageSize": 50
}

Response (normalized to our internal Headline model):

[
  {
    "id": "source-12345",
    "source": "newsapi",
    "category": "technology",
    "title": "Example headline text...",
    "published_at": "2025-11-23T12:34:56Z",
    "url": "https://example.com/article"
  },
  ...
]

Errors:
- 401 Unauthorized: invalid or missing API key
- 429 Too Many Requests: rate limited — implement retry/backoff or surface
  to user
- 5xx: upstream failure — surface to user with suggestion to retry later

Notes:
- The implementation must normalize incoming fields to the internal model
  and handle missing fields gracefully (e.g., missing `publishedAt`).
