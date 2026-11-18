import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# Set standard academic typography with 12 pt baseline matching Word body text 1:1
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.labelsize'] = 12.5
plt.rcParams['xtick.labelsize'] = 11.5
plt.rcParams['ytick.labelsize'] = 11.5
plt.rcParams['legend.fontsize'] = 10.5

# Load daily data for 0630011RF (JPS Kemaman) - highest completeness in network (98.33%)
df_daily = pd.read_csv('Coding/Data/Daily/0630011RF.csv')
df_daily['Date'] = pd.to_datetime(df_daily['Date'], format='%d/%m/%Y')
df_daily['Year'] = df_daily['Date'].dt.year

df_ann = pd.read_csv('Coding/Data/Annual/0630011RF.csv')

# Find exact dates of Annual Maxima
ams_records = []
for _, row in df_ann.iterrows():
    yr = int(row['Year'])
    val = row['Value (mm)']
    matches = df_daily[(df_daily['Year'] == yr) & (np.isclose(df_daily['Value (mm)'], val, atol=0.2))]
    if not matches.empty:
        ams_records.append({'Date': matches.iloc[0]['Date'], 'Year': yr, 'Value (mm)': matches.iloc[0]['Value (mm)']})
    else:
        sub = df_daily[df_daily['Year'] == yr]
        if not sub.empty:
            max_row = sub.loc[sub['Value (mm)'].idxmax()]
            ams_records.append({'Date': max_row['Date'], 'Year': yr, 'Value (mm)': max_row['Value (mm)']})

df_ams = pd.DataFrame(ams_records)

def overlaps(b1, b2):
    return not (b1.x1 < b2.x0 or b1.x0 > b2.x1 or b1.y1 < b2.y0 or b1.y0 > b2.y1)

# =====================================================================
# FIGURE 4.1: Multi-Decade Complete Daily Series vs. AMS (1970–2022)
# Direct 1:1 scale (6.5 x 4.8 in) with 12 pt thesis typography
# =====================================================================
fig1, ax1 = plt.subplots(figsize=(6.5, 4.8), dpi=300)

ax1.plot(df_daily['Date'], df_daily['Value (mm)'], color='#3B6978', linewidth=0.7, alpha=0.75, 
         label='Complete Daily Series ($N = 18,983$)')
ax1.scatter(df_ams['Date'], df_ams['Value (mm)'], color='#D90429', s=38, zorder=5, edgecolor='black', linewidth=0.6, 
            label='Retained AMS ($N = 51$)')
ax1.axhline(100, color='#D48C00', linestyle='--', linewidth=1.3, alpha=0.9, 
            label='Extreme Threshold (100 mm)')

ax1.set_xlabel('Observation Year (1970–2022)', fontweight='bold', fontsize=12.5, labelpad=6)
ax1.set_ylabel('Daily Precipitation (mm)', fontweight='bold', fontsize=12.5, labelpad=6)
ax1.tick_params(axis='both', which='major', labelsize=11.5)
ax1.set_xlim(pd.Timestamp('1970-01-01'), pd.Timestamp('2023-06-01'))
ax1.set_ylim(-20, 1050)
ax1.set_yticks([0, 200, 400, 600, 800, 1000])
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.xaxis.set_major_locator(mdates.YearLocator(10))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax1.xaxis.set_minor_locator(mdates.YearLocator(2))

# Top legend in 1 horizontal row
leg1 = ax1.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), ncol=3, framealpha=0.95, edgecolor='#C0C0C0', fontsize=10.5)

# Statistical Summary Inset Box in upper left (1971–1983)
stats_text = (
    "Station: 0630011RF (Kemaman)\n"
    "• Period: 1970–2022 (53 yrs)\n"
    "• Total Daily Records: 18,983\n"
    "• Days ≥ 100 mm: 179 storms\n"
    "• Retained by AMS: 51 events\n"
    "• Discarded ≥ 100 mm: 128 (71.5%)\n"
    "• Decimation Ratio: > 99.7%"
)
txt1 = ax1.text(0.02, 0.96, stats_text, transform=ax1.transAxes, verticalalignment='top',
                fontsize=9.8, bbox=dict(boxstyle='square,pad=0.35', facecolor='#F8F9FA', edgecolor='#A0A0A0', alpha=0.95))

# 1 Dec 1988 extreme storm (625.5 mm)
ann_1988 = ax1.annotate('1 Dec 1988:\n625.5 mm', 
             xy=(pd.Timestamp('1988-12-01'), 625.5), 
             xytext=(pd.Timestamp('1988-12-01'), 480),
             arrowprops=dict(arrowstyle='->', color='#333333', lw=1.1),
             fontsize=10.5, ha='center',
             bbox=dict(boxstyle='square,pad=0.3', facecolor='#FFFFFF', edgecolor='#666666', alpha=0.92))

# 14 Oct 2002 historic record (855.8 mm)
ann_2002 = ax1.annotate('Historic Extreme\n14 Oct 2002: 855.8 mm', 
             xy=(pd.Timestamp('2002-10-14'), 855.8), 
             xytext=(pd.Timestamp('2011-01-01'), 870),
             arrowprops=dict(arrowstyle='->', color='#D90429', lw=1.3),
             fontsize=11.0, fontweight='bold', color='#D90429', ha='center',
             bbox=dict(boxstyle='square,pad=0.35', facecolor='#FFF0F0', edgecolor='#D90429', alpha=0.95))

plt.tight_layout()
fig1.canvas.draw()
r1 = fig1.canvas.get_renderer()
b_txt1 = txt1.get_window_extent(r1)
b_1988 = ann_1988.get_bbox_patch().get_window_extent(r1)
b_2002 = ann_2002.get_bbox_patch().get_window_extent(r1)

fig1_overlaps = [
    ('Txt vs 1988', overlaps(b_txt1, b_1988)),
    ('Txt vs 2002', overlaps(b_txt1, b_2002)),
    ('1988 vs 2002', overlaps(b_1988, b_2002))
]
print("Figure 4.1 overlap checks:", fig1_overlaps)
assert not any(v for _, v in fig1_overlaps), "Overlap detected in Figure 4.1!"

out_fig1 = 'Chapter 4 - RESEARCH GAP/Figure_4_1_Multi_Decade_Data_Decimation.png'
plt.savefig(out_fig1, dpi=300)
plt.close(fig1)
print(f'Successfully generated: {out_fig1}')

# =====================================================================
# FIGURE 4.2: Representative Monsoonal Year (2009) Zoom-In
# Direct 1:1 scale (6.5 x 5.0 in) with 12 pt thesis typography
# =====================================================================
df_2009 = df_daily[df_daily['Year'] == 2009].copy().sort_values('Date')
ams_2009 = df_ams[df_ams['Year'] == 2009]
ams_val = ams_2009['Value (mm)'].values[0] if not ams_2009.empty else 257.9
ams_date = ams_2009['Date'].values[0] if not ams_2009.empty else pd.Timestamp('2009-12-01')
sec_2009 = df_2009[(df_2009['Value (mm)'] >= 100.0) & (df_2009['Date'] != ams_date)]

fig2, ax2 = plt.subplots(figsize=(6.5, 5.0), dpi=300)

ax2.bar(df_2009['Date'], df_2009['Value (mm)'], width=1.0, color='#3B6978', alpha=0.75, 
        label='Daily Rainfall (365 days)')
ax2.scatter([ams_date], [ams_val], color='#D90429', s=75, marker='o', zorder=6, edgecolor='black', linewidth=0.9,
            label='Retained AMS (1 Dec: 257.9 mm)')
ax2.scatter(sec_2009['Date'], sec_2009['Value (mm)'], color='#D48C00', s=60, marker='^', zorder=5, edgecolor='black', linewidth=0.7,
            label='Discarded Secondary (≥ 100 mm)')
ax2.axhline(100, color='#D48C00', linestyle='--', linewidth=1.3, alpha=0.85, 
            label='Extreme Threshold (100 mm)')
ax2.axhline(96.5, color='#6C757D', linestyle=':', linewidth=1.3, alpha=0.85, 
            label='Median AMS Drier Years (96.5 mm)')

ax2.set_xlabel('Date (Calendar Year 2009)', fontweight='bold', fontsize=12.5, labelpad=6)
ax2.set_ylabel('Daily Precipitation (mm)', fontweight='bold', fontsize=12.5, labelpad=6)
ax2.tick_params(axis='both', which='major', labelsize=11.5)
ax2.set_xlim(pd.Timestamp('2009-01-01'), pd.Timestamp('2010-01-10'))
ax2.set_ylim(-10, 420)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

# Top legend in 2 rows
leg2 = ax2.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), ncol=2, framealpha=0.95, edgecolor='#C0C0C0', fontsize=10.2)

# Consolidated callout for Northeast Monsoon compound deluges
cluster_text = (
    "Northeast Monsoon Compound Deluges:\n"
    "• 1st Deluge (Nov 20–22): 210.8, 226.8, 200.0 mm\n"
    "   All 3 severe storms discarded by AMS\n"
    "• 2nd Deluge (Nov 30–Dec 2): 188.2, 257.9, 156.4 mm\n"
    "   Only 1 peak kept; 2 severe storms discarded"
)
ann_cluster = ax2.annotate(cluster_text,
            xy=(pd.Timestamp('2009-11-21'), 226.8),
            xytext=(pd.Timestamp('2009-03-20'), 175),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=1.2, connectionstyle='arc3,rad=-0.08'),
            fontsize=10.2,
            bbox=dict(boxstyle='square,pad=0.45', facecolor='#FFFFFF', edgecolor='#666666', alpha=0.95))

ax2.annotate('',
            xy=(pd.Timestamp('2009-11-30'), 188.2),
            xytext=(pd.Timestamp('2009-08-15'), 185),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=1.2, connectionstyle='arc3,rad=-0.05'))

ann_peak = ax2.annotate('Retained AMS Peak\n(1 Dec: 257.9 mm)', 
             xy=(ams_date, ams_val), 
             xytext=(pd.Timestamp('2009-11-01'), 335),
             arrowprops=dict(arrowstyle='->', color='#D90429', lw=1.3),
             fontsize=10.5, fontweight='bold', color='#D90429',
             bbox=dict(boxstyle='square,pad=0.4', facecolor='#FFF0F0', edgecolor='#D90429', alpha=0.95))

plt.tight_layout()
fig2.canvas.draw()
r2 = fig2.canvas.get_renderer()
b_cl = ann_cluster.get_bbox_patch().get_window_extent(r2)
b_pk = ann_peak.get_bbox_patch().get_window_extent(r2)

fig2_overlaps = [
    ('Cluster vs Peak', overlaps(b_cl, b_pk))
]
print("Figure 4.2 overlap checks:", fig2_overlaps)
assert not any(v for _, v in fig2_overlaps), "Overlap detected in Figure 4.2!"

out_fig2 = 'Chapter 4 - RESEARCH GAP/Figure_4_2_Monsoonal_Multiplicity_2009.png'
plt.savefig(out_fig2, dpi=300)
plt.close(fig2)
print(f'Successfully generated: {out_fig2}')
