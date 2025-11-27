# Quickstart: Headlines Sentiment CLI

Requirements

- Python 3.11+
- `NEWSAPI_KEY` environment variable set (register at https://newsapi.org)
- Install dependencies (recommended in a venv):

```bash
python -m venv .venv
source .venv/bin/activate
pip install requests matplotlib ruff pytest
```

Run (example):

```bash
export NEWSAPI_KEY="your_api_key_here"
python -m headlines_sentiment --category technology --sample 50 --out chart.png --csv counts.csv
```

Output:

- `chart.png`: bar chart showing counts for Positive/Neutral/Negative
- `counts.csv`: optional CSV with counts and metadata

Notes:

- The CLI respects basic rate limits and will surface informative errors
  for 401/429 responses from NewsAPI.
- For development, you can run unit tests with `pytest`.
