import json
import os
from pathlib import Path

MAIN_NB = Path(
    "projects/predictive-maintenance-transit/notebooks/predictive_maintenance_analysis.ipynb"
)
UNTITLED_NB = Path("projects/predictive-maintenance-transit/notebooks/Untitled-2.ipynb")


def load_nb(path):
    with open(path, "r") as f:
        return json.load(f)


def save_nb(nb, path):
    with open(path, "w") as f:
        json.dump(nb, f, indent=1)


eval_def = [
    "def evaluate_model(name, true, pred):\n",
    "    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\n",
    "    import numpy as np\n",
    "    mae = mean_absolute_error(true, pred)\n",
    "    rmse = np.sqrt(mean_squared_error(true, pred))\n",
    "    r2 = r2_score(true, pred)\n",
    '    print(f"{name} Results:")\n',
    '    print(f"  MAE: {mae:.2f}")\n',
    '    print(f"  RMSE: {rmse:.2f}")\n',
    '    print(f"  R2:   {r2:.3f}")\n',
    "    return {'MAE': mae, 'RMSE': rmse, 'R2': r2}\n",
]

summary_cell = [
    "rf_metrics = evaluate_model('Random Forest', true_rul, rf_pred)\n",
    "xgb_metrics = evaluate_model('XGBoost', true_rul, xgb_pred)\n",
    "\n",
    "import pandas as pd\n",
    "metrics_df = pd.DataFrame([\n",
    "    {'Model': 'Random Forest', **rf_metrics},\n",
    "    {'Model': 'XGBoost', **xgb_metrics}\n",
    "])\n",
    "print('\\n--- Comparison ===')\n",
    "print(metrics_df.round(2).to_string(index=False))\n",
]


def patch(path):
    if not path.exists():
        print(f"Skipping {path}, not found.")
        return
    nb = load_nb(path)
    # Insert eval def after imports (usually cell 1 or 2)
    nb["cells"].insert(
        2,
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": eval_def,
        },
    )

    # Update summary cell
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and any(
            "rf_metrics =" in line for line in cell["source"]
        ):
            cell["source"] = summary_cell

    save_nb(nb, path)
    print(f"Successfully patched {path}")


if __name__ == "__main__":
    patch(MAIN_NB)
    patch(UNTITLED_NB)
