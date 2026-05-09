"""
Synthetic data generator for demand forecasting operations.
Creates realistic operational demand patterns based on BLS/BTS workforce patterns.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
random.seed(99)
np.random.seed(99)


def generate_hourly_demand(start_date='2023-01-01', days=730):
    """Generate hourly operational demand data."""
    dates = pd.date_range(start=start_date, periods=days*24, freq='H')
    
    # Base demand pattern
    hour = dates.hour
    day_of_week = dates.dayofweek
    month = dates.month
    
    # Rush hour peaks (7-9 AM, 5-7 PM)
    rush_morning = ((hour >= 7) & (hour <= 9)).astype(int)
    rush_evening = ((hour >= 17) & (hour <= 19)).astype(int)
    off_peak = 1 - rush_morning - rush_evening
    
    # Weekend reduction
    weekend_factor = np.where(day_of_week >= 5, 0.7, 1.0)
    
    # Seasonal pattern (summer higher)
    seasonal = 1 + 0.15 * np.sin(2 * np.pi * (month - 1) / 12)
    
    # Base demand
    base_demand = 1000 + 500 * rush_morning + 400 * rush_evening + 200 * off_peak
    demand = base_demand * weekend_factor * seasonal
    
    # Add noise
    demand += np.random.normal(0, 50, len(dates))
    demand = np.maximum(demand, 200).astype(int)
    
    # Overtime hours (correlates with demand spikes)
    overtime = np.where(demand > 1500, 
                        (demand - 1500) / 50 + np.random.normal(0, 5, len(dates)),
                        np.random.normal(2, 1, len(dates)))
    overtime = np.maximum(overtime, 0)
    
    # Staff needed (based on demand)
    staff_needed = (demand / 50 + np.random.normal(0, 2, len(dates))).astype(int)
    staff_needed = np.maximum(staff_needed, 10)
    
    # Weather severity (1-5 scale)
    weather = np.random.choice([1, 2, 3, 4, 5], len(dates), 
                              p=[0.5, 0.25, 0.15, 0.08, 0.02])
    
    # Service calls (correlates with weather)
    service_calls = (10 + weather * 5 + np.random.poisson(3, len(dates)))
    
    # Equipment usage
    equipment_hours = (demand / 100 + np.random.normal(0, 1, len(dates)))
    
    df = pd.DataFrame({
        'datetime': dates,
        'hour': hour,
        'day_of_week': day_of_week,
        'month': month,
        'is_holiday': np.random.random(len(dates)) < 0.05,
        'demand': demand,
        'overtime_hours': overtime.round(1),
        'staff_needed': staff_needed,
        'weather_severity': weather,
        'service_calls': service_calls,
        'equipment_usage_hours': equipment_hours.round(1)
    })
    
    return df


def generate_monthly_budget(start_date='2023-01-01', months=24):
    """Generate monthly budget data."""
    dates = pd.date_range(start=start_date, periods=months, freq='MS')
    
    categories = ['Labor', 'Equipment', 'Facilities', 'Technology', 'Training']
    
    data = []
    for date in dates:
        for category in categories:
            # Base budget with growth
            months_elapsed = (date.year - 2023) * 12 + date.month
            base = 50000 + months_elapsed * 1000
            
            if category == 'Labor':
                base *= 2.5
            elif category == 'Equipment':
                base *= 1.2
            
            budget = base + np.random.normal(0, base * 0.05)
            actual = budget * (1 + np.random.normal(0, 0.08))
            
            data.append({
                'month': date,
                'category': category,
                'budget_allocated': round(budget, 2),
                'actual_spent': round(actual, 2),
                'variance_pct': round((actual - budget) / budget * 100, 2),
                'fte_count': int(50 + np.random.normal(0, 3)) if category == 'Labor' else 0
            })
    
    return pd.DataFrame(data)


def generate_weekly_metrics(start_date='2023-01-02', weeks=104):
    """Generate weekly workforce metrics."""
    # Start on Monday
    dates = pd.date_range(start=start_date, periods=weeks, freq='W-MON')
    
    headcount = 100
    data = []
    
    for i, date in enumerate(dates):
        # Slow growth
        headcount += np.random.choice([0, 1], p=[0.7, 0.3])
        
        # Turnover (monthly pattern - higher in Jan and Dec)
        month = date.month
        base_turnover = 0.02
        if month in [1, 12]:
            base_turnover += 0.01
        
        turnover = base_turnover + np.random.normal(0, 0.005)
        turnover = max(0, min(0.1, turnover))
        
        # Overtime ratio (correlates with demand seasonality)
        quarter = (month - 1) // 3
        base_overtime = 0.15 + quarter * 0.02
        overtime = base_overtime + np.random.normal(0, 0.03)
        overtime = max(0, min(0.5, overtime))
        
        # Productivity index
        productivity = 100 + np.random.normal(0, 5)
        productivity -= overtime * 10  # Overtime reduces productivity
        
        # Safety incidents (inverse to training spend)
        safety = max(0, np.random.poisson(2))
        
        # Training hours
        training = 4 + np.random.normal(0, 1)
        training = max(0, training)
        
        data.append({
            'week_start': date,
            'headcount': headcount,
            'new_hires': max(0, int(np.random.poisson(1))),
            'terminations': max(0, int(headcount * turnover)),
            'turnover_rate': round(turnover, 4),
            'overtime_ratio': round(overtime, 4),
            'productivity_index': round(productivity, 2),
            'safety_incidents': safety,
            'training_hours_per_employee': round(training, 2)
        })
    
    return pd.DataFrame(data)


def generate_all_data(output_dir='../data'):
    """Generate all synthetic datasets."""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating hourly demand data...")
    hourly = generate_hourly_demand()
    hourly.to_csv(f'{output_dir}/hourly_demand.csv', index=False)
    print(f"  {len(hourly):,} records")
    
    print("Generating monthly budget data...")
    monthly = generate_monthly_budget()
    monthly.to_csv(f'{output_dir}/monthly_budget.csv', index=False)
    print(f"  {len(monthly)} records")
    
    print("Generating weekly workforce metrics...")
    weekly = generate_weekly_metrics()
    weekly.to_csv(f'{output_dir}/weekly_metrics.csv', index=False)
    print(f"  {len(weekly)} records")
    
    print("\nDataset summary:")
    print(f"  Hourly demand: {hourly['demand'].mean():.0f} avg, {hourly['demand'].max()} max")
    print(f"  Monthly budget: {monthly['budget_allocated'].sum():,.0f} total")
    print(f"  Weekly headcount: {weekly['headcount'].iloc[-1]} current")
    print("\nData generation complete.")
    
    return hourly, monthly, weekly


if __name__ == '__main__':
    print("Generating demand forecasting synthetic data...")
    generate_all_data('../data')
