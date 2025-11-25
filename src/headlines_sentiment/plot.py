from typing import Dict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv


def plot_counts(counts: Dict[str, int], out_path: str, title: str = "Sentiment") -> None:
    labels = list(counts.keys())
    values = [counts[k] for k in labels]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(labels, values, color=["#2ca02c", "#1f77b4", "#d62728", "#7f7f7f"][: len(labels)])
    ax.set_title(title)
    ax.set_ylabel("Count")
    for i, v in enumerate(values):
        ax.text(i, v + 0.1, str(v), ha="center")
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)


def write_csv_counts(counts: Dict[str, int], csv_path: str, category: str = "", sample_size: int = 0) -> None:
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "sample_size", "positive", "neutral", "negative", "unknown"])
        writer.writerow([
            category,
            sample_size,
            counts.get("Positive", 0),
            counts.get("Neutral", 0),
            counts.get("Negative", 0),
            counts.get("Unknown", 0),
        ])
