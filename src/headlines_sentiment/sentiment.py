import json
from pathlib import Path


def _load_lexicon() -> tuple[set, set]:
    base = Path(__file__).resolve().parents[1]
    lex_path = base / 'data' / 'lexicon.json'
    try:
        with open(lex_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            pos = set(w.lower() for w in data.get('positive', []))
            neg = set(w.lower() for w in data.get('negative', []))
            return pos, neg
    except Exception:
        # minimal defaults
        return {'good', 'great', 'positive', 'up'}, {'bad', 'sad', 'negative', 'down'}


_POS, _NEG = _load_lexicon()


def score_headline(text: str) -> tuple[str, int]:
    """Simple lexicon-based scoring. Returns (sentiment_label, score).

    score > 0 => Positive
    score == 0 => Neutral
    score < 0 => Negative
    """
    if not text:
        return 'Unknown', 0

    words = [w.strip('.,!?:;"\'()[]') for w in text.lower().split()]
    score = 0
    for w in words:
        if w in _POS:
            score += 1
        if w in _NEG:
            score -= 1

    if score > 0:
        return 'Positive', score
    if score < 0:
        return 'Negative', score
    return 'Neutral', score
