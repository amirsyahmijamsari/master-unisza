"""
L-MOMENTS FLOOD FREQUENCY ANALYSIS
===================================
Complete Analysis for Terengganu Rainfall Data

Research Objectives:
1. Estimate distribution parameters using L-moments
2. Identify best-fitting distribution using MADI/MSDI
3. Conduct return period analysis
4. Quantify overestimation when using AM approach vs Daily data

Author: Research Thesis
Date: January 2026
"""

import os
import pandas as pd
import numpy as np
import lmoments3 as lm
from lmoments3 import distr
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION
# ============================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(BASE_DIR, 'Data')
ANNUAL_DIR = os.path.join(DATA_DIR, 'Annual')
DAILY_DIR = os.path.join(DATA_DIR, 'Daily')
RESULTS_DIR = os.path.join(SCRIPT_DIR, 'Results')
PLOTS_DIR = os.path.join(SCRIPT_DIR, 'Plots')
FIGURES_DIR = os.path.join(SCRIPT_DIR, 'Figures')

# Create output directories
for d in [RESULTS_DIR, PLOTS_DIR, FIGURES_DIR,
          os.path.join(RESULTS_DIR, 'Annual'),
          os.path.join(RESULTS_DIR, 'Daily'),
          os.path.join(RESULTS_DIR, 'Overestimation'),
          os.path.join(PLOTS_DIR, 'Annual'),
          os.path.join(PLOTS_DIR, 'Daily')]:
    os.makedirs(d, exist_ok=True)

# Distributions to fit
DISTRIBUTIONS = ['gum', 'nor', 'exp', 'gev', 'glo', 'gno', 'gpa', 'pe3', 'kap']

# Station names
STATION_NAMES = {
    '0551621RF': 'Stor JPS Kuala Terengganu',
    '0580041RF': 'Klinik Bidan Kg. Baru Ajil',
    '0600011RF': 'JPS Bukit Besi',
    '0600131RF': 'JPS Dungun',
    '0600141RF': 'Rumah Pam Paya Ketam',
    '0600151RF': 'JPS Kuala Dungun',
    '0620081RF': 'Rumah Pam Nyatoh',
    '0630011RF': 'JPS Kemaman',
    '0630121RF': 'JPS Kg. Ibok, Kemaman',
    '0670051RF': 'Rumah Pam Tok Sabah, Marang',
    '0670181RF': 'Kg. Tepuh, Hulu Terengganu',
    '0670211RF': 'Rumah Pam Padang Landak',
    '0670221RF': 'JPS Kuala Berang',
    '0670251RF': 'Rumah Pam Jerangau',
    '0670281RF': 'Kg. Menerong, Hulu Terengganu',
    '0680071RF': 'Balai Polis Kg. Dura',
    '0680081RF': 'Rumah Pam Rantau Petronas',
    '0690051RF': 'Rumah Pam Pengkalan Ranggon',
    '0700011RF': 'Rumah Pam Besut',
    '0700131RF': 'JPS Jertih, Besut'
}

# Return periods for analysis
RETURN_PERIODS = [2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def filter_rainfall_data(data, data_type, threshold=1.0):
    """Filter data based on type. Daily data filtered to >= threshold."""
    if data_type == 'Daily':
        if hasattr(data, 'values'):
            data = data.values
        return data[data >= threshold]
    return data


def gringorten_plotting_positions(n):
    """Calculate Gringorten plotting positions: P_i = (i - 0.44) / (n + 0.12)"""
    return np.array([(i - 0.44) / (n + 0.12) for i in range(1, n + 1)])


def calculate_lmoments(data):
    """Calculate L-moments for data."""
    if hasattr(data, 'dropna'):
        clean_data = data.dropna()
    else:
        clean_data = data[~np.isnan(data)]
    l_moms = lm.lmom_ratios(clean_data, nmom=4)
    return {
        'L1': l_moms[0],
        'L2': l_moms[1],
        'T3': l_moms[2],
        'T4': l_moms[3]
    }


def fit_distributions(data):
    """Fit all distributions to data and return parameters."""
    if hasattr(data, 'dropna'):
        clean_data = data.dropna()
    elif isinstance(data, np.ndarray):
        clean_data = data[~np.isnan(data)]
    else:
        clean_data = data
    
    params = {}
    for dist_name in DISTRIBUTIONS:
        try:
            dist = getattr(distr, dist_name)
            fitted = dist.lmom_fit(clean_data)
            params[dist_name] = dict(fitted)
        except (ValueError, RuntimeError):
            params[dist_name] = None
    return params


def calculate_quantiles(data, params):
    """Calculate quantiles for all fitted distributions."""
    if hasattr(data, 'dropna'):
        clean_data = data.dropna()
    elif isinstance(data, np.ndarray):
        clean_data = data[~np.isnan(data)]
    else:
        clean_data = data
    
    n = len(clean_data)
    P_i = gringorten_plotting_positions(n)
    
    quantiles = {}
    for dist_name, dist_params in params.items():
        if dist_params is not None:
            try:
                dist = getattr(distr, dist_name)
                quantiles[dist_name] = dist.ppf(P_i, **dist_params)
            except Exception:
                quantiles[dist_name] = None
        else:
            quantiles[dist_name] = None
    return quantiles, P_i


def calculate_madi_msdi(sorted_data, quantiles):
    """Calculate MADI and MSDI for each distribution."""
    madi = {}
    msdi = {}
    
    for dist_name, q in quantiles.items():
        if q is not None and len(q) == len(sorted_data):
            # Normalized differences
            with np.errstate(divide='ignore', invalid='ignore'):
                norm_diff = (sorted_data - q) / sorted_data
                norm_diff = np.where(np.isfinite(norm_diff), norm_diff, 0)
            
            madi[dist_name] = np.mean(np.abs(norm_diff))
            msdi[dist_name] = np.mean(norm_diff ** 2)
        else:
            madi[dist_name] = None
            msdi[dist_name] = None
    
    return madi, msdi


def identify_best_distribution(madi, msdi):
    """Identify best distribution based on lowest MADI."""
    valid_madi = {k: v for k, v in madi.items() if v is not None}
    if valid_madi:
        best = min(valid_madi, key=valid_madi.get)
        return best, valid_madi[best]
    return None, None


def calculate_return_values(params, dist_name, return_periods):
    """Calculate return values for given return periods."""
    if params.get(dist_name) is None:
        return None
    
    try:
        dist = getattr(distr, dist_name)
        exceedance_probs = [1 - 1/T for T in return_periods]
        return_values = [dist.ppf(p, **params[dist_name]) for p in exceedance_probs]
        return return_values
    except Exception:
        return None


def calculate_return_period_for_value(params, dist_name, value):
    """Calculate return period for a specific value."""
    if params.get(dist_name) is None:
        return None
    
    try:
        dist = getattr(distr, dist_name)
        prob = dist.cdf(value, **params[dist_name])
        if prob >= 1:
            return np.inf
        return 1 / (1 - prob)
    except Exception:
        return None


# ============================================================================
# OBJECTIVE 1: PARAMETER ESTIMATION
# ============================================================================

def objective1_parameter_estimation(data_dir, data_type):
    """Objective 1: Estimate distribution parameters using L-moments."""
    print(f"\n{'='*70}")
    print(f"OBJECTIVE 1: Parameter Estimation ({data_type} Data)")
    print(f"{'='*70}")
    
    results = []
    
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    for csv_file in sorted(csv_files):
        station_id = csv_file.replace('.csv', '')
        station_name = STATION_NAMES.get(station_id, station_id)
        
        file_path = os.path.join(data_dir, csv_file)
        df = pd.read_csv(file_path)
        data = df['Value (mm)'].dropna()
        
        if data_type == 'Daily':
            data = filter_rainfall_data(data, data_type)
        
        l_moms = calculate_lmoments(data)
        
        print(f"\nProcessing: {station_id} - {station_name}")
        print(f"  L-moments: L1={l_moms['L1']:.4f}, L2={l_moms['L2']:.4f}, "
              f"T3={l_moms['T3']:.4f}, T4={l_moms['T4']:.4f}")
        
        results.append({
            'Station_ID': station_id,
            'Station_Name': station_name,
            'N': len(data),
            'L1_Mean': l_moms['L1'],
            'L2_Scale': l_moms['L2'],
            'T3_LSkewness': l_moms['T3'],
            'T4_LKurtosis': l_moms['T4']
        })
    
    return pd.DataFrame(results)


# ============================================================================
# OBJECTIVE 2: DISTRIBUTION SELECTION
# ============================================================================

def objective2_distribution_selection(data_dir, data_type):
    """Objective 2: Identify best-fitting distribution using MADI/MSDI."""
    print(f"\n{'='*70}")
    print(f"OBJECTIVE 2: Distribution Selection ({data_type} Data)")
    print(f"{'='*70}")
    
    results = []
    
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    for csv_file in sorted(csv_files):
        station_id = csv_file.replace('.csv', '')
        station_name = STATION_NAMES.get(station_id, station_id)
        
        file_path = os.path.join(data_dir, csv_file)
        df = pd.read_csv(file_path)
        data = df['Value (mm)'].dropna()
        
        if data_type == 'Daily':
            data = filter_rainfall_data(data, data_type)
        
        params = fit_distributions(data)
        sorted_data = np.sort(data)
        quantiles, _ = calculate_quantiles(data, params)
        madi, msdi = calculate_madi_msdi(sorted_data, quantiles)
        best_dist, best_madi = identify_best_distribution(madi, msdi)
        
        print(f"\nProcessing: {station_id} - {station_name}")
        print(f"  Best distribution (MADI): {best_dist.upper() if best_dist else 'N/A'}")
        print(f"  MADI = {best_madi:.4f}, MSDI = {msdi.get(best_dist, 0):.4f}")
        
        row = {
            'Station_ID': station_id,
            'Station_Name': station_name,
            'Best_Distribution': best_dist.upper() if best_dist else None,
            'Best_MADI': best_madi,
            'Best_MSDI': msdi.get(best_dist)
        }
        
        # Add MADI for all distributions
        for dist_name in DISTRIBUTIONS:
            row[f'MADI_{dist_name.upper()}'] = madi.get(dist_name)
            row[f'MSDI_{dist_name.upper()}'] = msdi.get(dist_name)
        
        results.append(row)
    
    return pd.DataFrame(results)


# ============================================================================
# OBJECTIVE 3: RETURN PERIOD ANALYSIS
# ============================================================================

def objective3_return_period_analysis(data_dir, data_type):
    """Objective 3: Conduct return period analysis using best distribution."""
    print(f"\n{'='*70}")
    print(f"OBJECTIVE 3: Return Period Analysis ({data_type} Data)")
    print(f"{'='*70}")
    
    results = []
    
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    for csv_file in sorted(csv_files):
        station_id = csv_file.replace('.csv', '')
        station_name = STATION_NAMES.get(station_id, station_id)
        
        file_path = os.path.join(data_dir, csv_file)
        df = pd.read_csv(file_path)
        data = df['Value (mm)'].dropna()
        
        if data_type == 'Daily':
            data = filter_rainfall_data(data, data_type)
        
        params = fit_distributions(data)
        sorted_data = np.sort(data)
        quantiles, _ = calculate_quantiles(data, params)
        madi, msdi = calculate_madi_msdi(sorted_data, quantiles)
        best_dist, _ = identify_best_distribution(madi, msdi)
        
        if best_dist is None:
            continue
        
        return_values = calculate_return_values(params, best_dist, RETURN_PERIODS)
        
        print(f"\nProcessing: {station_id} - {station_name}")
        print(f"  Using distribution: {best_dist.upper()}")
        print(f"  Return values calculated for {len(RETURN_PERIODS)} return periods")
        
        if return_values:
            for T, rv in zip(RETURN_PERIODS, return_values):
                results.append({
                    'Station_ID': station_id,
                    'Station_Name': station_name,
                    'Best_Distribution': best_dist.upper(),
                    'Return_Period_Years': T,
                    'Return_Value_mm': rv
                })
    
    return pd.DataFrame(results)


# ============================================================================
# OBJECTIVE 4: OVERESTIMATION QUANTIFICATION
# ============================================================================

def objective4_overestimation_analysis(annual_dir, daily_dir):
    """
    Objective 4: Quantify overestimation when using AM approach vs daily data.
    
    The overestimation factor is calculated as:
    OE(M) = RP_AM(M) / (RP_daily(M) / 365.25)
    
    Where:
    - RP_AM(M) is the return period in years from Annual Maxima analysis
    - RP_daily(M) is the return period in days from daily data analysis
    """
    print(f"\n{'='*70}")
    print("OBJECTIVE 4: Overestimation Quantification (AM vs Daily)")
    print(f"{'='*70}")
    
    results = []
    
    annual_files = set(f for f in os.listdir(annual_dir) if f.endswith('.csv'))
    daily_files = set(f for f in os.listdir(daily_dir) if f.endswith('.csv'))
    common_files = annual_files.intersection(daily_files)
    
    for csv_file in sorted(common_files):
        station_id = csv_file.replace('.csv', '')
        station_name = STATION_NAMES.get(station_id, station_id)
        
        print(f"\nProcessing: {station_id} - {station_name}")
        
        # Read Annual data
        annual_path = os.path.join(annual_dir, csv_file)
        annual_df = pd.read_csv(annual_path)
        annual_data = annual_df['Value (mm)'].dropna()
        
        # Read Daily data
        daily_path = os.path.join(daily_dir, csv_file)
        daily_df = pd.read_csv(daily_path)
        daily_raw = daily_df['Value (mm)'].dropna()  # All daily data including zeros
        daily_data = filter_rainfall_data(daily_raw, 'Daily')  # Filtered >= 1mm for distribution fitting
        
        # Fit distributions
        annual_params = fit_distributions(annual_data)
        daily_params = fit_distributions(daily_data)  # Fit to filtered data (>=1mm)
        
        # Calculate MADI/MSDI
        sorted_annual = np.sort(annual_data)
        sorted_daily = np.sort(daily_data)
        
        annual_quantiles, _ = calculate_quantiles(annual_data, annual_params)
        daily_quantiles, _ = calculate_quantiles(daily_data, daily_params)
        
        annual_madi, annual_msdi = calculate_madi_msdi(sorted_annual, annual_quantiles)
        daily_madi, daily_msdi = calculate_madi_msdi(sorted_daily, daily_quantiles)
        
        # Get best distributions
        best_annual, _ = identify_best_distribution(annual_madi, annual_msdi)
        best_daily, _ = identify_best_distribution(daily_madi, daily_msdi)
        
        print(f"  Best Annual distribution: {best_annual.upper() if best_annual else 'N/A'}")
        print(f"  Best Daily distribution: {best_daily.upper() if best_daily else 'N/A'}")
        
        if best_annual is None or best_daily is None:
            continue
        
        # Test at various percentiles of ALL daily data (including zeros)
        # This provides true frequency representation in the complete time series
        # Following Complete Time-series Analysis (CTA) approach (Volpi et al., 2019)
        # Percentiles from complete data ensure accurate frequency representation,
        # while distribution fitting uses filtered data (>=1mm) to avoid zero-inflation
        test_values = np.percentile(daily_raw, [50, 75, 90, 95, 99])
        
        for percentile, M in zip([50, 75, 90, 95, 99], test_values):
            # Return period from Annual Maxima (in years)
            rp_annual = calculate_return_period_for_value(annual_params, best_annual, M)
            
            # Return period from Daily data (in days)
            rp_daily = calculate_return_period_for_value(daily_params, best_daily, M)
            
            if rp_annual is None or rp_daily is None:
                continue
            if rp_daily <= 0 or rp_annual <= 0:
                continue
            
            # Convert daily return period to years
            rp_daily_years = rp_daily / 365.25
            
            # Overestimation factor
            if rp_daily_years > 0:
                oe_factor = rp_annual / rp_daily_years
                oe_percentage = (oe_factor - 1) * 100
            else:
                oe_factor = np.inf
                oe_percentage = np.inf
            
            results.append({
                'Station_ID': station_id,
                'Station_Name': station_name,
                'Magnitude_mm': M,
                'Percentile': percentile,
                'Best_Annual_Dist': best_annual.upper(),
                'Best_Daily_Dist': best_daily.upper(),
                'RP_Annual_Years': rp_annual,
                'RP_Daily_Days': rp_daily,
                'RP_Daily_Years': rp_daily_years,
                'OE_Factor': oe_factor,
                'OE_Percentage': oe_percentage
            })
        
        # Print summary
        station_results = [r for r in results if r['Station_ID'] == station_id]
        if station_results:
            avg_oe = np.mean([r['OE_Factor'] for r in station_results if r['OE_Factor'] != np.inf])
            print(f"  Average Overestimation Factor: {avg_oe:.2f}x")
    
    return pd.DataFrame(results)


# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def create_figures(annual_results_dir, daily_results_dir, oe_df, figures_dir):
    """Create all figures for Chapter 5."""
    print(f"\n{'='*70}")
    print("Creating Figures for Chapter 5")
    print(f"{'='*70}")
    
    # Load results
    annual_obj1 = pd.read_csv(os.path.join(annual_results_dir, 'obj1_parameter_estimation.csv'))
    daily_obj1 = pd.read_csv(os.path.join(daily_results_dir, 'obj1_parameter_estimation.csv'))
    annual_obj2 = pd.read_csv(os.path.join(annual_results_dir, 'obj2_distribution_selection.csv'))
    daily_obj2 = pd.read_csv(os.path.join(daily_results_dir, 'obj2_distribution_selection.csv'))
    annual_obj3 = pd.read_csv(os.path.join(annual_results_dir, 'obj3_return_period_analysis.csv'))
    
    # Figure 5.1: L-Moment Ratio Diagram with Theoretical Distribution Curves
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Define theoretical distribution curves
    # Generate L-moment ratios for theoretical distributions by varying shape parameters
    distributions_curves = {
        'Gumbel (GUM)': {'color': 'gray', 'linestyle': '--', 'linewidth': 1.5},
        'Normal (NOR)': {'color': 'purple', 'linestyle': '--', 'linewidth': 1.5},
        'Exponential (EXP)': {'color': 'orange', 'linestyle': '--', 'linewidth': 1.5},
        'GEV': {'color': 'green', 'linestyle': '-', 'linewidth': 2},
        'GLO': {'color': 'cyan', 'linestyle': '-', 'linewidth': 2},
        'GNO': {'color': 'magenta', 'linestyle': '-', 'linewidth': 2},
        'GPA': {'color': 'brown', 'linestyle': '-', 'linewidth': 2},
        'PE3': {'color': 'olive', 'linestyle': '-', 'linewidth': 2},
        'Kappa (KAP)': {'color': 'pink', 'linestyle': '-', 'linewidth': 2}
    }
    
    # Generate theoretical curves for distributions
    # Gumbel: fixed point (0, 0.1506)
    ax.plot([0], [0.1506], 'o', color='gray', markersize=8, label='Gumbel (GUM)')
    
    # Normal: fixed point (0, 0.1226)
    ax.plot([0], [0.1226], 's', color='purple', markersize=8, label='Normal (NOR)')
    
    # Exponential: fixed point (0.3333, 0.1667)
    ax.plot([0.3333], [0.1667], '^', color='orange', markersize=8, label='Exponential (EXP)')
    
    # GEV: curve for k from -0.5 to 0.5
    k_gev = np.linspace(-0.5, 0.5, 100)
    t3_gev = []
    t4_gev = []
    for k in k_gev:
        try:
            # Calculate theoretical L-moments for GEV
            # Using approximate relationships from Hosking (1990)
            if abs(k) < 1e-6:  # Gumbel limit
                t3_gev.append(0.1699)
                t4_gev.append(0.1504)
            else:
                # Theoretical L-moment ratios for GEV
                # These are approximations; exact values require numerical integration
                t3_val = 2 * (1 - 3**(-k)) / (1 - 2**(-k)) - 3
                t4_val = (1 - 5*4**(-k) + 10*3**(-k) - 6*2**(-k)) / (1 - 2**(-k))
                if -1 < t3_val < 1 and 0 < t4_val < 1:
                    t3_gev.append(t3_val)
                    t4_gev.append(t4_val)
        except:
            continue
    if t3_gev:
        ax.plot(t3_gev, t4_gev, color='green', linestyle='-', linewidth=2, label='GEV', alpha=0.7)
    
    # GLO: curve for k from -0.5 to 0.5
    k_glo = np.linspace(-0.5, 0.5, 100)
    t3_glo = []
    t4_glo = []
    for k in k_glo:
        try:
            if abs(k) < 1e-6:
                t3_glo.append(0)
                t4_glo.append(0.1667)
            else:
                # Theoretical L-moment ratios for GLO
                t3_val = -k
                t4_val = (1 + 5*k**2) / 6
                if -1 < t3_val < 1 and 0 < t4_val < 1:
                    t3_glo.append(t3_val)
                    t4_glo.append(t4_val)
        except:
            continue
    if t3_glo:
        ax.plot(t3_glo, t4_glo, color='cyan', linestyle='-', linewidth=2, label='GLO', alpha=0.7)
    
    # GNO: curve for k from -0.5 to 0.5
    k_gno = np.linspace(-0.5, 0.5, 100)
    t3_gno = []
    t4_gno = []
    for k in k_gno:
        try:
            if abs(k) < 1e-6:
                t3_gno.append(0)
                t4_gno.append(0.1226)
            else:
                # Theoretical L-moment ratios for GNO (Lognormal)
                # Approximate relationships
                t3_val = 6 * np.arctan(k) / np.pi
                t4_val = 0.1226 + 0.5 * k**2
                if -1 < t3_val < 1 and 0 < t4_val < 1:
                    t3_gno.append(t3_val)
                    t4_gno.append(t4_val)
        except:
            continue
    if t3_gno:
        ax.plot(t3_gno, t4_gno, color='magenta', linestyle='-', linewidth=2, label='GNO', alpha=0.7)
    
    # GPA: curve for c from -0.5 to 0.5
    c_gpa = np.linspace(-0.5, 0.5, 100)
    t3_gpa = []
    t4_gpa = []
    for c in c_gpa:
        try:
            if abs(c) < 1e-6:
                t3_gpa.append(0.3333)
                t4_gpa.append(0.1667)
            else:
                # Theoretical L-moment ratios for GPA
                t3_val = (1 + c) / 3
                t4_val = (1 + 3*c + 2*c**2) / 6
                if -1 < t3_val < 1 and 0 < t4_val < 1:
                    t3_gpa.append(t3_val)
                    t4_gpa.append(t4_val)
        except:
            continue
    if t3_gpa:
        ax.plot(t3_gpa, t4_gpa, color='brown', linestyle='-', linewidth=2, label='GPA', alpha=0.7)
    
    # PE3: curve for skew from -2 to 2
    skew_pe3 = np.linspace(-2, 2, 100)
    t3_pe3 = []
    t4_pe3 = []
    for skew in skew_pe3:
        try:
            # Theoretical L-moment ratios for PE3
            # Approximate relationships
            t3_val = skew / 3
            t4_val = 0.1226 + 0.1 * skew**2
            if -1 < t3_val < 1 and 0 < t4_val < 1:
                t3_pe3.append(t3_val)
                t4_pe3.append(t4_val)
        except:
            continue
    if t3_pe3:
        ax.plot(t3_pe3, t4_pe3, color='olive', linestyle='-', linewidth=2, label='PE3', alpha=0.7)
    
    # Kappa: 2D region (more complex, show as shaded region or sample points)
    # For simplicity, show a representative curve for h=1 and varying k
    k_kap = np.linspace(-0.5, 0.5, 100)
    t3_kap = []
    t4_kap = []
    h_kap = 1.0  # Fixed h for demonstration
    for k in k_kap:
        try:
            # Theoretical L-moment ratios for Kappa (simplified)
            t3_val = k
            t4_val = (1 + 3*k**2) / 6
            if -1 < t3_val < 1 and 0 < t4_val < 1:
                t3_kap.append(t3_val)
                t4_kap.append(t4_val)
        except:
            continue
    if t3_kap:
        ax.plot(t3_kap, t4_kap, color='pink', linestyle='-', linewidth=2, label='4-Parameter Kappa (K4D, h=1)', alpha=0.7)
    
    # Plot empirical data points
    ax.scatter(annual_obj1['T3_LSkewness'], annual_obj1['T4_LKurtosis'], 
               s=100, c='blue', marker='o', label='Annual Maximum Series', alpha=0.7, zorder=5)
    ax.scatter(daily_obj1['T3_LSkewness'], daily_obj1['T4_LKurtosis'], 
               s=100, c='red', marker='s', label='Daily Rainfall Series', alpha=0.7, zorder=5)
    
    ax.set_xlabel('L-Skewness (τ₃)', fontsize=12)
    ax.set_ylabel('L-Kurtosis (τ₄)', fontsize=12)
    ax.set_title('L-Moment Ratio Diagram with Theoretical Distribution Curves', fontsize=14)
    ax.legend(loc='upper left', fontsize=9, ncol=2)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, 'Figure_5_1_LMoments_Ratio_Diagram.png'), dpi=150)
    plt.close()
    print("  Created Figure 5.1: L-Moment Ratio Diagram with Theoretical Distribution Curves")
    
    # Figure 5.2: L-Moments Comparison
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    metrics = [('L1_Mean', 'L₁ (Mean)'), ('L2_Scale', 'L₂ (Scale)'), 
               ('T3_LSkewness', 'τ₃ (L-Skewness)'), ('T4_LKurtosis', 'τ₄ (L-Kurtosis)')]
    
    for ax, (col, label) in zip(axes.flat, metrics):
        x = range(len(annual_obj1))
        width = 0.35
        ax.bar([i - width/2 for i in x], annual_obj1[col], width, label='Annual', color='blue', alpha=0.7)
        ax.bar([i + width/2 for i in x], daily_obj1[col], width, label='Daily', color='red', alpha=0.7)
        ax.set_ylabel(label)
        ax.set_xticks(x)
        ax.set_xticklabels(annual_obj1['Station_ID'], rotation=45, ha='right', fontsize=8)
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('L-Moments Comparison: Annual vs Daily Data', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, 'Figure_5_2_LMoments_Comparison.png'), dpi=150)
    plt.close()
    print("  Created Figure 5.2: L-Moments Comparison")
    
    # Figure 5.3: Best Distribution Summary
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    for ax, (df, title) in zip(axes, [(annual_obj2, 'Annual'), (daily_obj2, 'Daily')]):
        counts = df['Best_Distribution'].value_counts()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
        ax.set_title(f'{title} Data')
    
    plt.suptitle('Best-Fitting Distribution Summary', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, 'Figure_5_3_Best_Distribution_Summary.png'), dpi=150)
    plt.close()
    print("  Created Figure 5.3: Best Distribution Summary")
    
    # Figure 5.4: MADI Comparison
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    for ax, (df, title) in zip(axes, [(annual_obj2, 'Annual'), (daily_obj2, 'Daily')]):
        madi_cols = [c for c in df.columns if c.startswith('MADI_')]
        madi_data = df[madi_cols].mean()
        madi_data.index = [c.replace('MADI_', '') for c in madi_data.index]
        madi_data.plot(kind='bar', ax=ax, color='steelblue', alpha=0.7)
        ax.set_xlabel('Distribution')
        ax.set_ylabel('Mean MADI')
        ax.set_title(f'{title} Data')
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('Mean MADI by Distribution', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, 'Figure_5_4_MADI_Comparison.png'), dpi=150)
    plt.close()
    print("  Created Figure 5.4: MADI Comparison")
    
    # Figure 5.5: Return Period Curves Comparison (AM vs Daily)
    # Load daily return period data
    daily_obj3 = pd.read_csv(os.path.join(daily_results_dir, 'obj3_return_period_analysis.csv'))
    
    # Select representative stations based on AM 100-year return values
    rp100_data = annual_obj3[annual_obj3['Return_Period_Years'] == 100].sort_values('Return_Value_mm')
    
    # Select 3 representative stations: lowest, median, and highest
    n_stations = len(rp100_data)
    selected_indices = [
        0,  # Lowest
        n_stations // 2,  # Median
        n_stations - 1  # Highest
    ]
    selected_stations = rp100_data.iloc[selected_indices]['Station_ID'].tolist()
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    for idx, station_id in enumerate(selected_stations):
        ax = axes[idx]
        
        # Annual Maximum data
        am_data = annual_obj3[annual_obj3['Station_ID'] == station_id]
        station_name = am_data['Station_Name'].iloc[0]
        
        # Daily data
        daily_data = daily_obj3[daily_obj3['Station_ID'] == station_id]
        
        # Plot both curves
        ax.plot(am_data['Return_Period_Years'], am_data['Return_Value_mm'], 
                'o-', label='Annual Maximum', linewidth=2, markersize=6, color='blue', alpha=0.8)
        ax.plot(daily_data['Return_Period_Years'], daily_data['Return_Value_mm'], 
                's-', label='Daily Rainfall', linewidth=2, markersize=6, color='red', alpha=0.8)
        
        ax.set_xlabel('Return Period (Years)', fontsize=11)
        ax.set_ylabel('Return Value (mm)', fontsize=11)
        ax.set_title(f'{station_id}\n{station_name[:35]}', fontsize=10)
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_xscale('log')
    
    plt.suptitle('Comparison of Return Period Curves: Annual Maximum vs Daily Rainfall', 
                 fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, 'Figure_5_5_Return_Period_Curves.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("  Created Figure 5.5: Return Period Curves Comparison (AM vs Daily)")
    
    # Figure 5.6: Return Values Heatmap
    pivot = annual_obj3.pivot(index='Station_ID', columns='Return_Period_Years', values='Return_Value_mm')
    fig, ax = plt.subplots(figsize=(14, 10))
    im = ax.imshow(pivot.values, cmap='YlOrRd', aspect='auto')
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns)
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    ax.set_xlabel('Return Period (Years)')
    ax.set_ylabel('Station ID')
    ax.set_title('Return Values (mm) Heatmap')
    plt.colorbar(im, ax=ax, label='Return Value (mm)')
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, 'Figure_5_6_Return_Values_Heatmap.png'), dpi=150)
    plt.close()
    print("  Created Figure 5.6: Return Values Heatmap")
    
    # Figure 5.7: Overestimation by Station (99th Percentile)
    oe_99 = oe_df[oe_df['Percentile'] == 99].copy()
    oe_99 = oe_99.sort_values('OE_Factor', ascending=True)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['green' if x < 1 else 'orange' if x < 3 else 'red' for x in oe_99['OE_Factor']]
    bars = ax.barh(range(len(oe_99)), oe_99['OE_Factor'], color=colors)
    ax.set_yticks(range(len(oe_99)))
    ax.set_yticklabels(oe_99['Station_ID'], fontsize=9)
    ax.axvline(x=1, color='green', linestyle='--', linewidth=2, label='No Overestimation')
    ax.axvline(x=oe_99['OE_Factor'].mean(), color='red', linestyle='-', linewidth=2, 
               label=f'Mean: {oe_99["OE_Factor"].mean():.2f}x')
    ax.set_xlabel('Overestimation Factor', fontsize=12)
    ax.set_title('Overestimation Factor by Station (99th Percentile)', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, 'Figure_5_7_Overestimation_by_Station.png'), dpi=150)
    plt.close()
    print("  Created Figure 5.7: Overestimation by Station (99th Percentile)")
    
    # Figure 5.8: Overestimation Summary (99th Percentile)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left: Histogram
    axes[0].hist(oe_99['OE_Factor'], bins=10, color='steelblue', edgecolor='black', alpha=0.7)
    axes[0].axvline(oe_99['OE_Factor'].mean(), color='red', linestyle='-', linewidth=2, 
                    label=f'Mean: {oe_99["OE_Factor"].mean():.2f}x')
    axes[0].axvline(oe_99['OE_Factor'].median(), color='orange', linestyle='--', linewidth=2,
                    label=f'Median: {oe_99["OE_Factor"].median():.2f}x')
    axes[0].set_xlabel('Overestimation Factor')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Distribution of OE Factor (99th Percentile)')
    axes[0].legend()
    
    # Right: Scatter plot
    axes[1].scatter(oe_99['RP_Daily_Years'], oe_99['RP_Annual_Years'], 
                    s=100, c='blue', alpha=0.7)
    max_val = max(oe_99['RP_Annual_Years'].max(), oe_99['RP_Daily_Years'].max())
    axes[1].plot([0, max_val], [0, max_val], 'k--', label='1:1 Line')
    axes[1].set_xlabel('RP from Daily Data (Years)')
    axes[1].set_ylabel('RP from Annual Data (Years)')
    axes[1].set_title('Return Period Comparison (99th Percentile)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.suptitle('Overestimation Analysis Summary (99th Percentile)', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, 'Figure_5_8_Overestimation_Summary.png'), dpi=150)
    plt.close()
    print("  Created Figure 5.8: Overestimation Summary (99th Percentile)")
    
    print(f"\nAll figures saved to: {figures_dir}")


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    print("="*70)
    print("L-MOMENTS FLOOD FREQUENCY ANALYSIS")
    print("Complete Analysis for Research Objectives 1-4")
    print("="*70)
    
    # ========== ANNUAL MAXIMUM SERIES ANALYSIS ==========
    print(f"\n{'='*70}")
    print("ANNUAL MAXIMUM SERIES (AMS) ANALYSIS")
    print(f"{'='*70}")
    
    # Objective 1: Parameter Estimation (Annual)
    annual_obj1 = objective1_parameter_estimation(ANNUAL_DIR, 'Annual')
    annual_obj1.to_csv(os.path.join(RESULTS_DIR, 'Annual', 'obj1_parameter_estimation.csv'), index=False)
    
    # Objective 2: Distribution Selection (Annual)
    annual_obj2 = objective2_distribution_selection(ANNUAL_DIR, 'Annual')
    annual_obj2.to_csv(os.path.join(RESULTS_DIR, 'Annual', 'obj2_distribution_selection.csv'), index=False)
    
    # Objective 3: Return Period Analysis (Annual)
    annual_obj3 = objective3_return_period_analysis(ANNUAL_DIR, 'Annual')
    annual_obj3.to_csv(os.path.join(RESULTS_DIR, 'Annual', 'obj3_return_period_analysis.csv'), index=False)
    
    # ========== DAILY RAINFALL SERIES ANALYSIS ==========
    print(f"\n{'='*70}")
    print("DAILY RAINFALL SERIES ANALYSIS")
    print(f"{'='*70}")
    
    # Objective 1: Parameter Estimation (Daily)
    daily_obj1 = objective1_parameter_estimation(DAILY_DIR, 'Daily')
    daily_obj1.to_csv(os.path.join(RESULTS_DIR, 'Daily', 'obj1_parameter_estimation.csv'), index=False)
    
    # Objective 2: Distribution Selection (Daily)
    daily_obj2 = objective2_distribution_selection(DAILY_DIR, 'Daily')
    daily_obj2.to_csv(os.path.join(RESULTS_DIR, 'Daily', 'obj2_distribution_selection.csv'), index=False)
    
    # Objective 3: Return Period Analysis (Daily)
    daily_obj3 = objective3_return_period_analysis(DAILY_DIR, 'Daily')
    daily_obj3.to_csv(os.path.join(RESULTS_DIR, 'Daily', 'obj3_return_period_analysis.csv'), index=False)
    
    # ========== OVERESTIMATION ANALYSIS ==========
    # Objective 4: Overestimation Quantification
    oe_df = objective4_overestimation_analysis(ANNUAL_DIR, DAILY_DIR)
    oe_df.to_csv(os.path.join(RESULTS_DIR, 'Overestimation', 'obj4_overestimation_analysis.csv'), index=False)
    
    # ========== CREATE FIGURES ==========
    create_figures(
        os.path.join(RESULTS_DIR, 'Annual'),
        os.path.join(RESULTS_DIR, 'Daily'),
        oe_df,
        FIGURES_DIR
    )
    
    # ========== SUMMARY ==========
    print(f"\n{'='*70}")
    print("ANALYSIS SUMMARY")
    print(f"{'='*70}")
    
    print("\nBest Distribution Summary (Annual Data):")
    print(annual_obj2['Best_Distribution'].value_counts().to_string())
    
    print("\nBest Distribution Summary (Daily Data):")
    print(daily_obj2['Best_Distribution'].value_counts().to_string())
    
    oe_99 = oe_df[oe_df['Percentile'] == 99]
    print(f"\nOverestimation Summary (99th Percentile):")
    print(f"  Mean OE Factor: {oe_99['OE_Factor'].mean():.2f}x")
    print(f"  Min OE Factor: {oe_99['OE_Factor'].min():.2f}x")
    print(f"  Max OE Factor: {oe_99['OE_Factor'].max():.2f}x")
    print(f"  Mean OE Percentage: {oe_99['OE_Percentage'].mean():.1f}%")
    
    print(f"\n{'='*70}")
    print("ANALYSIS COMPLETE")
    print(f"Results saved to: {RESULTS_DIR}")
    print(f"Figures saved to: {FIGURES_DIR}")
    print(f"{'='*70}")
    
    return {
        'annual_obj1': annual_obj1,
        'annual_obj2': annual_obj2,
        'annual_obj3': annual_obj3,
        'daily_obj1': daily_obj1,
        'daily_obj2': daily_obj2,
        'daily_obj3': daily_obj3,
        'overestimation': oe_df
    }


if __name__ == "__main__":
    results = main()
