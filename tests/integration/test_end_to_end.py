import tempfile
import os
from headlines_sentiment.fetcher import fetch_headlines
from headlines_sentiment.sentiment import score_headline
from headlines_sentiment.plot import plot_counts, write_csv_counts


def test_end_to_end_creates_outputs(tmp_path):
    # Ensure no NEWSAPI_KEY so fetcher uses sample data
    os.environ.pop("NEWSAPI_KEY", None)
    headlines = fetch_headlines("technology", 10, api_key=None)
    counts = {"Positive": 0, "Neutral": 0, "Negative": 0, "Unknown": 0}
    for h in headlines:
        label, _ = score_headline(h.get("title", ""))
        counts[label] = counts.get(label, 0) + 1

    out_png = str(tmp_path / "chart.png")
    out_csv = str(tmp_path / "counts.csv")
    plot_counts(counts, out_png, title="Test Chart")
    write_csv_counts(counts, out_csv, category="technology", sample_size=len(headlines))

    assert os.path.exists(out_png)
    assert os.path.exists(out_csv)
