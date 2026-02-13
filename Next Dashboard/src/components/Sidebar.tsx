"use client"

import { CloudRain, BarChart3, TrendingUp, Gauge, Table2, LayoutDashboard } from 'lucide-react'
import { cn } from '@/lib/utils'

interface SidebarProps {
  activeTab: string
  onTabChange: (tab: string) => void
}

const navItems = [
  { id: 'overview', label: 'Overview', icon: LayoutDashboard },
  { id: 'lmoments', label: 'L-Moments', icon: CloudRain },
  { id: 'distributions', label: 'Distributions', icon: BarChart3 },
  { id: 'returnperiod', label: 'Return Period', icon: TrendingUp },
  { id: 'overestimation', label: 'Overestimation', icon: Gauge },
  { id: 'data', label: 'Raw Data', icon: Table2 },
]

export function Sidebar({ activeTab, onTabChange }: SidebarProps) {
  return (
    <div className="w-64 border-r bg-card h-screen flex flex-col fixed left-0 top-0 z-20 hidden lg:flex shadow-xl shadow-zinc-200/50">
      <div className="p-6 border-b">
        <div className="flex items-center gap-2">
          <div className="h-8 w-8 rounded-lg bg-primary flex items-center justify-center shadow-md shadow-primary/20">
            <CloudRain className="h-5 w-5 text-primary-foreground" />
          </div>
          <div className="font-bold text-lg tracking-tight text-foreground">FloodFreq<span className="text-primary">AI</span></div>
        </div>
        <p className="text-xs text-muted-foreground mt-2 pl-1">Terengganu Flood Analysis</p>
      </div>
      
      <div className="flex-1 py-6 px-4 space-y-1 overflow-y-auto">
        <div className="text-xs font-semibold text-muted-foreground mb-4 px-2 uppercase tracking-wider">
          Analysis Modules
        </div>
        {navItems.map((item) => (
          <button
            key={item.id}
            onClick={() => onTabChange(item.id)}
            className={cn(
              "w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-all duration-200 ease-in-out",
              activeTab === item.id 
                ? "bg-primary text-primary-foreground shadow-md shadow-primary/20 translate-x-1" 
                : "text-muted-foreground hover:bg-muted hover:text-foreground hover:translate-x-1"
            )}
          >
            <item.icon className="h-4 w-4" />
            {item.label}
          </button>
        ))}
      </div>

      <div className="p-6 border-t bg-muted/30">
        <div className="flex items-center gap-3">
          <div className="h-10 w-10 rounded-full bg-background border flex items-center justify-center shadow-sm">
            <span className="font-semibold text-xs text-muted-foreground">MS</span>
          </div>
          <div>
            <p className="text-sm font-medium text-foreground">Master Thesis</p>
            <p className="text-xs text-muted-foreground">UniSZA</p>
          </div>
        </div>
      </div>
    </div>
  )
}

