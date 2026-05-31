import json
from pathlib import Path
path = Path('projects/predictive-maintenance-transit/notebooks/predictive_maintenance_analysis.ipynb')
nb = json.loads(path.read_text())

cell_18 = [
    'def evaluate_model(name, y_true, y_pred):\n',
    '    mae = mean_absolute_error(y_true, y_pred)\n',
    '    rmse = np.sqrt(mean_squared_error(y_true, y_pred))\n',
    '    r2 = r2_score(y_true, y_pred)\n',
    '\n',
    '    print(f"\\n=== {name} ===")\n',
    '    print(f"  MAE:  {mae:.2f} cycles")\n',
    '    print(f"  RMSE: {rmse:.2f} cycles")\n',
    '    print(f"  R2:   {r2:.3f}\")\n',
    '\n',
    '    return {\'MAE\': mae, \'RMSE\': rmse, \'R2\': r2}\n',
    '\n',
    '# Baseline: predict mean RUL of training set for all test engines\n',
    'mean_rul_train = y_train.mean()\n',
    'y_baseline = np.full_like(y_test, fill_value=mean_rul_train, dtype=float)\n',
    '\n',
    'baseline_metrics = evaluate_model(\'Mean RUL Baseline\', y_test, y_baseline)\n',
    'print(f"Baseline: predict mean RUL = {mean_rul_train:.1f} cycles for every engine")\n',
]
cell_20 = [
    "rf_metrics = evaluate_model('Random Forest', true_rul, rf_pred)\n",
    "xgb_metrics = evaluate_model('XGBoost', true_rul, xgb_pred)\n",
    '\n',
    '# Summary table\n',
    'metrics_df = pd.DataFrame([\n',
    "    {'Model': 'Random Forest', **rf_metrics},\n",
    "    {'Model': 'XGBoost', **xgb_metrics}\n",
    '])\n',
    'print(\\'\\n=== Comparison ===\\')\n',
    'print(metrics_df.round(2).to_string(index=False))\n',
]

nb['cells'][17]['source'] = cell_18
nb['cells'][19]['source'] = cell_20
path.write_text(json.dumps(nb, indent=1))
print('patch applied')
