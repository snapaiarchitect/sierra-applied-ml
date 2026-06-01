import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def test_imports():
    """Verify all src modules are importable."""
    import evaluate
    import fetch_bike_data
    import forecast
    import load_bike
    import preprocess

    assert True


def test_data_dir_exists():
    """Verify data directory structure exists."""
    data_dir = Path(__file__).parent.parent / "data"
    assert data_dir.exists()
    assert (data_dir / "raw").exists()


def test_raw_data_files_exist():
    """Verify UCI Bike Sharing raw data files are present."""
    raw_dir = Path(__file__).parent.parent / "data" / "raw"
    required_files = ["hour.csv", "day.csv", "Readme.txt"]
    for f in required_files:
        assert (raw_dir / f).exists(), f"Missing: {f}"


def test_figures_dir_exists():
    """Verify figures directory exists."""
    figures_dir = Path(__file__).parent.parent / "figures"
    assert figures_dir.exists()


def test_results_json_exists():
    """Verify results.json is present and valid."""
    import json

    results_file = Path(__file__).parent.parent / "results.json"
    assert results_file.exists()
    with open(results_file) as f:
        data = json.load(f)
    assert "models" in data
    assert "xgboost" in data["models"]
    # MAPE is stored as percentage in results.json; compare accordingly
    assert data["models"]["xgboost"]["mape"] < 100.0
    assert data["models"]["xgboost"]["mape"] > 0.0


def test_data_dictionary_exists():
    """Verify DATA_DICTIONARY.md is present."""
    dd_file = Path(__file__).parent.parent / "data" / "DATA_DICTIONARY.md"
    assert dd_file.exists()
    content = dd_file.read_text()
    assert "UCI" in content
    assert "Bike Sharing" in content


def test_create_lag_features_produces_expected_columns():
    """Verify lag feature engineering creates correct columns."""
    import pandas as pd
    from preprocess import create_lag_features

    df = pd.DataFrame(
        {
            "datetime": pd.date_range("2023-01-01", periods=5, freq="h"),
            "cnt": [1.0, 2.0, 3.0, 4.0, 5.0],
        }
    )
    result = create_lag_features(df, target_col="cnt", lags=[1, 2])
    assert "cnt_lag_1" in result.columns
    assert "cnt_lag_2" in result.columns
    assert result["cnt_lag_1"].iloc[2] == 2.0
    assert result["cnt_lag_2"].iloc[2] == 1.0


def test_split_time_series_respects_temporal_order():
    """Verify time-series split does not leak future data."""
    import pandas as pd
    from preprocess import split_time_series

    df = pd.DataFrame(
        {
            "datetime": pd.date_range("2023-01-01", periods=100, freq="h"),
            "cnt": range(100),
        }
    )
    train, test = split_time_series(df, test_days=1)
    assert train["datetime"].max() < test["datetime"].min()
    assert len(test) <= 24
