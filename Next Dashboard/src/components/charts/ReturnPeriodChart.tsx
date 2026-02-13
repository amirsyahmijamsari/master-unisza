"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { ReturnPeriodRecord } from '@/types'

interface ReturnPeriodChartProps {
  data: ReturnPeriodRecord[];
  selectedStations: string[];
  dataType: 'annual' | 'daily';
}

const COLORS = [
  '#0891b2', '#2563eb', '#7c3aed', '#db2777', '#dc2626',
  '#ea580c', '#ca8a04', '#16a34a', '#0d9488', '#4f46e5'
]

export function ReturnPeriodChart({ data, selectedStations, dataType }: ReturnPeriodChartProps) {
  // Group data by station
  const stationsToShow = selectedStations.length > 0 
    ? selectedStations.filter(s => s !== 'all')
    : [...new Set(data.map(d => d.stationId))].slice(0, 5)
  
  // Transform data for recharts
  const returnPeriods = [...new Set(data.map(d => d.returnPeriod))].sort((a, b) => a - b)
  
  const chartData = returnPeriods.map(rp => {
    const point: Record<string, number | string> = { returnPeriod: rp }
    stationsToShow.forEach(stationId => {
      const record = data.find(d => d.stationId === stationId && d.returnPeriod === rp)
      if (record) {
        point[stationId] = record.returnValue
      }
    })
    return point
  })

  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={chartData} margin={{ top: 20, right: 30, bottom: 20, left: 20 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
        <XAxis 
          dataKey="returnPeriod" 
          scale="log"
          domain={['auto', 'auto']}
          tick={{ fill: '#475569', fontSize: 12 }}
          label={{ value: 'Return Period (Years)', position: 'bottom', fill: '#334155', fontSize: 14 }}
        />
        <YAxis 
          tick={{ fill: '#475569', fontSize: 12 }}
          label={{ value: 'Return Value (mm)', angle: -90, position: 'insideLeft', fill: '#334155', fontSize: 14 }}
        />
        <Tooltip 
          contentStyle={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '8px', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)' }}
          labelStyle={{ color: '#1e293b', fontWeight: 600 }}
          formatter={(value) => typeof value === 'number' ? `${value.toFixed(1)} mm` : String(value)}
          labelFormatter={(value) => `${value}-year Return Period`}
        />
        <Legend />
        {stationsToShow.map((stationId, index) => {
          const stationData = data.find(d => d.stationId === stationId)
          return (
            <Line
              key={stationId}
              type="monotone"
              dataKey={stationId}
              name={stationData?.stationName || stationId}
              stroke={COLORS[index % COLORS.length]}
              strokeWidth={2}
              dot={{ fill: COLORS[index % COLORS.length], r: 4 }}
              activeDot={{ r: 6 }}
            />
          )
        })}
      </LineChart>
    </ResponsiveContainer>
  )
}
