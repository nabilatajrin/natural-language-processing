"""
Experiment 07 — Part B
Semantic search on synthetic resumes using text embeddings + PCA.

Steps mirror the lab notebook:
  1. Synthetic resume / role table
  2. SentenceTransformer embeddings
  3. PCA to 2D
  4. Scatter by role
  5. Query → top-k cosine matches
  6. Plot query in PCA space
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity

IMAGES = Path(__file__).resolve().parent / "images"
IMAGES.mkdir(exist_ok=True)

DATA = {
    "resume": [
        "Experienced data scientist skilled in Python, SQL, and machine learning.",
        "AI researcher with a focus on natural language processing and large language models.",
        "Mobile app developer proficient in Flutter, Firebase, and Android development.",
        "Mechanical engineer experienced in CAD software and product design.",
        "Marketing specialist with expertise in SEO, content writing, and branding.",
        "Data engineer with Apache Airflow, Spark, and data pipeline design experience.",
        "AI product manager with a background in project leadership and ML deployment.",
        "Full-stack developer with JavaScript, React, Node.js, and database skills.",
        "Electrical engineer skilled in embedded systems and circuit design.",
        "UX designer with strong UI principles, Figma, and user research experience.",
    ],
    "role": [
        "Data Scientist",
        "AI Researcher",
        "Mobile Developer",
        "Mechanical Engineer",
        "Marketing Specialist",
        "Data Engineer",
        "AI Product Manager",
        "Full-stack Developer",
        "Electrical Engineer",
        "UX Designer",
    ],
}

DEFAULT_QUERY = "Looking for someone with Apache Airflow and data pipeline experience"


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


def main() -> None:
    df = pd.DataFrame(DATA)
    print("Resumes:")
    print(df.to_string(index=False))

    print("\nLoading SentenceTransformer('all-MiniLM-L6-v2')...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embedding_arr = model.encode(df["resume"].tolist())
    print("Embedding shape:", embedding_arr.shape)

    pca = PCA(n_components=2).fit(embedding_arr)
    reduced = pca.transform(embedding_arr)
    print("PCA explained variance ratio:", pca.explained_variance_ratio_)

    # --- Plot by role ---
    plt.figure(figsize=(10, 7))
    plt.grid(True, alpha=0.4)
    plt.title("Resume Embeddings by Role (PCA 2D)", fontsize=16)
    cmap = mpl.colormaps["tab10"]
    for i, role in enumerate(df["role"].unique()):
        idx = df["role"] == role
        plt.scatter(
            reduced[idx, 0],
            reduced[idx, 1],
            label=role,
            color=cmap(i % 10),
            s=80,
        )
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.xlabel("PC 1")
    plt.ylabel("PC 2")
    save_fig("01_resume_pca_by_role.png")

    # --- Semantic search ---
    query = DEFAULT_QUERY
    query_embedding = model.encode(query).reshape(1, -1)
    similarities = cosine_similarity(embedding_arr, query_embedding).flatten()
    top_matches = np.argsort(similarities)[-5:][::-1]

    print(f'\nQuery: "{query}"')
    print("\nTop matches:")
    for idx in top_matches:
        print(f"\nRole: {df['role'].iloc[idx]}")
        print(f"Resume: {df['resume'].iloc[idx]}")
        print(f"Similarity Score: {similarities[idx]:.3f}")

    # --- Query on PCA plot ---
    query_pca = pca.transform(query_embedding)[0]
    plt.figure(figsize=(10, 7))
    plt.grid(True, alpha=0.4)
    plt.title(f'Semantic Search Visualization\nQuery: "{query}"', fontsize=14)
    for i, role in enumerate(df["role"].unique()):
        idx = df["role"] == role
        plt.scatter(
            reduced[idx, 0],
            reduced[idx, 1],
            label=role,
            color=cmap(i % 10),
            s=80,
        )
    plt.scatter(
        query_pca[0],
        query_pca[1],
        color="black",
        marker="*",
        s=300,
        label="Query",
        zorder=5,
    )
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.xlabel("PC 1")
    plt.ylabel("PC 2")
    save_fig("02_semantic_search_query.png")

    print("\nDone. Change DEFAULT_QUERY in the script to try other searches.")


if __name__ == "__main__":
    main()
