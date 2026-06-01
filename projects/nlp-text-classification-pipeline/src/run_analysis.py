"""
End-to-end NLP text classification analysis.
Fetches 20 Newsgroups, vectorizes with TF-IDF, trains multiple models,
and writes results in the canonical schema expected by dashboards and tests.
"""

import json

from sklearn.datasets import fetch_20newsgroups
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC


def main() -> None:
    # Load dataset using canonical sklearn train/test split (no leakage)
    train_data = fetch_20newsgroups(
        subset="train",
        remove=("headers", "footers", "quotes"),
        shuffle=True,
        random_state=42,
    )
    test_data = fetch_20newsgroups(
        subset="test",
        remove=("headers", "footers", "quotes"),
        shuffle=True,
        random_state=42,
    )
    X_train, y_train = train_data.data, train_data.target
    X_test, y_test = test_data.data, test_data.target

    # Vectorize text
    vectorizer = TfidfVectorizer(
        stop_words="english", max_features=5000, ngram_range=(1, 2), sublinear_tf=True
    )
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Define models
    models = {
        "naive_bayes": MultinomialNB(),
        "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
        "linear_svm": LinearSVC(random_state=42),
    }

    # Train and evaluate
    model_results = {}
    for name, model in models.items():
        model.fit(X_train_tfidf, y_train)
        y_pred = model.predict(X_test_tfidf)
        model_results[name] = {
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(
                precision_score(y_test, y_pred, average="weighted", zero_division=0)
            ),
            "recall": float(
                recall_score(y_test, y_pred, average="weighted", zero_division=0)
            ),
            "f1": float(f1_score(y_test, y_pred, average="weighted", zero_division=0)),
        }

    # Write results in canonical nested schema
    results = {
        "version": "2.0.0",
        "project": "nlp-text-classification-pipeline",
        "dataset": {
            "source": "20 Newsgroups (sklearn.datasets)",
            "url": "https://scikit-learn.org/stable/datasets/twenty_newsgroups.html",
            "records": len(train_data.data) + len(test_data.data),
            "train_samples": len(train_data.data),
            "test_samples": len(test_data.data),
            "n_categories": len(train_data.target_names),
            "citation": "Lang, K. (1995). Newsweeder: Learning to filter netnews. ICML 1995.",
        },
        "models": model_results,
        "feature_engineering": {
            "vectorizer": "TfidfVectorizer",
            "max_features": 5000,
            "ngram_range": "(1, 2)",
            "sublinear_tf": True,
            "stop_words": "english",
        },
        "status": "complete",
        "executed": True,
    }

    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Analysis complete. Results saved to results.json")


if __name__ == "__main__":
    main()
