export interface Station {
  id: string;
  name: string;
  district: string;
  lat: number;
  lng: number;
}

export interface ParameterRecord {
  stationId: string;
  stationName: string;
  nObservations: number;
  l1Mean: number;
  l2Scale: number;
  t3LSkewness: number;
  t4LKurtosis: number;
}

export interface GofRecord {
  stationId: string;
  stationName: string;
  distribution: string;
  madi: number | null;
  msdi: number | null;
  bestMadi: boolean;
  bestMsdi: boolean;
}

export interface ReturnPeriodRecord {
  stationId: string;
  stationName: string;
  bestDistribution: string;
  returnPeriod: number;
  returnValue: number;
}

export interface OverestimationRecord {
  stationId: string;
  stationName: string;
  magnitude: number;
  percentile: number;
  bestAnnualDist: string;
  bestDailyDist: string;
  rpAnnualYears: number;
  rpDailyDays: number;
  rpDailyYears: number;
  oeFactor: number | null;
  oePercentage: number | null;
}

export interface AnalysisData {
  stations: Station[];
  annual: {
    parameters: ParameterRecord[];
    gof: GofRecord[];
    returnPeriods: ReturnPeriodRecord[];
  };
  daily: {
    parameters: ParameterRecord[];
    gof: GofRecord[];
    returnPeriods: ReturnPeriodRecord[];
  };
  overestimation: OverestimationRecord[];
}

