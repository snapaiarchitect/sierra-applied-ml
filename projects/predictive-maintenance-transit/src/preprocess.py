"""
Data preprocessing module for predictive maintenance.
Handles data cleaning, feature engineering, and dataset preparation.
"""

from datetime import datetime
from typing import Optional, Tuple

import numpy as np
import pandas as pd


def load_transit_data(
    data_dir: str = "../data",
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load all transit datasets."""
    assets = pd.read_csv(f"{data_dir}/transit_assets.csv")
    assets["installation_date"] = pd.to_datetime(assets["installation_date"])
    assets["last_maintenance"] = pd.to_datetime(assets["last_maintenance"])

    failures = pd.read_csv(f"{data_dir}/failure_history.csv")
    failures["failure_date"] = pd.to_datetime(failures["failure_date"])
"""DEPRECATED: preprocess

This module has been archived and moved to `archive/preprocess.py` as part of
a code-quality cleanup. The top-level module re-exports the archived
implementation to preserve import compatibility for callers.
"""

from .archive.preprocess import *  # noqa: F401,F403

