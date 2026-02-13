"use client"

import { useState, useMemo } from 'react'
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card'
import { StatsCard } from '@/components/StatsCard'
import { FilterPanel } from '@/components/FilterPanel'
import { DataTable } from '@/components/DataTable'
import { Sidebar } from '@/components/Sidebar'
import { LMomentsChart } from '@/components/charts/LMomentsChart'
import { ReturnPeriodChart } from '@/components/charts/ReturnPeriodChart'
import { OverestimationChart } from '@/components/charts/OverestimationChart'
import { DistributionPieChart } from '@/components/charts/DistributionPieChart'
import { MADIBarChart } from '@/components/charts/MADIBarChart'
import { 
  CloudRain, 
  AlertTriangle, 
  BarChart3, 
  MapPin, 
  Activity,
  Droplets,
  Gauge,
  ArrowRight
} from 'lucide-react'
import { cn } from '@/lib/utils'

import analysisData from '@/data/analysis-results.json'
import { AnalysisData, ParameterRecord, GofRecord, OverestimationRecord } from '@/types'

const data = analysisData as AnalysisData

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('overview')
  const [selectedStation, setSelectedStation] = useState('all')
  const [selectedDataType, setSelectedDataType] = useState<'annual' | 'daily' | 'both'>('both')
  const [selectedDistrict, setSelectedDistrict] = useState('All Districts')
  const [selectedPercentile, setSelectedPercentile] = useState(95)

  // Compute stats
  const stats = useMemo(() => {
    const annualBestDists = data.annual.gof.filter(g => g.bestMadi)
    const dailyBestDists = data.daily.gof.filter(g => g.bestMadi)
    
    const oe95 = data.overestimation.filter(o => o.percentile === 95 && o.oeFactor !== null)
    const meanOE = oe95.reduce((sum, o) => sum + (o.oeFactor || 0), 0) / oe95.length
    
    const kapCount = annualBestDists.filter(g => g.distribution === 'KAP').length
    
    return {
      totalStations: data.stations.length,
      meanOE: meanOE.toFixed(2),
      kapPercentAnnual: ((kapCount / annualBestDists.length) * 100).toFixed(0),
      kapPercentDaily: 100,
      avgMADI_annual: (annualBestDists.reduce((sum, g) => sum + (g.madi || 0), 0) / annualBestDists.length).toFixed(4),
      avgMADI_daily: (dailyBestDists.reduce((sum, g) => sum + (g.madi || 0), 0) / dailyBestDists.length).toFixed(4)
    }
  }, [])

  // Filter data based on selected district
  const filteredStations = useMemo(() => {
    if (selectedDistrict === 'All Districts') return data.stations
    return data.stations.filter(s => s.district === selectedDistrict)
  }, [selectedDistrict])

  const filteredStationIds = useMemo(() => {
    return new Set(filteredStations.map(s => s.id))
  }, [filteredStations])

  return (
    <div className="min-h-screen bg-muted/10">
      <Sidebar activeTab={activeTab} onTabChange={setActiveTab} />
      
      <main className="lg:pl-64 min-h-screen">
        <div className="p-8 max-w-[1600px] mx-auto space-y-8">
          
          {/* Header Section */}
          <div className="flex flex-col gap-1">
            <h1 className="text-3xl font-bold tracking-tight text-foreground">
              {activeTab === 'overview' && 'Dashboard Overview'}
              {activeTab === 'lmoments' && 'L-Moments Analysis'}
              {activeTab === 'distributions' && 'Distribution Fitting'}
              {activeTab === 'returnperiod' && 'Return Period Analysis'}
              {activeTab === 'overestimation' && 'Overestimation Quantification'}
              {activeTab === 'data' && 'Raw Data Explorer'}
          </h1>
            <p className="text-muted-foreground">
              Hydrological analysis of {stats.totalStations} stations across Terengganu
          </p>
        </div>

          {/* KPI Cards - Always visible or only on overview? Let's keep them on Overview */}
          {activeTab === 'overview' && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <StatsCard
                title="Total Stations"
                value={stats.totalStations}
                subtitle="Across Terengganu"
                icon={MapPin}
                trend={{ value: "100% Active", isPositive: true }}
              />
              <StatsCard
                title="Mean Overestimation"
                value={`${stats.meanOE}x`}
                subtitle="At 95th percentile"
                icon={AlertTriangle}
                trend={{ value: "+329% vs Daily", isPositive: false }}
              />
              <StatsCard
                title="Best Annual Dist."
                value={`KAP ${stats.kapPercentAnnual}%`}
                subtitle="Kappa Distribution"
                icon={BarChart3}
                trend={{ value: "Most robust fit", isPositive: true }}
              />
              <StatsCard
                title="Best Daily Dist."
                value="KAP 100%"
                subtitle="All Stations"
                icon={Activity}
                trend={{ value: "Consistent fit", isPositive: true }}
              />
            </div>
          )}

          {/* Main Content Area */}
          <div className="space-y-6">
            
            {/* Overview Tab */}
            {activeTab === 'overview' && (
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <Card className="shadow-sm">
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <div className="space-y-1">
                        <CardTitle className="flex items-center gap-2">
                          <Droplets className="h-5 w-5 text-primary" />
                          L-Moment Ratio Diagram
                        </CardTitle>
                        <CardDescription>
                          L-skewness vs L-kurtosis space
                        </CardDescription>
                      </div>
                      <button 
                        onClick={() => setActiveTab('lmoments')}
                        className="text-sm font-medium text-primary hover:underline flex items-center gap-1"
                      >
                        View Details <ArrowRight className="h-4 w-4" />
                      </button>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <LMomentsChart 
                      annualData={data.annual.parameters}
                      dailyData={data.daily.parameters}
                    />
                  </CardContent>
                </Card>

                <Card className="shadow-sm">
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <div className="space-y-1">
                        <CardTitle className="flex items-center gap-2">
                          <BarChart3 className="h-5 w-5 text-primary" />
                          Distribution Summary
                        </CardTitle>
                        <CardDescription>
                          Best fitting distributions (MADI)
                        </CardDescription>
                      </div>
                      <button 
                        onClick={() => setActiveTab('distributions')}
                        className="text-sm font-medium text-primary hover:underline flex items-center gap-1"
                      >
                        View Details <ArrowRight className="h-4 w-4" />
                      </button>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="grid grid-cols-2 gap-4">
                      <DistributionPieChart data={data.annual.gof} title="Annual Maximum" />
                      <DistributionPieChart data={data.daily.gof} title="Daily Rainfall" />
                    </div>
                  </CardContent>
                </Card>

                <Card className="lg:col-span-2 shadow-sm">
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <div className="space-y-1">
                        <CardTitle className="flex items-center gap-2">
                          <Gauge className="h-5 w-5 text-primary" />
                          Overestimation Analysis
                        </CardTitle>
                        <CardDescription>
                          Bias in Annual Maxima approach (95th percentile)
                        </CardDescription>
                      </div>
                      <button 
                        onClick={() => setActiveTab('overestimation')}
                        className="text-sm font-medium text-primary hover:underline flex items-center gap-1"
                      >
                        View Details <ArrowRight className="h-4 w-4" />
                      </button>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <OverestimationChart 
                      data={data.overestimation}
                      percentile={95}
                    />
                  </CardContent>
                </Card>
              </div>
            )}

            {/* L-Moments Tab */}
            {activeTab === 'lmoments' && (
              <div className="space-y-6 animate-in fade-in-50 duration-500">
                <FilterPanel
                  stations={data.stations}
                  selectedStation={selectedStation}
                  onStationChange={setSelectedStation}
                  selectedDataType={selectedDataType}
                  onDataTypeChange={setSelectedDataType}
                  selectedDistrict={selectedDistrict}
                  onDistrictChange={setSelectedDistrict}
                  showDistrict
                />
                
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  <Card>
                    <CardHeader>
                      <CardTitle>L-Moment Ratio Diagram</CardTitle>
                      <CardDescription>Visualizing distributional properties</CardDescription>
                    </CardHeader>
                    <CardContent>
                      <LMomentsChart 
                        annualData={data.annual.parameters.filter(p => 
                          (selectedStation === 'all' || p.stationId === selectedStation) &&
                          filteredStationIds.has(p.stationId)
                        )}
                        dailyData={data.daily.parameters.filter(p => 
                          (selectedStation === 'all' || p.stationId === selectedStation) &&
                          filteredStationIds.has(p.stationId)
                        )}
                        selectedStation={selectedStation}
                      />
                    </CardContent>
                  </Card>

                  <Card>
                    <CardHeader>
                      <CardTitle>Statistics Table</CardTitle>
                      <CardDescription>Detailed L-moment values</CardDescription>
                    </CardHeader>
                    <CardContent>
                      <DataTable
                        data={(selectedDataType === 'annual' || selectedDataType === 'both' 
                          ? data.annual.parameters : data.daily.parameters
                        ).filter(p => 
                          (selectedStation === 'all' || p.stationId === selectedStation) &&
                          filteredStationIds.has(p.stationId)
                        )}
                        columns={[
                          { key: 'stationName', header: 'Station', sortable: true },
                          { key: 'l1Mean', header: 'L₁', sortable: true, render: (item: ParameterRecord) => item.l1Mean.toFixed(2) },
                          { key: 'l2Scale', header: 'L₂', sortable: true, render: (item: ParameterRecord) => item.l2Scale.toFixed(2) },
                          { key: 't3LSkewness', header: 'τ₃', sortable: true, render: (item: ParameterRecord) => item.t3LSkewness.toFixed(4) },
                          { key: 't4LKurtosis', header: 'τ₄', sortable: true, render: (item: ParameterRecord) => item.t4LKurtosis.toFixed(4) },
                        ]}
                        pageSize={8}
                      />
                    </CardContent>
                  </Card>
                </div>
              </div>
            )}

            {/* Distributions Tab */}
            {activeTab === 'distributions' && (
              <div className="space-y-6 animate-in fade-in-50 duration-500">
                <FilterPanel
                  stations={data.stations}
                  selectedStation={selectedStation}
                  onStationChange={setSelectedStation}
                  selectedDataType={selectedDataType}
                  onDataTypeChange={setSelectedDataType}
                />
                
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  {selectedStation !== 'all' && (
                    <>
                      <Card>
                        <CardHeader>
                          <CardTitle>Annual Maxima Fits</CardTitle>
                          <CardDescription>MADI scores (Lower is better)</CardDescription>
                        </CardHeader>
                        <CardContent>
                          <MADIBarChart 
                            data={data.annual.gof}
                            selectedStation={selectedStation}
                          />
                        </CardContent>
                      </Card>
                      <Card>
                        <CardHeader>
                          <CardTitle>Daily Rainfall Fits</CardTitle>
                          <CardDescription>MADI scores (Lower is better)</CardDescription>
                        </CardHeader>
                        <CardContent>
                          <MADIBarChart 
                            data={data.daily.gof}
                            selectedStation={selectedStation}
                          />
                        </CardContent>
                      </Card>
                    </>
                  )}
                  
                  <Card className={selectedStation === 'all' ? 'lg:col-span-2' : 'lg:col-span-2'}>
                    <CardHeader>
                      <CardTitle>Goodness-of-Fit Results</CardTitle>
                      <CardDescription>Best distribution selection for each station</CardDescription>
                    </CardHeader>
                    <CardContent>
                      <DataTable
                        data={data.annual.gof.filter(g => 
                          g.bestMadi && 
                          (selectedStation === 'all' || g.stationId === selectedStation)
                        )}
                        columns={[
                          { key: 'stationName', header: 'Station', sortable: true },
                          { key: 'distribution', header: 'Best Distribution', sortable: true },
                          { key: 'madi', header: 'MADI', sortable: true, render: (item: GofRecord) => item.madi?.toFixed(4) || '-' },
                          { key: 'msdi', header: 'MSDI', sortable: true, render: (item: GofRecord) => item.msdi?.toFixed(4) || '-' },
                        ]}
                        pageSize={10}
                      />
                    </CardContent>
                  </Card>
                </div>
              </div>
            )}

            {/* Return Period Tab */}
            {activeTab === 'returnperiod' && (
              <div className="space-y-6 animate-in fade-in-50 duration-500">
                <FilterPanel
                  stations={data.stations}
                  selectedStation={selectedStation}
                  onStationChange={setSelectedStation}
                  selectedDataType={selectedDataType}
                  onDataTypeChange={setSelectedDataType}
                />
                
                <Card>
                  <CardHeader>
                    <CardTitle>Return Period Curves</CardTitle>
                    <CardDescription>Estimated rainfall depth vs Return period (Years)</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ReturnPeriodChart 
                      data={selectedDataType === 'daily' ? data.daily.returnPeriods : data.annual.returnPeriods}
                      selectedStations={selectedStation === 'all' ? [] : [selectedStation]}
                      dataType={selectedDataType === 'daily' ? 'daily' : 'annual'}
                    />
                  </CardContent>
                </Card>
                
                <Card>
                  <CardHeader>
                    <CardTitle>Return Value Data</CardTitle>
                    <CardDescription>Tabulated quantile estimates</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <DataTable
                      data={(selectedDataType === 'daily' ? data.daily.returnPeriods : data.annual.returnPeriods)
                        .filter(r => selectedStation === 'all' || r.stationId === selectedStation)}
                      columns={[
                        { key: 'stationName', header: 'Station', sortable: true },
                        { key: 'bestDistribution', header: 'Distribution', sortable: true },
                        { key: 'returnPeriod', header: 'Return Period (yr)', sortable: true },
                        { key: 'returnValue', header: 'Return Value (mm)', sortable: true, 
                          render: (item) => (item.returnValue as number).toFixed(2) },
                      ]}
                      pageSize={10}
                    />
                  </CardContent>
                </Card>
              </div>
            )}

            {/* Overestimation Tab */}
            {activeTab === 'overestimation' && (
              <div className="space-y-6 animate-in fade-in-50 duration-500">
                <FilterPanel
                  stations={data.stations}
                  selectedStation={selectedStation}
                  onStationChange={setSelectedStation}
                  selectedDataType={selectedDataType}
                  onDataTypeChange={setSelectedDataType}
                  selectedPercentile={selectedPercentile}
                  onPercentileChange={setSelectedPercentile}
                  showDataType={false}
                  showPercentile
                />
                
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  {(() => {
                    const oeData = data.overestimation.filter(o => 
                      o.percentile === selectedPercentile && 
                      o.oeFactor !== null &&
                      (selectedStation === 'all' || o.stationId === selectedStation)
                    )
                    const meanOE = oeData.reduce((sum, o) => sum + (o.oeFactor || 0), 0) / oeData.length
                    const minOE = Math.min(...oeData.map(o => o.oeFactor || 0))
                    const maxOE = Math.max(...oeData.map(o => o.oeFactor || 0))
                    
                    return (
                      <>
                        <Card className="bg-amber-50/50 border-amber-200">
                          <CardContent className="p-6">
                            <p className="text-sm font-medium text-amber-900">Mean OE Factor</p>
                            <p className="text-3xl font-bold text-amber-700 mt-2">{meanOE.toFixed(2)}x</p>
                            <p className="text-sm text-amber-600/80 mt-1">{((meanOE - 1) * 100).toFixed(0)}% overestimation</p>
                          </CardContent>
                        </Card>
                        <Card className="bg-emerald-50/50 border-emerald-200">
                          <CardContent className="p-6">
                            <p className="text-sm font-medium text-emerald-900">Minimum OE Factor</p>
                            <p className="text-3xl font-bold text-emerald-700 mt-2">{minOE.toFixed(2)}x</p>
                            <p className="text-sm text-emerald-600/80 mt-1">Lowest bias observed</p>
                          </CardContent>
                        </Card>
                        <Card className="bg-rose-50/50 border-rose-200">
                          <CardContent className="p-6">
                            <p className="text-sm font-medium text-rose-900">Maximum OE Factor</p>
                            <p className="text-3xl font-bold text-rose-700 mt-2">{maxOE.toFixed(2)}x</p>
                            <p className="text-sm text-rose-600/80 mt-1">Highest bias observed</p>
                          </CardContent>
                        </Card>
                      </>
                    )
                  })()}
                </div>
                
                <Card>
                  <CardHeader>
                    <CardTitle>Overestimation Factor by Station</CardTitle>
                    <CardDescription>Comparing bias magnitude across locations</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <OverestimationChart 
                      data={data.overestimation}
                      percentile={selectedPercentile}
                      selectedStation={selectedStation}
                    />
                  </CardContent>
                </Card>
                
                <Card>
                  <CardHeader>
                    <CardTitle>Detailed Comparison Table</CardTitle>
                    <CardDescription>Return periods and calculated factors</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <DataTable
                      data={data.overestimation.filter(o => 
                        o.percentile === selectedPercentile &&
                        (selectedStation === 'all' || o.stationId === selectedStation)
                      )}
                      columns={[
                        { key: 'stationName', header: 'Station', sortable: true },
                        { key: 'magnitude', header: 'Magnitude (mm)', sortable: true, 
                          render: (item: OverestimationRecord) => item.magnitude.toFixed(1) },
                        { key: 'rpAnnualYears', header: 'RP AM (yr)', sortable: true,
                          render: (item: OverestimationRecord) => item.rpAnnualYears.toFixed(2) },
                        { key: 'rpDailyYears', header: 'RP Daily (yr)', sortable: true,
                          render: (item: OverestimationRecord) => item.rpDailyYears.toFixed(2) },
                        { key: 'oeFactor', header: 'OE Factor', sortable: true,
                          render: (item: OverestimationRecord) => item.oeFactor ? 
                            <span className={cn(
                              "font-medium",
                              (item.oeFactor > 4) ? "text-red-600" :
                              (item.oeFactor > 2) ? "text-amber-600" : "text-green-600"
                            )}>{item.oeFactor.toFixed(2)}x</span> : '-' },
                      ]}
                      pageSize={10}
                    />
                  </CardContent>
                </Card>
              </div>
            )}

            {/* Data Tables Tab */}
            {activeTab === 'data' && (
              <div className="space-y-6 animate-in fade-in-50 duration-500">
                <FilterPanel
                  stations={data.stations}
                  selectedStation={selectedStation}
                  onStationChange={setSelectedStation}
                  selectedDataType={selectedDataType}
                  onDataTypeChange={setSelectedDataType}
                  selectedDistrict={selectedDistrict}
                  onDistrictChange={setSelectedDistrict}
                  showDistrict
                />
                
                <Card>
                  <CardContent className="p-0">
                    <DataTable
                      data={filteredStations}
                      columns={[
                        { key: 'id', header: 'Station ID', sortable: true },
                        { key: 'name', header: 'Station Name', sortable: true },
                        { key: 'district', header: 'District', sortable: true },
                        { key: 'lat', header: 'Latitude', sortable: true },
                        { key: 'lng', header: 'Longitude', sortable: true },
                      ]}
                      pageSize={15}
                    />
                  </CardContent>
                </Card>
              </div>
            )}
            
          </div>
        </div>
      </main>
    </div>
  )
}
