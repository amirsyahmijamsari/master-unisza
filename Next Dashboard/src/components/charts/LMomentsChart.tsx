"use client"

import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Line, ComposedChart } from 'recharts'
import { ParameterRecord } from '@/types'

interface LMomentsChartProps {
  annualData: ParameterRecord[];
  dailyData: ParameterRecord[];
  selectedStation?: string;
}

// Theoretical L-moment ratio curves for various distributions
// τ4 as a function of τ3 for common distributions
const generateDistributionCurves = () => {
  const curves: Record<string, { t3: number; t4: number }[]> = {
    // Generalized Logistic (GLO): τ4 = (1 + 5τ3²) / 6
    GLO: [],
    // Generalized Extreme Value (GEV): approximate relationship
    GEV: [],
    // Generalized Pareto (GPA): τ4 = (1 + 5τ3) * (τ3 + 1) / 20 - approximate
    GPA: [],
    // Pearson Type III (PE3): approximate
    PE3: [],
    // Generalized Normal (GNO/Log-Normal 3): approximate
    GNO: [],
    // Kappa: covers a region
    KAP: [],
  }

  // Generate points for each curve
  for (let t3 = -0.1; t3 <= 0.6; t3 += 0.02) {
    // GLO: τ4 = (1 + 5τ3²) / 6
    curves.GLO.push({ t3, t4: (1 + 5 * t3 * t3) / 6 })
    
    // GEV: τ4 ≈ 0.1070 + 0.1109τ3 + 0.8454τ3² - 0.0622τ3³
    curves.GEV.push({ t3, t4: 0.1070 + 0.1109 * t3 + 0.8454 * t3 * t3 - 0.0622 * t3 * t3 * t3 })
    
    // GPA: τ4 = (1 + τ3)(2 - τ3) / 6, for τ3 >= 0
    if (t3 >= 0) {
      curves.GPA.push({ t3, t4: t3 * (1 + t3) / (3 + t3) })
    }
    
    // PE3: τ4 ≈ 0.1224 + 0.30115τ3² + 0.95812τ3⁴
    curves.PE3.push({ t3, t4: 0.1224 + 0.30115 * t3 * t3 + 0.95812 * Math.pow(t3, 4) })
    
    // GNO (Log-Normal): τ4 ≈ 0.1228 + 0.7752τ3² + 0.1122τ3³
    curves.GNO.push({ t3, t4: 0.1228 + 0.7752 * t3 * t3 + 0.1122 * t3 * t3 * t3 })
  }

  return curves
}

const DISTRIBUTION_CURVES = generateDistributionCurves()

const CURVE_COLORS: Record<string, string> = {
  GLO: '#dc2626',
  GEV: '#2563eb',
  GPA: '#16a34a',
  PE3: '#9333ea',
  GNO: '#ea580c',
}

export function LMomentsChart({ annualData, dailyData, selectedStation }: LMomentsChartProps) {
  const filterData = (data: ParameterRecord[]) => {
    if (selectedStation && selectedStation !== 'all') {
      return data.filter(d => d.stationId === selectedStation)
    }
    return data
  }

  const annualPoints = filterData(annualData).map(d => ({
    t3: d.t3LSkewness,
    t4: d.t4LKurtosis,
    name: d.stationName,
    id: d.stationId,
    type: 'Annual'
  }))

  const dailyPoints = filterData(dailyData).map(d => ({
    t3: d.t3LSkewness,
    t4: d.t4LKurtosis,
    name: d.stationName,
    id: d.stationId,
    type: 'Daily'
  }))

  // Combine all data for the chart
  const allCurveData: Record<string, number>[] = []
  const t3Values = DISTRIBUTION_CURVES.GLO.map(p => p.t3)
  
  t3Values.forEach((t3, i) => {
    const point: Record<string, number> = { t3 }
    Object.entries(DISTRIBUTION_CURVES).forEach(([dist, curve]) => {
      const curvePoint = curve.find(p => Math.abs(p.t3 - t3) < 0.001)
      if (curvePoint) {
        point[dist] = curvePoint.t4
      }
    })
    allCurveData.push(point)
  })

  return (
    <ResponsiveContainer width="100%" height={450}>
      <ComposedChart margin={{ top: 20, right: 30, bottom: 40, left: 20 }} data={allCurveData}>
        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
        <XAxis 
          type="number" 
          dataKey="t3" 
          domain={[-0.1, 0.6]}
          tick={{ fill: '#475569', fontSize: 12 }}
          tickFormatter={(v) => v.toFixed(1)}
          label={{ value: 'L-Skewness (τ₃)', position: 'bottom', offset: 10, fill: '#334155', fontSize: 14 }}
        />
        <YAxis 
          type="number" 
          domain={[0, 0.4]}
          tick={{ fill: '#475569', fontSize: 12 }}
          tickFormatter={(v) => v.toFixed(2)}
          label={{ value: 'L-Kurtosis (τ₄)', angle: -90, position: 'insideLeft', fill: '#334155', fontSize: 14 }}
        />
        <Tooltip 
          cursor={{ strokeDasharray: '3 3' }}
          contentStyle={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '8px', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)' }}
          labelStyle={{ color: '#1e293b', fontWeight: 600 }}
          formatter={(value) => typeof value === 'number' ? value.toFixed(4) : value}
        />
        <Legend wrapperStyle={{ paddingTop: 20 }} />
        
        {/* Distribution curves */}
        {Object.entries(CURVE_COLORS).map(([dist, color]) => (
          <Line
            key={dist}
            type="monotone"
            dataKey={dist}
            stroke={color}
            strokeWidth={2}
            dot={false}
            name={dist}
            connectNulls
          />
        ))}
        
        {/* Scatter points for annual data */}
        <Scatter 
          name="Annual Maximum" 
          data={annualPoints}
          fill="#3b82f6"
          shape="circle"
        >
        </Scatter>
        
        {/* Scatter points for daily data */}
        <Scatter 
          name="Daily Rainfall" 
          data={dailyPoints}
          fill="#f97316"
          shape="diamond"
        >
        </Scatter>
      </ComposedChart>
    </ResponsiveContainer>
  )
}
