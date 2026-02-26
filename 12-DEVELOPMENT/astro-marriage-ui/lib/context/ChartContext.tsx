'use client';

import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { calculateChart } from '@/lib/calculations/planets';
import { calculatePlanetaryPositions } from '@/lib/calculations/ephemeris';
import { DashaService } from '@/lib/services/DashaService';
import { ShadowService } from '@/lib/services/ShadowService';
import type { ChartData } from '@/lib/types/astrology';

interface BirthDetails {
  date: string;
  time: string;
  latitude: number;
  longitude: number;
  timezone: string;
  name?: string;
}

interface ChartContextType {
  birthDetails: BirthDetails | null;
  chartData: ChartData | null;
  dashaService: DashaService | null;
  shadowService: ShadowService | null;
  isLoading: boolean;
  error: string | null;
  setBirthDetails: (details: BirthDetails) => void;
  clearChart: () => void;
}

const ChartContext = createContext<ChartContextType | undefined>(undefined);

// Default birth details (example chart)
const DEFAULT_BIRTH_DETAILS: BirthDetails = {
  date: '1995-01-01',
  time: '10:30',
  latitude: 28.6139,
  longitude: 77.2090,
  timezone: 'Asia/Kolkata',
  name: 'Sample Chart',
};

export function ChartProvider({ children }: { children: ReactNode }) {
  const [birthDetails, setBirthDetailsState] = useState<BirthDetails | null>(null);
  const [chartData, setChartData] = useState<ChartData | null>(null);
  const [dashaService, setDashaService] = useState<DashaService | null>(null);
  const [shadowService, setShadowService] = useState<ShadowService | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Load from localStorage on mount
  useEffect(() => {
    const saved = localStorage.getItem('birthDetails');
    if (saved) {
      try {
        const details = JSON.parse(saved);
        setBirthDetailsState(details);
      } catch (e) {
        // Use default if parsing fails
        setBirthDetailsState(DEFAULT_BIRTH_DETAILS);
      }
    } else {
      // Use default chart
      setBirthDetailsState(DEFAULT_BIRTH_DETAILS);
    }
  }, []);

  // Calculate chart when birth details change
  useEffect(() => {
    if (!birthDetails) return;

    setIsLoading(true);
    setError(null);

    try {
      // Parse date and time
      const birthDate = new Date(birthDetails.date + 'T' + birthDetails.time);
      
      // Calculate chart
      const chart = calculateChart(
        birthDate,
        birthDetails.time,
        birthDetails.timezone,
        birthDetails.latitude,
        birthDetails.longitude,
        'Lahiri'
      );

      setChartData(chart);

      // Initialize services
      const dasha = new DashaService(chart);
      const shadow = new ShadowService(chart);

      setDashaService(dasha);
      setShadowService(shadow);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to calculate chart');
      console.error('Chart calculation error:', err);
    } finally {
      setIsLoading(false);
    }
  }, [birthDetails]);

  const setBirthDetails = (details: BirthDetails) => {
    setBirthDetailsState(details);
    // Save to localStorage
    localStorage.setItem('birthDetails', JSON.stringify(details));
  };

  const clearChart = () => {
    setBirthDetailsState(null);
    setChartData(null);
    setDashaService(null);
    setShadowService(null);
    localStorage.removeItem('birthDetails');
  };

  return (
    <ChartContext.Provider
      value={{
        birthDetails,
        chartData,
        dashaService,
        shadowService,
        isLoading,
        error,
        setBirthDetails,
        clearChart,
      }}
    >
      {children}
    </ChartContext.Provider>
  );
}

export function useChart() {
  const context = useContext(ChartContext);
  if (context === undefined) {
    throw new Error('useChart must be used within a ChartProvider');
  }
  return context;
}
