# L-Moments Flood Frequency Analysis Dashboard

An interactive Next.js dashboard for visualizing L-moments flood frequency analysis results from Terengganu, Malaysia rainfall stations.

## Features

### Research Objectives Covered

1. **Objective 1: L-Moments Parameter Estimation**
   - View L-moment statistics (L₁, L₂, τ₃, τ₄) for all stations
   - Compare Annual Maximum vs Daily rainfall data
   - L-moment ratio diagram visualization

2. **Objective 2: Distribution Selection**
   - Goodness-of-fit assessment using MADI and MSDI
   - Best distribution identification for each station
   - Distribution comparison charts

3. **Objective 3: Return Period Analysis**
   - Return period curves for multiple stations
   - Quantile estimates for 2-100 year return periods
   - Interactive station selection

4. **Objective 4: Overestimation Quantification**
   - Compare Annual Maxima vs Daily data return periods
   - Overestimation Factor (OE) calculation
   - Overestimation Percentage visualization
   - Percentile-based filtering (50th, 75th, 90th, 95th, 99th)

### Filters Available

- **Station Selection**: Filter by individual station or view all
- **Data Type**: Annual Maximum, Daily Rainfall, or Both
- **District**: Filter stations by Terengganu district
- **Distribution**: Filter by probability distribution type
- **Percentile**: For overestimation analysis (50, 75, 90, 95, 99)

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

```bash
cd "Next Dashboard"
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build for Production

```bash
npm run build
```

### Deploy to Vercel

1. Push to GitHub
2. Import project in Vercel
3. Deploy automatically

Or use Vercel CLI:

```bash
npm i -g vercel
vercel
```

## Data Update

To update the dashboard data from new analysis results:

1. Run the Python analysis scripts in `Coding/Cursor Analysis/`
2. Run the data conversion script:

```bash
cd "Next Dashboard"
python scripts/convert_data.py
```

3. Rebuild and redeploy

## Technology Stack

- **Framework**: Next.js 16 (App Router)
- **Styling**: Tailwind CSS
- **Charts**: Recharts
- **UI Components**: Radix UI primitives
- **Icons**: Lucide React
- **Deployment**: Vercel

## Study Area

The dashboard presents analysis results from 20 rainfall stations across Terengganu, Malaysia:

- Kuala Terengganu District
- Dungun District  
- Kemaman District
- Marang District
- Hulu Terengganu District
- Setiu District
- Besut District

## License

Master Thesis Research Project - University of Sultan Zainal Abidin (UniSZA)
