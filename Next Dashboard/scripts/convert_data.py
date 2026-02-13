"""
Convert CSV analysis results to JSON for Next.js dashboard.
"""

import os
import json
import pandas as pd
import numpy as np

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DASHBOARD_DIR = os.path.dirname(SCRIPT_DIR)
THESIS_DIR = os.path.dirname(DASHBOARD_DIR)
RESULTS_DIR = os.path.join(THESIS_DIR, 'Coding', 'Cursor Analysis', 'Results')
OUTPUT_DIR = os.path.join(DASHBOARD_DIR, 'src', 'data')

# Station metadata
STATION_METADATA = {
    '0551621RF': {'name': 'Stor JPS Kuala Terengganu', 'district': 'Kuala Terengganu', 'lat': 5.3117, 'lng': 103.1324},
    '0580041RF': {'name': 'Klinik Bidan Kg. Baru Ajil', 'district': 'Hulu Terengganu', 'lat': 5.1500, 'lng': 103.0167},
    '0600011RF': {'name': 'JPS Bukit Besi', 'district': 'Dungun', 'lat': 4.8333, 'lng': 103.2667},
    '0600131RF': {'name': 'JPS Dungun', 'district': 'Dungun', 'lat': 4.7667, 'lng': 103.4167},
    '0600141RF': {'name': 'Rumah Pam Paya Ketam', 'district': 'Dungun', 'lat': 4.7833, 'lng': 103.3833},
    '0600151RF': {'name': 'JPS Kuala Dungun', 'district': 'Dungun', 'lat': 4.7833, 'lng': 103.4167},
    '0620081RF': {'name': 'Rumah Pam Nyatoh', 'district': 'Kemaman', 'lat': 4.4500, 'lng': 103.2333},
    '0630011RF': {'name': 'JPS Kemaman', 'district': 'Kemaman', 'lat': 4.2333, 'lng': 103.4167},
    '0630121RF': {'name': 'JPS Kg. Ibok, Kemaman', 'district': 'Kemaman', 'lat': 4.2667, 'lng': 103.3833},
    '0670051RF': {'name': 'Rumah Pam Tok Sabah, Marang', 'district': 'Marang', 'lat': 5.2000, 'lng': 103.2000},
    '0670181RF': {'name': 'Kg. Tepuh, Hulu Terengganu', 'district': 'Hulu Terengganu', 'lat': 5.0667, 'lng': 102.9833},
    '0670211RF': {'name': 'Rumah Pam Padang Landak', 'district': 'Kuala Terengganu', 'lat': 5.2333, 'lng': 103.0833},
    '0670221RF': {'name': 'JPS Kuala Berang', 'district': 'Hulu Terengganu', 'lat': 5.0500, 'lng': 103.0167},
    '0670251RF': {'name': 'Rumah Pam Jerangau', 'district': 'Marang', 'lat': 5.0333, 'lng': 103.1500},
    '0670281RF': {'name': 'Kg. Menerong, Hulu Terengganu', 'district': 'Hulu Terengganu', 'lat': 5.1000, 'lng': 102.9500},
    '0680071RF': {'name': 'Balai Polis Kg. Dura', 'district': 'Hulu Terengganu', 'lat': 4.9500, 'lng': 102.9167},
    '0680081RF': {'name': 'Rumah Pam Rantau Petronas', 'district': 'Hulu Terengganu', 'lat': 4.9833, 'lng': 102.9500},
    '0690051RF': {'name': 'Rumah Pam Pengkalan Ranggon', 'district': 'Setiu', 'lat': 5.4833, 'lng': 102.9333},
    '0700011RF': {'name': 'Rumah Pam Besut', 'district': 'Besut', 'lat': 5.7833, 'lng': 102.5500},
    '0700131RF': {'name': 'JPS Jertih, Besut', 'district': 'Besut', 'lat': 5.7333, 'lng': 102.5167},
}

def convert_all_data():
    """Convert all CSV files to JSON."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    data = {
        'stations': [],
        'annual': {
            'parameters': [],
            'gof': [],
            'returnPeriods': []
        },
        'daily': {
            'parameters': [],
            'gof': [],
            'returnPeriods': []
        },
        'overestimation': []
    }
    
    # Create stations list
    for station_id, meta in STATION_METADATA.items():
        data['stations'].append({
            'id': station_id,
            'name': meta['name'],
            'district': meta['district'],
            'lat': meta['lat'],
            'lng': meta['lng']
        })
    
    # Annual data
    annual_params = pd.read_csv(os.path.join(RESULTS_DIR, 'Annual', 'obj1_parameter_estimation.csv'))
    annual_gof = pd.read_csv(os.path.join(RESULTS_DIR, 'Annual', 'obj2_distribution_selection.csv'))
    annual_rp = pd.read_csv(os.path.join(RESULTS_DIR, 'Annual', 'obj3_return_period_analysis.csv'))
    
    # Process annual parameters - get unique stations with L-moments
    for station_id in annual_params['Station_ID'].unique():
        station_data = annual_params[annual_params['Station_ID'] == station_id].iloc[0]
        data['annual']['parameters'].append({
            'stationId': station_id,
            'stationName': station_data['Station_Name'],
            'nObservations': int(station_data['N_Observations']),
            'l1Mean': float(station_data['L1_Mean']),
            'l2Scale': float(station_data['L2_Scale']),
            't3LSkewness': float(station_data['T3_LSkewness']),
            't4LKurtosis': float(station_data['T4_LKurtosis'])
        })
    
    # Process annual GOF
    for _, row in annual_gof.iterrows():
        madi = row['MADI']
        msdi = row['MSDI']
        if madi == float('inf'):
            madi = None
        if msdi == float('inf'):
            msdi = None
        data['annual']['gof'].append({
            'stationId': row['Station_ID'],
            'stationName': row['Station_Name'],
            'distribution': row['Distribution'],
            'madi': madi,
            'msdi': msdi,
            'bestMadi': bool(row['Best_MADI']),
            'bestMsdi': bool(row['Best_MSDI'])
        })
    
    # Process annual return periods
    for _, row in annual_rp.iterrows():
        data['annual']['returnPeriods'].append({
            'stationId': row['Station_ID'],
            'stationName': row['Station_Name'],
            'bestDistribution': row['Best_Distribution'],
            'returnPeriod': int(row['Return_Period_Years']),
            'returnValue': float(row['Return_Value_mm'])
        })
    
    # Daily data
    daily_params = pd.read_csv(os.path.join(RESULTS_DIR, 'Daily', 'obj1_parameter_estimation.csv'))
    daily_gof = pd.read_csv(os.path.join(RESULTS_DIR, 'Daily', 'obj2_distribution_selection.csv'))
    daily_rp = pd.read_csv(os.path.join(RESULTS_DIR, 'Daily', 'obj3_return_period_analysis.csv'))
    
    # Process daily parameters
    for station_id in daily_params['Station_ID'].unique():
        station_data = daily_params[daily_params['Station_ID'] == station_id].iloc[0]
        data['daily']['parameters'].append({
            'stationId': station_id,
            'stationName': station_data['Station_Name'],
            'nObservations': int(station_data['N_Observations']),
            'l1Mean': float(station_data['L1_Mean']),
            'l2Scale': float(station_data['L2_Scale']),
            't3LSkewness': float(station_data['T3_LSkewness']),
            't4LKurtosis': float(station_data['T4_LKurtosis'])
        })
    
    # Process daily GOF
    for _, row in daily_gof.iterrows():
        madi = row['MADI']
        msdi = row['MSDI']
        if madi == float('inf'):
            madi = None
        if msdi == float('inf'):
            msdi = None
        data['daily']['gof'].append({
            'stationId': row['Station_ID'],
            'stationName': row['Station_Name'],
            'distribution': row['Distribution'],
            'madi': madi,
            'msdi': msdi,
            'bestMadi': bool(row['Best_MADI']),
            'bestMsdi': bool(row['Best_MSDI'])
        })
    
    # Process daily return periods
    for _, row in daily_rp.iterrows():
        data['daily']['returnPeriods'].append({
            'stationId': row['Station_ID'],
            'stationName': row['Station_Name'],
            'bestDistribution': row['Best_Distribution'],
            'returnPeriod': int(row['Return_Period_Years']),
            'returnValue': float(row['Return_Value_mm'])
        })
    
    # Overestimation data
    oe_df = pd.read_csv(os.path.join(RESULTS_DIR, 'Overestimation', 'obj4_overestimation_analysis.csv'))
    for _, row in oe_df.iterrows():
        oe_factor = row['OE_Factor']
        oe_pct = row['OE_Percentage']
        rp_annual = row['RP_Annual_Years']
        rp_daily_days = row['RP_Daily_Days']
        rp_daily_years = row['RP_Daily_Years']
        
        # Handle infinity values (not valid JSON)
        if oe_factor == float('inf') or np.isinf(oe_factor):
            oe_factor = None
            oe_pct = None
        if np.isinf(rp_annual):
            rp_annual = None
        if np.isinf(rp_daily_days):
            rp_daily_days = None
        if np.isinf(rp_daily_years):
            rp_daily_years = None
            
        data['overestimation'].append({
            'stationId': row['Station_ID'],
            'stationName': row['Station_Name'],
            'magnitude': float(row['Magnitude_mm']),
            'percentile': int(row['Percentile']),
            'bestAnnualDist': row['Best_Annual_Dist'],
            'bestDailyDist': row['Best_Daily_Dist'],
            'rpAnnualYears': float(rp_annual) if rp_annual is not None else None,
            'rpDailyDays': float(rp_daily_days) if rp_daily_days is not None else None,
            'rpDailyYears': float(rp_daily_years) if rp_daily_years is not None else None,
            'oeFactor': float(oe_factor) if oe_factor is not None else None,
            'oePercentage': float(oe_pct) if oe_pct is not None else None
        })
    
    # Write JSON file
    output_path = os.path.join(OUTPUT_DIR, 'analysis-results.json')
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Data converted successfully to: {output_path}")
    print(f"  - {len(data['stations'])} stations")
    print(f"  - {len(data['annual']['parameters'])} annual parameter records")
    print(f"  - {len(data['annual']['gof'])} annual GOF records")
    print(f"  - {len(data['annual']['returnPeriods'])} annual return period records")
    print(f"  - {len(data['daily']['parameters'])} daily parameter records")
    print(f"  - {len(data['overestimation'])} overestimation records")


if __name__ == '__main__':
    convert_all_data()

