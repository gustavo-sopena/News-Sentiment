import json
import os
from pathlib import Path
from typing import List, Dict, Optional

import requests


NEWSAPI_URL = "https://newsapi.org/v2/top-headlines"


def _normalize_article(article: Dict, category: str) -> Dict:
    title = article.get("title") or article.get("headline") or ""
    published = article.get("publishedAt") or article.get("published_at") or None
    url = article.get("url") or article.get("link") or ""
    source = (article.get("source") and article.get("source").get("name")) or article.get(
        "source"
    ) or "newsapi"
    return {
        "id": article.get("id") or url or title[:64],
        "source": source,
        "category": category,
        "title": title,
        "published_at": published,
        "url": url,
    }


def fetch_headlines(category: str, page_size: int = 50, api_key: Optional[str] = None) -> List[Dict]:
    """Fetch headlines from NewsAPI.org. If `api_key` is None or a request fails,
    fall back to bundled sample data for offline testing.
    Returns a list of normalized headline dicts.
    """
    # If no API key, use sample data
    if not api_key:
        return _load_sample(category, page_size)

    params = {"category": category, "pageSize": page_size, "language": "en"}
    headers = {"Authorization": api_key}
    try:
        resp = requests.get(NEWSAPI_URL, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        articles = data.get("articles") or []
        return [_normalize_article(a, category) for a in articles[:page_size]]
    except Exception:
        # Fallback to sample data
        return _load_sample(category, page_size)


def _load_sample(category: str, page_size: int) -> List[Dict]:
    base = Path(__file__).resolve().parents[1]
    sample_path = base / "data" / "sample_headlines.json"
    try:
        with open(sample_path, "r", encoding="utf-8") as f:
            arr = json.load(f)
            return [_normalize_article(a, category) for a in arr[:page_size]]
    except Exception:
        return []
