"use client"

import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { GofRecord } from '@/types'

interface DistributionPieChartProps {
  data: GofRecord[];
  title: string;
}

const COLORS: Record<string, string> = {
  'KAP': '#2563eb',
  'GLO': '#dc2626',
  'PE3': '#16a34a',
  'GNO': '#ea580c',
  'GPA': '#7c3aed',
  'GEV': '#0891b2',
  'GUM': '#db2777',
  'NOR': '#ca8a04',
  'EXP': '#0d9488'
}

export function DistributionPieChart({ data, title }: DistributionPieChartProps) {
  const bestDists = data.filter(d => d.bestMadi)
  const total = bestDists.length
  
  const distCounts: Record<string, number> = {}
  bestDists.forEach(d => {
    distCounts[d.distribution] = (distCounts[d.distribution] || 0) + 1
  })
  
  const chartData = Object.entries(distCounts).map(([name, value]) => ({
    name,
    value,
    percentage: ((value / total) * 100).toFixed(0)
  }))

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const renderLabel = (props: any) => {
    const pct = props.value && total > 0 ? ((props.value / total) * 100).toFixed(0) : '0'
    return `${props.name} (${pct}%)`
  }

  return (
    <div className="text-center">
      <h4 className="text-sm font-medium text-slate-600 mb-2">{title}</h4>
      <ResponsiveContainer width="100%" height={250}>
        <PieChart>
          <Pie
            data={chartData}
            cx="50%"
            cy="50%"
            innerRadius={50}
            outerRadius={80}
            paddingAngle={3}
            dataKey="value"
            label={renderLabel}
            labelLine={{ stroke: '#94a3b8' }}
          >
            {chartData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[entry.name] || '#9ca3af'} />
            ))}
          </Pie>
          <Tooltip 
            contentStyle={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', borderRadius: '8px', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)' }}
          />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  )
}
