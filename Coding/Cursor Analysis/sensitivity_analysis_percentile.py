"""
SENSITIVITY ANALYSIS: Percentile Threshold Choice
==================================================
Tests whether the overestimation factor (OE) is stable across different
percentile thresholds used as the "test magnitude" M in:

    OE(M) = RP_AM(M) / (RP_daily(M) / 365.25)

Percentiles tested: 90, 95, 97, 99, 99.5, 99.9 (of complete daily series)

Output:
  - Results/Overestimation/sensitivity_percentile.csv
  - Figures/Figure_5_9_Sensitivity_Percentile_Line.png
  - Figures/Figure_5_10_Sensitivity_Percentile_Heatmap.png

Author: Research Thesis
"""

import os
import pandas as pd
import numpy as np
import lmoments3 as lm
from lmoments3 import distr
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# PATHS  (mirrors complete_analysis.py layout)
# ============================================================================
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
BASE_DIR    = os.path.dirname(SCRIPT_DIR)
DATA_DIR    = os.path.join(BASE_DIR, 'Data')
ANNUAL_DIR  = os.path.join(DATA_DIR, 'Annual')
DAILY_DIR   = os.path.join(DATA_DIR, 'Daily')
RESULTS_DIR = os.path.join(SCRIPT_DIR, 'Results', 'Overestimation')
FIGURES_DIR = os.path.join(SCRIPT_DIR, 'Figures')

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

# ============================================================================
# CONFIGURATION
# ============================================================================
DISTRIBUTIONS = ['gum', 'nor', 'exp', 'gev', 'glo', 'gno', 'gpa', 'pe3', 'kap']

# Percentiles to test (of the COMPLETE daily series including zeros — CTA approach)
TEST_PERCENTILES = [90, 95, 97, 99, 99.5, 99.9]

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
    '0700131RF': 'JPS Jertih, Besut',
}

# ============================================================================
# HELPER FUNCTIONS  (self-contained, mirrors complete_analysis.py)
# ============================================================================

def fit_distributions(data):
    params = {}
    clean = data[~np.isnan(data)] if isinstance(data, np.ndarray) else data.dropna().values
    for name in DISTRIBUTIONS:
        try:
            fitted = getattr(distr, name).lmom_fit(clean)
            params[name] = dict(fitted)
        except Exception:
            params[name] = None
    return params


def gringorten_pp(n):
    return np.array([(i - 0.44) / (n + 0.12) for i in range(1, n + 1)])


def best_distribution(data, params):
    clean = data[~np.isnan(data)] if isinstance(data, np.ndarray) else data.dropna().values
    sorted_data = np.sort(clean)
    n = len(sorted_data)
    pp = gringorten_pp(n)
    best_name, best_madi = None, np.inf
    for name, p in params.items():
        if p is None:
            continue
        try:
            q = getattr(distr, name).ppf(pp, **p)
            with np.errstate(divide='ignore', invalid='ignore'):
                nd = (sorted_data - q) / sorted_data
                nd = np.where(np.isfinite(nd), nd, 0)
            madi = float(np.mean(np.abs(nd)))
            if madi < best_madi:
                best_madi, best_name = madi, name
        except Exception:
            continue
    return best_name


def return_period_for_value(params, dist_name, value):
    """Return period (in native units of the fitted data) for a given magnitude."""
    if params.get(dist_name) is None:
        return None
    try:
        prob = getattr(distr, dist_name).cdf(value, **params[dist_name])
        if prob >= 1.0:
            return np.inf
        if prob <= 0.0:
            return None
        return 1.0 / (1.0 - prob)
    except Exception:
        return None


# ============================================================================
# MAIN SENSITIVITY ANALYSIS
# ============================================================================

def run_sensitivity():
    print("=" * 65)
    print("SENSITIVITY ANALYSIS: Percentile Threshold Choice")
    print("=" * 65)

    annual_files = set(f for f in os.listdir(ANNUAL_DIR) if f.endswith('.csv'))
    daily_files  = set(f for f in os.listdir(DAILY_DIR)  if f.endswith('.csv'))
    common_files = sorted(annual_files & daily_files)

    records = []

    for csv_file in common_files:
        station_id   = csv_file.replace('.csv', '')
        station_name = STATION_NAMES.get(station_id, station_id)
        print(f"\n  Processing: {station_id} — {station_name}")

        # --- Load data ---
        annual_data = pd.read_csv(os.path.join(ANNUAL_DIR, csv_file))['Value (mm)'].dropna().values
        daily_raw   = pd.read_csv(os.path.join(DAILY_DIR,  csv_file))['Value (mm)'].dropna().values
        daily_wet   = daily_raw[daily_raw >= 1.0]   # >=1mm for distribution fitting

        # --- Fit distributions ---
        annual_params = fit_distributions(annual_data)
        daily_params  = fit_distributions(daily_wet)

        best_annual = best_distribution(annual_data, annual_params)
        best_daily  = best_distribution(daily_wet,   daily_params)

        if best_annual is None or best_daily is None:
            print(f"    WARNING: could not identify best distribution — skipping")
            continue

        print(f"    Best AMS dist : {best_annual.upper()}")
        print(f"    Best Daily dist: {best_daily.upper()}")

        # --- Loop over percentiles ---
        for pct in TEST_PERCENTILES:
            # Test magnitude from the COMPLETE series (CTA approach — includes zeros)
            M = float(np.percentile(daily_raw, pct))

            rp_am    = return_period_for_value(annual_params, best_annual, M)
            rp_daily = return_period_for_value(daily_params,  best_daily,  M)

            if rp_am is None or rp_daily is None:
                continue
            if rp_am <= 0 or rp_daily <= 0 or np.isinf(rp_am):
                continue

            rp_daily_years = rp_daily / 365.25
            oe_factor  = rp_am / rp_daily_years if rp_daily_years > 0 else np.inf
            oe_percent = (oe_factor - 1) * 100

            records.append({
                'Station_ID':        station_id,
                'Station_Name':      station_name,
                'Percentile':        pct,
                'Magnitude_mm':      round(M, 2),
                'Best_Annual_Dist':  best_annual.upper(),
                'Best_Daily_Dist':   best_daily.upper(),
                'RP_Annual_Years':   round(rp_am, 4),
                'RP_Daily_Days':     round(rp_daily, 2),
                'RP_Daily_Years':    round(rp_daily_years, 4),
                'OE_Factor':         round(oe_factor, 4),
                'OE_Percentage':     round(oe_percent, 2),
            })

            print(f"    {pct:5.1f}th pct  M={M:7.2f} mm  "
                  f"RP_AM={rp_am:.2f} yr  "
                  f"RP_daily={rp_daily:.1f} d  "
                  f"OE={oe_factor:.2f}x ({oe_percent:.0f}%)")

    df = pd.DataFrame(records)
    out_csv = os.path.join(RESULTS_DIR, 'sensitivity_percentile.csv')
    df.to_csv(out_csv, index=False)
    print(f"\n  Results saved -> {out_csv}")
    return df


# ============================================================================
# SUMMARY TABLE  (printed and returned)
# ============================================================================

def print_summary(df):
    print("\n" + "=" * 65)
    print("SENSITIVITY SUMMARY TABLE (all 20 stations)")
    print("=" * 65)
    print(f"{'Percentile':>12} {'N stations':>10} {'Mean Magnitude':>16} "
          f"{'Mean OE Factor':>15} {'Min OE':>8} {'Max OE':>8} {'Mean OE%':>10}")
    print("-" * 82)

    summary_rows = []
    for pct in TEST_PERCENTILES:
        sub = df[df['Percentile'] == pct]
        valid = sub[np.isfinite(sub['OE_Factor'])]
        if valid.empty:
            continue
        row = {
            'Percentile':    pct,
            'N_Stations':    len(valid),
            'Mean_Mag_mm':   valid['Magnitude_mm'].mean(),
            'Mean_OE_Factor': valid['OE_Factor'].mean(),
            'Min_OE_Factor': valid['OE_Factor'].min(),
            'Max_OE_Factor': valid['OE_Factor'].max(),
            'Std_OE_Factor': valid['OE_Factor'].std(),
            'Mean_OE_Pct':   valid['OE_Percentage'].mean(),
        }
        summary_rows.append(row)
        print(f"{pct:>12.1f} {row['N_Stations']:>10} {row['Mean_Mag_mm']:>16.2f} "
              f"{row['Mean_OE_Factor']:>15.2f} {row['Min_OE_Factor']:>8.2f} "
              f"{row['Max_OE_Factor']:>8.2f} {row['Mean_OE_Pct']:>10.1f}%")

    summary_df = pd.DataFrame(summary_rows)
    out_csv = os.path.join(RESULTS_DIR, 'sensitivity_summary.csv')
    summary_df.to_csv(out_csv, index=False)
    print(f"\n  Summary saved -> {out_csv}")
    return summary_df


# ============================================================================
# FIGURES
# ============================================================================

def create_figures(df, summary_df):
    # --- Colour palette & label map ---
    PCT_COLORS  = {90: '#4393c3', 95: '#2166ac', 97: '#f4a582',
                   99: '#d6604d', 99.5: '#b2182b', 99.9: '#67001f'}
    PCT_LABELS  = {p: f'{p}th' if p < 99.5 else f'{p}th' for p in TEST_PERCENTILES}
    VALID_PCTS  = [p for p in TEST_PERCENTILES if p in df['Percentile'].values]

    # ── Figure 5.9: Line chart — OE Factor by station for each percentile ──
    stations = sorted(df['Station_ID'].unique())
    n_st = len(stations)
    x    = np.arange(n_st)

    fig, axes = plt.subplots(2, 1, figsize=(16, 12), sharex=True,
                             gridspec_kw={'height_ratios': [3, 1]})

    ax_main = axes[0]
    for pct in VALID_PCTS:
        sub = df[df['Percentile'] == pct].set_index('Station_ID')
        y   = [sub.loc[s, 'OE_Factor'] if s in sub.index else np.nan for s in stations]
        ax_main.plot(x, y, marker='o', markersize=5, linewidth=1.8,
                     color=PCT_COLORS[pct], label=f'{PCT_LABELS[pct]} percentile',
                     alpha=0.9)

    ax_main.set_ylabel('Overestimation Factor (×)', fontsize=12)
    ax_main.set_title('Sensitivity Analysis: OE Factor Across Percentile Thresholds\n'
                      '(All 20 Terengganu Stations)', fontsize=13, fontweight='bold')
    ax_main.legend(title='Percentile', fontsize=10, title_fontsize=10,
                   loc='upper left', ncol=2)
    ax_main.grid(True, alpha=0.3, linestyle='--')
    ax_main.set_ylim(bottom=0)

    # Shade the 99th percentile band
    sub99 = df[df['Percentile'] == 99].set_index('Station_ID')
    y99 = [sub99.loc[s, 'OE_Factor'] if s in sub99.index else np.nan for s in stations]
    ax_main.fill_between(x, 0, y99, alpha=0.07, color=PCT_COLORS[99],
                         label='_nolegend_')

    # --- Bottom panel: coefficient of variation across percentiles per station ---
    ax_cv = axes[1]
    cv_vals = []
    for s in stations:
        sub_s = df[df['Station_ID'] == s]['OE_Factor'].replace([np.inf], np.nan).dropna()
        cv = sub_s.std() / sub_s.mean() if sub_s.mean() != 0 else np.nan
        cv_vals.append(cv)
    ax_cv.bar(x, cv_vals, color='steelblue', alpha=0.75, edgecolor='white')
    ax_cv.axhline(np.nanmean(cv_vals), color='red', linestyle='--',
                  linewidth=1.5, label=f'Mean CV = {np.nanmean(cv_vals):.3f}')
    ax_cv.set_ylabel('CV of OE Factor', fontsize=10)
    ax_cv.set_title('Coefficient of Variation across Percentiles (lower = more stable)',
                    fontsize=10)
    ax_cv.legend(fontsize=9)
    ax_cv.grid(True, alpha=0.3, linestyle='--')
    ax_cv.set_xticks(x)
    ax_cv.set_xticklabels(stations, rotation=45, ha='right', fontsize=8)

    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'Figure_5_9_Sensitivity_Percentile_Line.png')
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n  Saved -> {fig_path}")

    # ── Figure 5.10: Summary bar + table panel ──
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left — grouped bar chart: mean, min, max OE Factor
    pct_labels = [f'{p}th' for p in summary_df['Percentile']]
    x_s = np.arange(len(summary_df))
    w   = 0.25
    ax  = axes[0]
    ax.bar(x_s - w, summary_df['Mean_OE_Factor'], width=w, label='Mean OE',
           color='steelblue', alpha=0.85, edgecolor='white')
    ax.bar(x_s,     summary_df['Min_OE_Factor'],  width=w, label='Min OE',
           color='#74c5a2', alpha=0.85, edgecolor='white')
    ax.bar(x_s + w, summary_df['Max_OE_Factor'],  width=w, label='Max OE',
           color='#e07070', alpha=0.85, edgecolor='white')
    # Error bars for std
    ax.errorbar(x_s - w, summary_df['Mean_OE_Factor'],
                yerr=summary_df['Std_OE_Factor'],
                fmt='none', color='black', capsize=4, linewidth=1.2)
    ax.set_xticks(x_s)
    ax.set_xticklabels(pct_labels, fontsize=11)
    ax.set_xlabel('Percentile Threshold', fontsize=12)
    ax.set_ylabel('Overestimation Factor (×)', fontsize=12)
    ax.set_title('OE Factor Statistics Across\nPercentile Thresholds', fontsize=12,
                 fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')
    ax.set_ylim(bottom=0)

    # Annotate mean values on bars
    for i, v in enumerate(summary_df['Mean_OE_Factor']):
        ax.text(x_s[i] - w, v + 0.1, f'{v:.2f}×', ha='center', va='bottom',
                fontsize=8, fontweight='bold')

    # Right — summary numeric table
    ax2 = axes[1]
    ax2.axis('off')
    col_labels = ['Percentile', 'N', 'Mean M (mm)', 'Mean OE', 'Min OE',
                  'Max OE', 'Std OE', 'Mean OE%']
    table_data = []
    for _, row in summary_df.iterrows():
        table_data.append([
            f"{row['Percentile']:.1f}th",
            int(row['N_Stations']),
            f"{row['Mean_Mag_mm']:.1f}",
            f"{row['Mean_OE_Factor']:.2f}×",
            f"{row['Min_OE_Factor']:.2f}×",
            f"{row['Max_OE_Factor']:.2f}×",
            f"{row['Std_OE_Factor']:.2f}",
            f"{row['Mean_OE_Pct']:.0f}%",
        ])
    tbl = ax2.table(cellText=table_data, colLabels=col_labels,
                    cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    # Style header
    for j in range(len(col_labels)):
        tbl[(0, j)].set_facecolor('#2c5f8a')
        tbl[(0, j)].set_text_props(color='white', fontweight='bold')
    # Highlight 99th row
    for i, row in enumerate(summary_df.itertuples(), start=1):
        if row.Percentile == 99:
            for j in range(len(col_labels)):
                tbl[(i, j)].set_facecolor('#fff3cd')

    ax2.set_title('Sensitivity Analysis — Numeric Summary\n(yellow = adopted 99th percentile)',
                  fontsize=10, fontweight='bold', pad=10)

    plt.suptitle('Overestimation Factor: Sensitivity to Percentile Threshold Choice',
                 fontsize=13, fontweight='bold', y=1.01)
    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'Figure_5_10_Sensitivity_Percentile_Heatmap.png')
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved -> {fig_path}")


# ============================================================================
# RUN
# ============================================================================

if __name__ == '__main__':
    df         = run_sensitivity()
    summary_df = print_summary(df)
    create_figures(df, summary_df)

    print("\n" + "=" * 65)
    print("DONE - Sensitivity analysis complete.")
    print(f"  CSVs  -> {RESULTS_DIR}")
    print(f"  Figs  -> {FIGURES_DIR}")
    print("=" * 65)
