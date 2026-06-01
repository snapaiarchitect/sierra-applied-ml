import sys
from pathlib import Path

# Add src/ to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def test_imports():
    """Verify core src modules are importable."""
    import fetch_cmapss_data
    import load_nasa
    import evaluate
    assert True


def test_data_dir_exists():
    """Verify data directory structure exists."""
    data_dir = Path(__file__).parent.parent / "data"
    assert data_dir.exists()
    assert (data_dir / "raw").exists()


def test_raw_data_files_exist():
    """Verify NASA C-MAPSS raw data files are present."""
    raw_dir = Path(__file__).parent.parent / "data" / "raw"
    required_files = ["train_FD001.txt", "test_FD001.txt", "RUL_FD001.txt"]
    for f in required_files:
        assert (raw_dir / f).exists(), f"Missing: {f}"


def test_figures_dir_exists():
    """Verify figures directory exists."""
    figures_dir = Path(__file__).parent.parent / "figures"
    assert figures_dir.exists()


def test_results_json_exists():
    """Verify results.json is present and valid."""
    results_file = Path(__file__).parent.parent / "results.json"
    assert results_file.exists()
    import json
    with open(results_file) as f:
        data = json.load(f)
    assert "models" in data
    assert "dataset" in data


def test_execute_analysis_runs():
    """Verify execute_analysis.py can be imported and its create_features function works."""
    import pandas as pd
    from execute_analysis import create_features

    df = pd.DataFrame({
        "unit_number": [1, 1, 1, 2, 2, 2],
        "time_in_cycles": [1, 2, 3, 1, 2, 3],
        "sensor_2": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
        "sensor_3": [1.0, 1.1, 1.2, 2.0, 2.1, 2.2],
    })
    result = create_features(df, ["sensor_2", "sensor_3"], window=2)
    assert "sensor_2_rolling_mean" in result.columns
    assert "sensor_2_rolling_std" in result.columns
    assert "sensor_2_diff" in result.columns
    assert "cycle_norm" in result.columns
