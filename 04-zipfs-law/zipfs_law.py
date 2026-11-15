"""
NLP Experiment 04 — Zipf's Law

Pipeline:
  1. Load local text
  2. Preprocess (contractions, lowercase, alpha tokens, stopwords)
  3. Word frequencies → rank table + probabilities
  4. Log-rank / log-frequency Zipf plot + regression
  5. Top-N bar chart
  6. Cumulative distribution
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from contractions import fix
from matplotlib.colors import ListedColormap, Normalize
import matplotlib.cm as cm
from nltk import download
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from scipy.stats import linregress

BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data" / "ai_sample.txt"
IMAGES = BASE / "images"
IMAGES.mkdir(exist_ok=True)

for resource in ("punkt", "punkt_tab", "stopwords"):
    download(resource, quiet=True)


def load_text(file_path: Path | str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Text file not found: {path}")
    return path.read_text(encoding="utf-8")


def preprocess_text(text: str) -> list[str]:
    """Expand contractions, lowercase, keep alphabetic tokens, drop stopwords."""
    text = fix(text)
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    words = word_tokenize(text)
    stop = set(stopwords.words("english"))
    return [w for w in words if w not in stop and w.strip()]


def get_word_frequencies(text: str) -> Counter:
    return Counter(preprocess_text(text))


def create_word_dataframe(word_counts: Counter) -> pd.DataFrame:
    total_words = sum(word_counts.values())
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(sorted_counts, columns=["Word", "Frequency"])
    df["Rank"] = range(1, len(df) + 1)
    df["P(r)"] = df["Frequency"] / total_words
    df["r * P(r)"] = df["Rank"] * df["P(r)"]
    return df


def compute_log_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Log_Rank"] = np.log10(df["Rank"])
    df["Log_Frequency"] = np.log10(df["Frequency"])
    return df


def create_color_gradient(ranks: pd.Series):
    norm = Normalize(vmin=float(ranks.min()), vmax=float(ranks.max()))
    base_colors = cm.Greens(np.linspace(0.2, 0.9, 256))
    green_cmap = ListedColormap(base_colors)
    colors = [green_cmap(norm(rank)) for rank in ranks]
    return colors, green_cmap, norm


def save_fig(name: str) -> None:
    path = IMAGES / name
    plt.tight_layout()
    plt.savefig(path, dpi=120, bbox_inches="tight")
    print(f"Saved: {path}")
    try:
        plt.show()
    except Exception:
        pass
    plt.close()


def plot_zipfs_law(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    colors, green_cmap, norm = create_color_gradient(df["Rank"])

    scatter = plt.scatter(
        df["Log_Rank"],
        df["Log_Frequency"],
        c=df["Rank"],
        cmap=green_cmap,
        norm=norm,
        edgecolors="k",
        linewidths=0.5,
        alpha=0.7,
    )

    slope, intercept, *_ = linregress(df["Log_Rank"], df["Log_Frequency"])
    x = df["Log_Rank"]
    plt.plot(
        x,
        slope * x + intercept,
        color="red",
        linestyle="dashed",
        label=f"Regression (slope={slope:.3f})",
    )

    plt.xlabel("Rank (log10)")
    plt.ylabel("Frequency (log10)")
    plt.title("Zipf's Law: Word Frequency vs. Rank")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    cbar = plt.colorbar(scatter)
    cbar.set_label("Rank level")
    save_fig("01_zipf_loglog.png")


def plot_top_words(df: pd.DataFrame, top_n: int = 20) -> None:
    top = df.head(top_n)
    plt.figure(figsize=(12, 5))
    sns.barplot(
        x=top["Word"],
        y=top["Frequency"],
        hue=top["Word"],
        palette="viridis",
        legend=False,
    )
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title(f"Top {top_n} Most Frequent Words")
    save_fig("02_top_words.png")


def plot_cumulative_distribution(df: pd.DataFrame) -> None:
    df = df.copy()
    df["Cumulative_Frequency"] = df["Frequency"].cumsum()
    df["Cumulative_Percentage"] = (
        df["Cumulative_Frequency"] / df["Frequency"].sum() * 100
    )

    plt.figure(figsize=(10, 5))
    plt.plot(
        df["Rank"],
        df["Cumulative_Percentage"],
        marker="o",
        linestyle="-",
        markersize=3,
    )
    plt.xlabel("Rank")
    plt.ylabel("Cumulative Percentage")
    plt.title("Cumulative Distribution of Word Frequencies")
    plt.axhline(y=50, color="r", linestyle="--", label="50% Coverage")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    save_fig("03_cumulative.png")


def main() -> None:
    text_sample = load_text(DATA_PATH)
    word_counts = get_word_frequencies(text_sample)
    df = create_word_dataframe(word_counts)
    df = compute_log_values(df)

    plot_zipfs_law(df)
    plot_top_words(df)
    plot_cumulative_distribution(df)

    print("\nTop rows of rank–frequency table:")
    print(df.head(10).to_string(index=False))
    print(f"\nVocabulary size (unique words): {len(df)}")
    print(f"Total tokens (after preprocess): {int(df['Frequency'].sum())}")


if __name__ == "__main__":
    main()
