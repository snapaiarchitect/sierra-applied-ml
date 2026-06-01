"""DEPRECATED: survival_model

This module has been archived and moved to `archive/survival_model.py` as part of
a code-quality refactor. The original implementation is preserved in the
`archive` package; the top-level module re-exports the archived symbols to
preserve import compatibility.
"""

# Re-export archived implementation to preserve backwards compatibility
from .archive.survival_model import *  # noqa: F401,F403
        raise ValueError("Log-rank test requires exactly 2 groups")

    mask_a = df[group_col] == groups[0]
    mask_b = df[group_col] == groups[1]

    T_a = df.loc[mask_a, duration_col] / 365.25
    T_b = df.loc[mask_b, duration_col] / 365.25
    E_a = df.loc[mask_a, event_col]
    E_b = df.loc[mask_b, event_col]

    result = logrank_test(T_a, T_b, event_observed_A=E_a, event_observed_B=E_b)

    return {
        "test_statistic": result.test_statistic,
        "p_value": result.p_value,
        "significant": result.p_value < 0.05,
    }


if __name__ == "__main__":
    # Test survival model
    df = pd.read_csv("../data/processed_features.csv")

    print("Fitting Cox PH model...")
    model = SurvivalModel(model_type="cox")
    model.fit(df)

    summary = model.get_summary()
    print(f"C-index: {summary['concordance_index']:.3f}")
    print(f"AIC: {summary['AIC']:.2f}")

    # Predict risk scores
    risk_scores = model.predict_risk(df)
    print(f"Risk scores: mean={risk_scores.mean():.3f}, std={risk_scores.std():.3f}")
