"use client"

import * as React from "react"
import { LucideIcon } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"
import { cn } from "@/lib/utils"

interface StatsCardProps {
  title: string
  value: string | number
  subtitle?: string
  icon: LucideIcon
  className?: string
  trend?: {
    value: string
    isPositive: boolean
  }
}

export function StatsCard({ 
  title, 
  value, 
  subtitle, 
  icon: Icon,
  className,
  trend 
}: StatsCardProps) {
  return (
    <Card className={cn("overflow-hidden relative", className)}>
      <CardContent className="p-6">
        <div className="flex items-center justify-between space-y-0 pb-2">
          <p className="text-sm font-medium text-muted-foreground">{title}</p>
          <div className="p-2 bg-primary/10 rounded-full">
            <Icon className="h-4 w-4 text-primary" />
          </div>
        </div>
        <div className="flex flex-col gap-1">
          <div className="text-2xl font-bold tracking-tight">{value}</div>
          {subtitle && (
            <p className="text-xs text-muted-foreground">{subtitle}</p>
          )}
          {trend && (
            <div className={cn(
              "flex items-center text-xs mt-1 font-medium",
              trend.isPositive ? "text-green-600" : "text-red-600"
            )}>
              {trend.value}
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  )
}
