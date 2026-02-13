"use client"

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Cell } from 'recharts'
import { GofRecord } from '@/types'

interface MADIBarChartProps {
  data: GofRecord[];
  selectedStation: string;
}

const DIST_COLORS: Record<string, string> = {
  'GUM': '#0891b2',
  'NOR': '#2563eb',
  'EXP': '#7c3aed',
  'GEV': '#db2777',
  'GLO': '#dc2626',
  'GNO': '#ea580c',
  'GPA': '#ca8a04',
  'PE3': '#16a34a',
  'KAP': '#0d9488'
}

export function MADIBarChart({ data, selectedStation }: MADIBarChartProps) {
  const filteredData = data.filter(d => d.stationId === selectedStation && d.madi !== null)
  
  const chartData = filteredData.map(d => ({
    distribution: d.distribution,
    madi: d.madi,
    msdi: d.msdi,
    isBest: d.bestMadi
  })).sort((a, b) => (a.madi || 0) - (b.madi || 0))

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={chartData} margin={{ top: 20, right: 30, bottom: 20, left: 20 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
        <XAxis 
          dataKey="distribution"
          tick={{ fill: '#475569', fontSize: 12 }}
        />
        <YAxis 
          tick={{ fill: '#475569', fontSize: 12 }}
          label={{ value: 'MADI', angle: -90, position: 'insideLeft', fill: '#334155', fontSize: 14 }}
        />
        <Tooltip 
          contentStyle={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '8px', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)' }}
          labelStyle={{ color: '#1e293b', fontWeight: 600 }}
          formatter={(value, name) => [typeof value === 'number' ? value.toFixed(4) : String(value), String(name).toUpperCase()]}
        />
        <Legend />
        <Bar dataKey="madi" name="MADI">
          {chartData.map((entry, index) => (
            <Cell 
              key={`cell-${index}`} 
              fill={entry.isBest ? '#16a34a' : DIST_COLORS[entry.distribution] || '#9ca3af'} 
              stroke={entry.isBest ? '#15803d' : 'none'}
              strokeWidth={entry.isBest ? 2 : 0}
            />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  )
}
