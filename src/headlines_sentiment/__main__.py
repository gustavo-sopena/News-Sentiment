import argparse
import os

from .fetcher import fetch_headlines
from .sentiment import score_headline
from .plot import plot_counts, write_csv_counts


def main() -> None:
    parser = argparse.ArgumentParser(description='Headlines Sentiment CLI')
    parser.add_argument(
        '--category',
        required=True,
        help='News category to fetch',
        choices=[
            'business',
            'entertainment',
            'general',
            'health',
            'science',
            'sports',
            'technology',
        ],
    )
    parser.add_argument(
        '--sample', type=int, default=50, help='Number of headlines to analyze'
    )
    parser.add_argument('--out', default='chart.png', help='Output PNG path')
    parser.add_argument('--csv', default=None, help='Optional CSV output path')
    args: argparse.Namespace = parser.parse_args()

    api_key: str | None = os.environ.get('NEWSAPI_KEY')

    headlines = fetch_headlines(
        args.category,
        args.sample,
        api_key=api_key
    )
    counts: dict[str, int] = {'Positive': 0, 'Neutral': 0, 'Negative': 0, 'Unknown': 0}
    for h in headlines:
        sentiment, _ = score_headline(h.get('title', ''))
        counts[sentiment] = counts.get(sentiment, 0) + 1

    # Plot and optional CSV
    plot_counts(counts, args.out, title=f'Sentiment for {args.category}')
    if args.csv:
        write_csv_counts(
            counts, args.csv, category=args.category, sample_size=len(headlines)
        )


if __name__ == '__main__':
    main()
