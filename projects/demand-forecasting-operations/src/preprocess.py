"""
Data preprocessing module for demand forecasting operations.
Handles time series cleaning, feature engineering, and dataset preparation.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Tuple, Optional, List


def load_demand_data(data_dir: str = '../data') -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load all demand forecasting datasets."""
    hourly = pd.read_csv(f'{data_dir}/hourly_demand.csv', parse_dates=['datetime'])
    monthly = pd.read_csv(f'{data_dir}/monthly_budget.csv')
    weekly = pd.read_csv(f'{data_dir}/weekly_metrics.csv', parse_dates=['week_start'])
    
    return hourly, monthly, weekly


def aggregate_to_daily(hourly: pd.DataFrame) -> pd.DataFrame:
    """Aggregate hourly data to daily level."""
    daily = hourly.set_index('datetime').resample('D').agg({
        'demand': 'sum',
        'overtime_hours': 'sum',
        'staff_needed': 'sum',
        'weather_severity': 'mean',
        'service_calls': 'sum',
        'equipment_usage_hours': 'sum'
    })
    
    return daily.reset_index()


def create_time_features(df: pd.DataFrame, datetime_col: str = 'datetime') -> pd.DataFrame:
    """Create time-based features."""
    df = df.copy()
    
    if pd.api.types.is_datetime64_any_dtype(df[datetime_col]):
        dt = df[datetime_col]
    else:
        dt = pd.to_datetime(df[datetime_col])
    
    # Basic time features
    df['day_of_week'] = dt.dt.dayofweek
    df['month'] = dt.dt.month
    df['day_of_month'] = dt.dt.day
    df['week_of_year'] = dt.dt.isocalendar().week.astype(int)
    df['is_weekend'] = (dt.dt.dayofweek >= 5).astype(int)
    df['quarter'] = dt.dt.quarter
    df['year'] = dt.dt.year
    
    # Cyclical encodings
    df['hour_sin'] = np.sin(2 * np.pi * dt.dt.hour / 24)
    df['hour_cos'] = np.cos(2 * np.pi * dt.dt.hour / 24)
    df['dow_sin'] = np.sin(2 * np.pi * dt.dt.dayofweek / 7)
    df['dow_cos'] = np.cos(2 * np.pi * dt.dt.dayofweek / 7)
    df['month_sin'] = np.sin(2 * np.pi * dt.dt.month / 12)
    df['month_cos'] = np.cos(2 * np.pi * dt.dt.month / 12)
    
    return df


def create_lag_features(df: pd.DataFrame, target_col: str = 'demand',
                       lags: List[int] = [1, 2, 3, 7, 14]) -> pd.DataFrame:
    """Create lag features for time series."""
    df = df.copy()
    
    for lag in lags:
        df[f'{target_col}_lag_{lag}'] = df[target_col].shift(lag)
    
    return df


def create_rolling_features(df: pd.DataFrame, target_col: str = 'demand',
                           windows: List[int] = [7, 14, 30]) -> pd.DataFrame:
    """Create rolling window statistics."""
    df = df.copy()
    
    for window in windows:
        df[f'{target_col}_roll_mean_{window}'] = df[target_col].shift(1).rolling(window=window, min_periods=1).mean()
        df[f'{target_col}_roll_std_{window}'] = df[target_col].shift(1).rolling(window=window, min_periods=1).std()
        df[f'{target_col}_roll_max_{window}'] = df[target_col].shift(1).rolling(window=window, min_periods=1).max()
        df[f'{target_col}_roll_min_{window}'] = df[target_col].shift(1).rolling(window=window, min_periods=1).min()
    
    return df


def prepare_forecasting_features(df: pd.DataFrame, target_col: str = 'demand') -> pd.DataFrame:
    """Full feature engineering pipeline for forecasting."""
    # Time features
    if 'datetime' in df.columns:
        df = create_time_features(df)
    
    # Lag features
    df = create_lag_features(df, target_col)
    
    # Rolling features
    df = create_rolling_features(df, target_col)
    
    # Drop rows with NaN from lags
    df = df.dropna()
    
    return df


def split_time_series(df: pd.DataFrame, test_days: int = 30,
                     datetime_col: str = 'datetime') -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Split time series into train/test sets."""
    if datetime_col in df.columns:
        df = df.sort_values(datetime_col)
    
    split_idx = len(df) - test_days
    train = df.iloc[:split_idx].copy()
    test = df.iloc[split_idx:].copy()
    
    return train, test


def detect_anomalies(df: pd.DataFrame, target_col: str = 'demand',
                    threshold: float = 3.0) -> pd.DataFrame:
    """Detect anomalies using Z-score method."""
    df = df.copy()
    
    mean = df[target_col].mean()
    std = df[target_col].std()
    
    df['z_score'] = (df[target_col] - mean) / std
    df['is_anomaly'] = np.abs(df['z_score']) > threshold
    
    return df


def save_processed_data(df: pd.DataFrame, output_path: str):
    """Save processed dataframe."""
    df.to_csv(output_path, index=False)
    print(f"Saved processed data to: {output_path}")


if __name__ == '__main__':
    # Test preprocessing pipeline
    print("Testing demand forecasting preprocessing...")
    
    # Create sample data
    dates = pd.date_range('2023-01-01', periods=100, freq='D')
    sample = pd.DataFrame({
        'datetime': dates,
        'demand': np.random.randint(1000, 5000, 100),
        'weather_severity': np.random.randint(1, 5, 100)
    })
    
    processed = prepare_forecasting_features(sample)
    print(f"Original shape: {sample.shape}")
    print(f"Processed shape: {processed.shape}")
    print(f"New features: {[c for c in processed.columns if c not in sample.columns]}")
    print("\nPreprocessing module ready.")
