"use client"

import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Station } from '@/types'
import { Card } from '@/components/ui/card'
import { Filter } from 'lucide-react'

interface FilterPanelProps {
  stations: Station[];
  selectedStation: string;
  onStationChange: (value: string) => void;
  selectedDataType: 'annual' | 'daily' | 'both';
  onDataTypeChange: (value: 'annual' | 'daily' | 'both') => void;
  selectedDistrict?: string;
  onDistrictChange?: (value: string) => void;
  selectedDistribution?: string;
  onDistributionChange?: (value: string) => void;
  selectedPercentile?: number;
  onPercentileChange?: (value: number) => void;
  showDataType?: boolean;
  showDistrict?: boolean;
  showDistribution?: boolean;
  showPercentile?: boolean;
}

const DISTRICTS = ['All Districts', 'Kuala Terengganu', 'Dungun', 'Kemaman', 'Marang', 'Hulu Terengganu', 'Setiu', 'Besut']
const DISTRIBUTIONS = ['All', 'GUM', 'NOR', 'EXP', 'GEV', 'GLO', 'GNO', 'GPA', 'PE3', 'KAP']
const PERCENTILES = [50, 75, 90, 95, 99]

export function FilterPanel({
  stations,
  selectedStation,
  onStationChange,
  selectedDataType,
  onDataTypeChange,
  selectedDistrict,
  onDistrictChange,
  selectedDistribution,
  onDistributionChange,
  selectedPercentile,
  onPercentileChange,
  showDataType = true,
  showDistrict = false,
  showDistribution = false,
  showPercentile = false
}: FilterPanelProps) {
  const filteredStations = selectedDistrict && selectedDistrict !== 'All Districts'
    ? stations.filter(s => s.district === selectedDistrict)
    : stations

  return (
    <Card className="p-4 bg-muted/30 border-dashed">
      <div className="flex flex-col md:flex-row items-start md:items-end gap-4 flex-wrap">
        <div className="flex items-center gap-2 text-sm font-medium text-muted-foreground mr-2 mb-1 md:mb-0 h-9">
          <Filter className="w-4 h-4" />
          <span>Filters:</span>
        </div>

        <div className="flex flex-col gap-1.5 w-full md:w-auto min-w-[200px]">
          <label className="text-xs font-medium text-muted-foreground">Station</label>
          <Select value={selectedStation} onValueChange={onStationChange}>
            <SelectTrigger className="bg-background">
              <SelectValue placeholder="Select station" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Stations</SelectItem>
              {filteredStations.map(station => (
                <SelectItem key={station.id} value={station.id}>
                  {station.name}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        {showDataType && (
          <div className="flex flex-col gap-1.5 w-full md:w-auto min-w-[160px]">
            <label className="text-xs font-medium text-muted-foreground">Data Type</label>
            <Select value={selectedDataType} onValueChange={(v) => onDataTypeChange(v as 'annual' | 'daily' | 'both')}>
              <SelectTrigger className="bg-background">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="both">Both</SelectItem>
                <SelectItem value="annual">Annual Maximum</SelectItem>
                <SelectItem value="daily">Daily Rainfall</SelectItem>
              </SelectContent>
            </Select>
          </div>
        )}

        {showDistrict && onDistrictChange && (
          <div className="flex flex-col gap-1.5 w-full md:w-auto min-w-[160px]">
            <label className="text-xs font-medium text-muted-foreground">District</label>
            <Select value={selectedDistrict || 'All Districts'} onValueChange={onDistrictChange}>
              <SelectTrigger className="bg-background">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                {DISTRICTS.map(district => (
                  <SelectItem key={district} value={district}>
                    {district}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
        )}

        {showDistribution && onDistributionChange && (
          <div className="flex flex-col gap-1.5 w-full md:w-auto min-w-[140px]">
            <label className="text-xs font-medium text-muted-foreground">Distribution</label>
            <Select value={selectedDistribution || 'All'} onValueChange={onDistributionChange}>
              <SelectTrigger className="bg-background">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                {DISTRIBUTIONS.map(dist => (
                  <SelectItem key={dist} value={dist}>
                    {dist}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
        )}

        {showPercentile && onPercentileChange && (
          <div className="flex flex-col gap-1.5 w-full md:w-auto min-w-[120px]">
            <label className="text-xs font-medium text-muted-foreground">Percentile</label>
            <Select 
              value={String(selectedPercentile || 95)} 
              onValueChange={(v) => onPercentileChange(parseInt(v))}
            >
              <SelectTrigger className="bg-background">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                {PERCENTILES.map(p => (
                  <SelectItem key={p} value={String(p)}>
                    {p}th
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
        )}
      </div>
    </Card>
  )
}
