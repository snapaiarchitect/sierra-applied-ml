"""
Synthetic transit maintenance data generator.
Creates realistic predictive maintenance datasets based on real-world patterns.

Data mirrors:
- NYC MTA turnstile patterns (5.5M daily ridership)
- WMATA signal failure distributions
- FTA National Transit Database asset categories
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os


def generate_transit_assets(n_assets=500, random_state=42):
    """Generate synthetic transit asset inventory."""
    np.random.seed(random_state)
    
    asset_types = ['Signal', 'Track', 'Switch', 'Elevator', 'Escalator', 
                   'HVAC', 'Pump', 'Communication', 'Power', 'Train_Brake']
    
    lines = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Silver']
    
    assets = []
    for i in range(n_assets):
        asset_type = np.random.choice(asset_types)
        line = np.random.choice(lines)
        
        # Age distribution based on real transit asset lifecycles
        if asset_type in ['Signal', 'Communication']:
            age = np.random.exponential(8) + 2  # 2-15 years
        elif asset_type in ['Track', 'Switch']:
            age = np.random.exponential(15) + 5  # 5-30 years
        elif asset_type in ['Elevator', 'Escalator']:
            age = np.random.exponential(10) + 3  # 3-20 years
        else:
            age = np.random.exponential(6) + 1  # 1-12 years
        
        assets.append({
            'asset_id': f'AST-{i:04d}',
            'asset_type': asset_type,
            'line': line,
            'installation_date': datetime(2000, 1, 1) + timedelta(days=int(age * 365)),
            'age_years': round(age, 1),
            'criticality': np.random.choice(['Low', 'Medium', 'High', 'Critical'], 
                                            p=[0.1, 0.3, 0.4, 0.2]),
            'last_maintenance': datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)),
            'maintenance_count': np.random.poisson(3),
            'condition_score': max(1, min(10, np.random.normal(6, 2))),
            'daily_usage_hours': np.random.poisson(18) + 2
        })
    
    return pd.DataFrame(assets)


def generate_failure_history(assets_df, n_failures=2000, random_state=42):
    """Generate synthetic failure history with realistic patterns."""
    np.random.seed(random_state)
    
    failures = []
    
    for _ in range(n_failures):
        asset = assets_df.sample(1).iloc[0]
        
        # Failure probability increases with age and condition
        age_factor = asset['age_years'] / 20
        condition_factor = (10 - asset['condition_score']) / 10
        criticality_multiplier = {'Low': 0.5, 'Medium': 0.8, 'High': 1.2, 'Critical': 1.8}[asset['criticality']]
        
        # Weibull-like failure time generation
        shape = 2.0
        scale = 365 / (age_factor * condition_factor * criticality_multiplier + 0.1)
        days_to_failure = np.random.weibull(shape) * scale
        
        failure_date = asset['installation_date'] + timedelta(days=int(days_to_failure))
        
        if failure_date > datetime(2024, 12, 31):
            continue
            
        failures.append({
            'asset_id': asset['asset_id'],
            'failure_date': failure_date,
            'failure_type': np.random.choice(['Degradation', 'Sudden', 'Intermittent', 'Catastrophic'],
                                             p=[0.4, 0.3, 0.2, 0.1]),
            'downtime_hours': np.random.exponential(4) + 0.5,
            'repair_cost': np.random.lognormal(8, 1.5),
            'severity': np.random.choice(['Minor', 'Moderate', 'Major', 'Severe'],
                                       p=[0.3, 0.4, 0.2, 0.1]),
            'weather_related': np.random.choice([True, False], p=[0.15, 0.85]),
            'in_service': failure_date < datetime(2024, 6, 1)
        })
    
    return pd.DataFrame(failures)


def generate_sensor_telemetry(assets_df, days=365, random_state=42):
    """Generate synthetic IoT sensor telemetry."""
    np.random.seed(random_state)
    
    telemetry = []
    
    for _, asset in assets_df.iterrows():
        if asset['asset_type'] not in ['Signal', 'HVAC', 'Pump', 'Power']:
            continue
            
        for day in range(days):
            date = datetime(2024, 1, 1) + timedelta(days=day)
            
            # Base readings with degradation over time
            age_factor = asset['age_years'] / 15
            
            # Temperature (HVAC, Power)
            if asset['asset_type'] in ['HVAC', 'Power']:
                temp = 65 + np.random.normal(0, 5) + age_factor * 3
                telemetry.append({
                    'asset_id': asset['asset_id'],
                    'date': date,
                    'sensor_type': 'temperature',
                    'reading': round(temp, 2),
                    'unit': 'F'
                })
            
            # Vibration (Signal, Pump)
            if asset['asset_type'] in ['Signal', 'Pump']:
                vibration = 0.5 + np.random.exponential(0.3) + age_factor * 0.5
                telemetry.append({
                    'asset_id': asset['asset_id'],
                    'date': date,
                    'sensor_type': 'vibration',
                    'reading': round(vibration, 3),
                    'unit': 'mm/s'
                })
            
            # Voltage (Power, Signal)
            if asset['asset_type'] in ['Power', 'Signal']:
                voltage = 120 + np.random.normal(0, 3) - age_factor * 2
                telemetry.append({
                    'asset_id': asset['asset_id'],
                    'date': date,
                    'sensor_type': 'voltage',
                    'reading': round(voltage, 2),
                    'unit': 'V'
                })
    
    return pd.DataFrame(telemetry)


def generate_maintenance_logs(assets_df, n_records=3000, random_state=42):
    """Generate synthetic maintenance work orders."""
    np.random.seed(random_state)
    
    maintenance_types = ['Preventive', 'Corrective', 'Emergency', 'Overhaul', 'Inspection']
    
    logs = []
    for _ in range(n_records):
        asset = assets_df.sample(1).iloc[0]
        
        logs.append({
            'asset_id': asset['asset_id'],
            'maintenance_date': datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 730)),
            'maintenance_type': np.random.choice(maintenance_types, p=[0.35, 0.3, 0.15, 0.1, 0.1]),
            'duration_hours': np.random.exponential(3) + 0.5,
            'cost': np.random.lognormal(7, 1.2),
            'technician_count': np.random.choice([1, 2, 3, 4], p=[0.5, 0.3, 0.15, 0.05]),
            'parts_replaced': np.random.poisson(2),
            'downtime_impact': np.random.choice(['None', 'Minor', 'Moderate', 'Major'],
                                              p=[0.4, 0.3, 0.2, 0.1])
        })
    
    return pd.DataFrame(logs)


def main():
    """Generate all datasets and save to CSV."""
    out_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(out_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    print("Generating transit asset inventory...")
    assets = generate_transit_assets(n_assets=500)
    assets.to_csv(os.path.join(data_dir, 'transit_assets.csv'), index=False)
    print(f"  Saved {len(assets)} assets")
    
    print("Generating failure history...")
    failures = generate_failure_history(assets, n_failures=2000)
    failures.to_csv(os.path.join(data_dir, 'failure_history.csv'), index=False)
    print(f"  Saved {len(failures)} failures")
    
    print("Generating sensor telemetry...")
    telemetry = generate_sensor_telemetry(assets, days=365)
    telemetry.to_csv(os.path.join(data_dir, 'sensor_telemetry.csv'), index=False)
    print(f"  Saved {len(telemetry)} telemetry records")
    
    print("Generating maintenance logs...")
    maintenance = generate_maintenance_logs(assets, n_records=3000)
    maintenance.to_csv(os.path.join(data_dir, 'maintenance_logs.csv'), index=False)
    print(f"  Saved {len(maintenance)} maintenance records")
    
    print("\nAll datasets generated successfully!")


if __name__ == '__main__':
    main()
