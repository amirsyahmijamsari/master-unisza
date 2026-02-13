"""
Temporary script to create histogram for station 0680071RF
For visual inspection only - not for chapter inclusion
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(BASE_DIR, 'Data')
ANNUAL_DIR = os.path.join(DATA_DIR, 'Annual')
DAILY_DIR = os.path.join(DATA_DIR, 'Daily')
FIGURES_DIR = os.path.join(SCRIPT_DIR, 'Figures')

station_id = '0680071RF'
station_name = 'Balai Polis Kg. Dura'

# Read data
annual_file = os.path.join(ANNUAL_DIR, f'{station_id}.csv')
daily_file = os.path.join(DAILY_DIR, f'{station_id}.csv')

annual_data = pd.read_csv(annual_file)['Value (mm)'].dropna()
daily_data = pd.read_csv(daily_file)['Value (mm)'].dropna()
daily_filtered = daily_data[daily_data >= 1.0]

# Create figure with subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Annual Maximum Series Histogram
axes[0].hist(annual_data, bins=20, edgecolor='black', alpha=0.7, color='steelblue')
axes[0].set_xlabel('Rainfall (mm)', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)
axes[0].set_title(f'Annual Maximum Series - {station_name} ({station_id})\n'
                  f'N = {len(annual_data)}, Mean = {annual_data.mean():.2f} mm, '
                  f'Max = {annual_data.max():.2f} mm', fontsize=13)
axes[0].grid(True, alpha=0.3)
axes[0].axvline(annual_data.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {annual_data.mean():.2f} mm')
axes[0].axvline(annual_data.median(), color='green', linestyle='--', linewidth=2, label=f'Median: {annual_data.median():.2f} mm')
axes[0].legend()

# Daily Rainfall Series Histogram (filtered >= 1mm)
axes[1].hist(daily_filtered, bins=50, edgecolor='black', alpha=0.7, color='coral')
axes[1].set_xlabel('Rainfall (mm)', fontsize=12)
axes[1].set_ylabel('Frequency', fontsize=12)
axes[1].set_title(f'Daily Rainfall Series (≥1mm) - {station_name} ({station_id})\n'
                  f'N = {len(daily_filtered)}, Mean = {daily_filtered.mean():.2f} mm, '
                  f'Max = {daily_filtered.max():.2f} mm', fontsize=13)
axes[1].grid(True, alpha=0.3)
axes[1].axvline(daily_filtered.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {daily_filtered.mean():.2f} mm')
axes[1].axvline(daily_filtered.median(), color='green', linestyle='--', linewidth=2, label=f'Median: {daily_filtered.median():.2f} mm')
axes[1].legend()

# Add statistics text box
stats_text = f'Statistics:\n'
stats_text += f'Annual Max - 99th percentile: {np.percentile(annual_data, 99):.2f} mm\n'
stats_text += f'Daily (≥1mm) - 99th percentile: {np.percentile(daily_filtered, 99):.2f} mm\n'
stats_text += f'Annual Max - Max value: {annual_data.max():.2f} mm\n'
stats_text += f'Daily (≥1mm) - Max value: {daily_filtered.max():.2f} mm'

fig.text(0.02, 0.02, stats_text, fontsize=10, verticalalignment='bottom',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

# Save figure
output_file = os.path.join(FIGURES_DIR, 'TEMP_histogram_0680071RF.png')
plt.savefig(output_file, dpi=150, bbox_inches='tight')
print(f"Histogram saved to: {output_file}")
print(f"\nAnnual Max Statistics:")
print(f"  Count: {len(annual_data)}")
print(f"  Mean: {annual_data.mean():.2f} mm")
print(f"  Median: {annual_data.median():.2f} mm")
print(f"  Std: {annual_data.std():.2f} mm")
print(f"  Min: {annual_data.min():.2f} mm")
print(f"  Max: {annual_data.max():.2f} mm")
print(f"  99th percentile: {np.percentile(annual_data, 99):.2f} mm")
print(f"\nDaily (>=1mm) Statistics:")
print(f"  Count: {len(daily_filtered)}")
print(f"  Mean: {daily_filtered.mean():.2f} mm")
print(f"  Median: {daily_filtered.median():.2f} mm")
print(f"  Std: {daily_filtered.std():.2f} mm")
print(f"  Min: {daily_filtered.min():.2f} mm")
print(f"  Max: {daily_filtered.max():.2f} mm")
print(f"  99th percentile: {np.percentile(daily_filtered, 99):.2f} mm")

plt.close()
