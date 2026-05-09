"""
Synthetic operational demand data generator.
Creates realistic workforce and operational demand data.

Patterns based on:
- Bureau of Labor Statistics (BLS) employment trends
- Bureau of Transportation Statistics (BTS) operational data
- WMATA overtime and workforce patterns
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os


def generate_hourly_demand(days=730, random_state=42):
    """Generate synthetic hourly operational demand data (2 years)."""
    np.random.seed(random_state)
    
    base_date = datetime(2023, 1, 1)
    records = []
    
    for day in range(days):
        date = base_date + timedelta(days=day)
        
        # Seasonal patterns
        month = date.month
        seasonal_factor = 1 + 0.15 * np.sin(2 * np.pi * month / 12)
        
        # Day of week patterns (weekdays higher)
        dow = date.weekday()
        dow_factor = 1.3 if dow < 5 else 0.8
        
        # Trend (slow growth)
        trend = 1 + (day / days) * 0.08
        
        for hour in range(24):
            # Hourly patterns (rush hours, lunch, overnight)
            if 6 <= hour < 9:
                hour_factor = 1.8  # Morning rush
            elif 9 <= hour < 12:
                hour_factor = 1.2
            elif 12 <= hour < 14:
                hour_factor = 1.0  # Lunch dip
            elif 14 <= hour < 17:
                hour_factor = 1.3
            elif 17 <= hour < 20:
                hour_factor = 1.6  # Evening rush
            elif 20 <= hour < 23:
                hour_factor = 0.9
            else:
                hour_factor = 0.4  # Overnight
            
            # Random noise
            noise = np.random.normal(1, 0.1)
            
            base_demand = 1000
            demand = base_demand * seasonal_factor * dow_factor * trend * hour_factor * noise
            
            # Overtime hours (correlated with demand spikes)
            overtime = max(0, (demand - 1200) / 50 + np.random.poisson(5))
            
            # Staff count needed
            staff_needed = int(demand / 25 + np.random.poisson(2))
            
            # Weather impact (random events)
            weather_severity = np.random.choice([0, 1, 2, 3], p=[0.7, 0.2, 0.08, 0.02])
            weather_impact = 1 + weather_severity * 0.15
            
            records.append({
                'datetime': date + timedelta(hours=hour),
                'date': date.date(),
                'hour': hour,
                'day_of_week': dow,
                'month': month,
                'is_weekend': dow >= 5,
                'is_holiday': False,  # Will flag separately
                'seasonal_factor': round(seasonal_factor, 3),
                'demand': int(demand),
                'overtime_hours': round(overtime, 1),
                'staff_needed': staff_needed,
                'weather_severity': weather_severity,
                'weather_impact': round(weather_impact, 2),
                'actual_staff': max(0, staff_needed + np.random.randint(-3, 4)),
                'service_calls': np.random.poisson(demand / 100),
                'equipment_usage_hours': round(demand / 200 + np.random.poisson(2), 1)
            })
    
    df = pd.DataFrame(records)
    
    # Flag holidays (simplified US holidays)
    holidays = [
        '2023-01-01', '2023-01-16', '2023-02-20', '2023-05-29', '2023-07-04',
        '2023-09-04', '2023-10-09', '2023-11-11', '2023-11-23', '2023-12-25',
        '2024-01-01', '2024-01-15', '2024-02-19', '2024-05-27', '2024-07-04',
        '2024-09-02', '2024-10-14', '2024-11-11', '2024-11-28', '2024-12-25'
    ]
    df['is_holiday'] = df['date'].astype(str).isin(holidays)
    
    # Reduce demand on holidays
    df.loc[df['is_holiday'], 'demand'] = (df.loc[df['is_holiday'], 'demand'] * 0.6).astype(int)
    
    return df


def generate_monthly_budget(n_months=24, random_state=42):
    """Generate synthetic monthly budget and expenditure data."""
    np.random.seed(random_state)
    
    categories = ['Labor', 'Equipment', 'Maintenance', 'Training', 'Supplies', 'Contractors']
    
    records = []
    base_date = datetime(2023, 1, 1)
    
    for month in range(n_months):
        date = base_date + timedelta(days=month * 30)
        
        for cat in categories:
            base_budget = {'Labor': 500000, 'Equipment': 150000, 'Maintenance': 100000,
                          'Training': 25000, 'Supplies': 40000, 'Contractors': 80000}[cat]
            
            # Budget with slight increases
            budget = base_budget * (1 + month * 0.005)
            
            # Expenditure with variance
            variance = np.random.normal(0, 0.08)
            spent = budget * (1 + variance)
            
            records.append({
                'month': date.strftime('%Y-%m'),
                'category': cat,
                'budget_allocated': round(budget, 2),
                'actual_spent': round(spent, 2),
                'variance_pct': round(variance * 100, 2),
                'variance_amount': round(spent - budget, 2)
            })
    
    return pd.DataFrame(records)


def generate_weekly_metrics(n_weeks=104, random_state=42):
    """Generate synthetic weekly workforce metrics."""
    np.random.seed(random_state)
    
    records = []
    base_date = datetime(2023, 1, 1)
    
    for week in range(n_weeks):
        date = base_date + timedelta(weeks=week)
        
        # Headcount with slow growth
        headcount = 450 + week * 0.5 + np.random.normal(0, 3)
        
        # Turnover rate (seasonal)
        turnover = 0.02 + 0.01 * np.sin(2 * np.pi * week / 52) + np.random.normal(0, 0.005)
        
        # Overtime ratio
        ot_ratio = 0.08 + 0.03 * np.sin(2 * np.pi * week / 52) + np.random.normal(0, 0.02)
        
        # Absenteeism
        absenteeism = 0.03 + np.random.normal(0, 0.01)
        
        # Productivity index
        productivity = 100 + week * 0.1 + np.random.normal(0, 2)
        
        records.append({
            'week_start': date.date(),
            'week_number': week + 1,
            'headcount': int(headcount),
            'new_hires': max(0, np.random.poisson(3)),
            'terminations': max(0, int(headcount * turnover)),
            'turnover_rate': round(turnover, 4),
            'overtime_hours': int(headcount * 40 * ot_ratio),
            'overtime_ratio': round(ot_ratio, 4),
            'absenteeism_rate': round(absenteeism, 4),
            'sick_days_total': int(headcount * absenteeism * 5),
            'productivity_index': round(productivity, 2),
            'training_hours': np.random.poisson(headcount * 0.5),
            'safety_incidents': np.random.poisson(2)
        })
    
    return pd.DataFrame(records)


def main():
    """Generate all datasets."""
    out_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(out_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    print("Generating hourly operational demand...")
    hourly = generate_hourly_demand(days=730)
    hourly.to_csv(os.path.join(data_dir, 'hourly_demand.csv'), index=False)
    print(f"  Saved {len(hourly)} hourly records")
    
    print("Generating monthly budget data...")
    monthly = generate_monthly_budget(n_months=24)
    monthly.to_csv(os.path.join(data_dir, 'monthly_budget.csv'), index=False)
    print(f"  Saved {len(monthly)} monthly records")
    
    print("Generating weekly workforce metrics...")
    weekly = generate_weekly_metrics(n_weeks=104)
    weekly.to_csv(os.path.join(data_dir, 'weekly_metrics.csv'), index=False)
    print(f"  Saved {len(weekly)} weekly records")
    
    print("\nAll datasets generated!")


if __name__ == '__main__':
    main()
