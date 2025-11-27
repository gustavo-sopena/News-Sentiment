import json
from pathlib import Path
from typing import Final, Any

import requests


NEWSAPI_URL: Final[str] = 'https://newsapi.org/v2/top-headlines'


def _normalize_article(article: dict, category: str) -> dict:
    title = article.get('title') or article.get('headline') or ''
    published = article.get('publishedAt') or article.get('published_at') or None
    url = article.get('url') or article.get('link') or ''
    source = (
        (article.get('source') and article.get('source').get('name'))
        or article.get('source')
        or 'newsapi'
    )
    return {
        'id': article.get('id') or url or title[:64],
        'source': source,
        'category': category,
        'title': title,
        'published_at': published,
        'url': url,
    }


def fetch_headlines(
    category: str, page_size: int = 50, api_key: str | None = None
) -> list[dict[Any, Any]]:
    """Fetch headlines from NewsAPI.org. If `api_key` is None or a request fails,
    fall back to bundled sample data for offline testing.
    Returns a list of normalized headline dicts.
    """
    # If no API key, use sample data
    if not api_key:
        return _load_sample(category, page_size)

    params: dict[str, str | int] = {
        'category': category,
        'pageSize': page_size,
        'language': 'en',
    }
    headers: dict[str, str] = {'Authorization': api_key}
    try:
        resp: requests.Response = requests.get(
            NEWSAPI_URL, params=params, headers=headers, timeout=10
        )
        resp.raise_for_status()
        data: dict[str, Any] = resp.json()
        articles = data.get('articles') or []
        return [_normalize_article(a, category) for a in articles[:page_size]]
    except Exception:
        # Fallback to sample data
        return _load_sample(category, page_size)


def _load_sample(category: str, page_size: int) -> list[dict[Any, Any]]:
    base = Path(__file__).resolve().parents[1]
    sample_path = base / 'data' / 'sample_headlines.json'
    try:
        with open(sample_path, 'r', encoding='utf-8') as f:
            arr = json.load(f)
            return [_normalize_article(a, category) for a in arr[:page_size]]
    except Exception:
        return []
