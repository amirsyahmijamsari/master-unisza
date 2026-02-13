"use client"

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine, Cell } from 'recharts'
import { OverestimationRecord } from '@/types'

interface OverestimationChartProps {
  data: OverestimationRecord[];
  percentile: number;
  selectedStation?: string;
}

export function OverestimationChart({ data, percentile, selectedStation }: OverestimationChartProps) {
  let filteredData = data.filter(d => d.percentile === percentile && d.oeFactor !== null)
  
  if (selectedStation && selectedStation !== 'all') {
    filteredData = filteredData.filter(d => d.stationId === selectedStation)
  }
  
  const chartData = filteredData
    .map(d => ({
      stationId: d.stationId,
      stationName: d.stationName.length > 20 ? d.stationName.substring(0, 18) + '...' : d.stationName,
      oeFactor: d.oeFactor,
      oePercentage: d.oePercentage,
      magnitude: d.magnitude
    }))
    .sort((a, b) => (a.oeFactor || 0) - (b.oeFactor || 0))

  const meanOE = chartData.reduce((sum, d) => sum + (d.oeFactor || 0), 0) / chartData.length

  const getBarColor = (oeFactor: number | null) => {
    if (!oeFactor) return '#9ca3af'
    if (oeFactor < 2) return '#22c55e'
    if (oeFactor < 4) return '#eab308'
    if (oeFactor < 6) return '#f97316'
    return '#ef4444'
  }

  return (
    <ResponsiveContainer width="100%" height={450}>
      <BarChart 
        data={chartData} 
        layout="vertical"
        margin={{ top: 20, right: 30, bottom: 20, left: 150 }}
      >
        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
        <XAxis 
          type="number"
          tick={{ fill: '#475569', fontSize: 12 }}
          label={{ value: 'Overestimation Factor (OE)', position: 'bottom', fill: '#334155', fontSize: 14 }}
        />
        <YAxis 
          type="category"
          dataKey="stationName"
          tick={{ fill: '#475569', fontSize: 11 }}
          width={140}
        />
        <Tooltip 
          contentStyle={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '8px', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)' }}
          labelStyle={{ color: '#1e293b', fontWeight: 600 }}
          formatter={(value, name) => {
            if (name === 'oeFactor' && typeof value === 'number') return [`${value.toFixed(2)}x`, 'OE Factor']
            return [String(value), String(name)]
          }}
        />
        <Legend />
        <ReferenceLine x={1} stroke="#16a34a" strokeDasharray="5 5" label={{ value: 'No Overestimation', fill: '#16a34a', fontSize: 10 }} />
        <ReferenceLine x={meanOE} stroke="#dc2626" strokeWidth={2} label={{ value: `Mean: ${meanOE.toFixed(2)}x`, fill: '#dc2626', fontSize: 10 }} />
        <Bar dataKey="oeFactor" name="OE Factor">
          {chartData.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={getBarColor(entry.oeFactor)} />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  )
}
