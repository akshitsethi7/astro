'use client';

import { useState } from 'react';
import Link from 'next/link';
import { Star, ArrowLeft, Circle, TrendingUp, Zap } from 'lucide-react';
import BirthChartVisualization from '@/components/chart/BirthChartVisualization';
import PlanetaryPositions from '@/components/chart/PlanetaryPositions';
import AspectGrid from '@/components/chart/AspectGrid';
import { sampleChartData } from '@/lib/data/sampleChartData';
import styles from './page.module.scss';

export default function ChartPage() {
  const [selectedPlanet, setSelectedPlanet] = useState<string | null>(null);

  // Use accurate chart data from chartsimp
  const chartData = {
    ascendant: {
      sign: sampleChartData.ascendant.sign,
      degree: sampleChartData.ascendant.degree,
    },
    planets: sampleChartData.planets.map(p => ({
      planet: p.planet,
      sign: p.sign,
      degree: p.degree,
      house: p.house,
      nakshatra: p.nakshatra,
      retrograde: p.retrograde,
      dignity: p.dignity || 'neutral',
      combust: p.combust,
      avastha: p.avastha,
    })),
    aspects: [
      // Calculate aspects based on planetary positions
      { planet1: 'Venus', planet2: 'Rahu', type: 'conjunction', angle: 7.15, orb: 7.15, strength: 75 },
      { planet1: 'Sun', planet2: 'Mercury', type: 'conjunction', angle: 7.19, orb: 7.19, strength: 80 },
      { planet1: 'Mars', planet2: 'Saturn', type: 'opposition', angle: 174.78, orb: 5.22, strength: 70 },
    ],
    houses: sampleChartData.houses,
  };

  return (
    <div className={styles.chartPage}>
      {/* Header */}
      <header className={styles.header}>
        <Link href="/" className={styles.backBtn}>
          <ArrowLeft size={20} />
          Back to Home
        </Link>
        
        <div className={styles.headerContent}>
          <div className={styles.titleSection}>
            <h1 className={styles.title}>
              <Star size={36} />
              Birth Chart Analysis
            </h1>
            <p className={styles.subtitle}>
              Complete natal chart with planetary positions, houses, and aspects
            </p>
          </div>
          
          <div className={styles.chartInfo}>
            <div className={styles.infoItem}>
              <span className={styles.infoLabel}>Ascendant</span>
              <span className={styles.infoValue}>
                {chartData.ascendant.sign} {chartData.ascendant.degree.toFixed(2)}°
              </span>
            </div>
            <div className={styles.infoItem}>
              <span className={styles.infoLabel}>Nakshatra</span>
              <span className={styles.infoValue}>{sampleChartData.ascendant.nakshatra}</span>
            </div>
            <div className={styles.infoItem}>
              <span className={styles.infoLabel}>Ayanamsa</span>
              <span className={styles.infoValue}>Lahiri</span>
            </div>
            <div className={styles.infoItem}>
              <span className={styles.infoLabel}>Birth Date</span>
              <span className={styles.infoValue}>
                {sampleChartData.birthDate.toLocaleDateString()}
              </span>
            </div>
          </div>
        </div>
      </header>

      {/* Chart Visualization */}
      <section className={styles.chartSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>
            <Circle size={24} />
            Birth Chart (D1 - Rashi)
          </h2>
        </div>
        
        <div className={styles.chartContainer}>
          <BirthChartVisualization 
            chartData={chartData}
            selectedPlanet={selectedPlanet}
            onPlanetSelect={setSelectedPlanet}
          />
        </div>
      </section>

      {/* Planetary Positions */}
      <section className={styles.positionsSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>
            <TrendingUp size={24} />
            Planetary Positions
          </h2>
        </div>
        
        <PlanetaryPositions 
          planets={chartData.planets}
          onPlanetSelect={setSelectedPlanet}
          selectedPlanet={selectedPlanet}
        />
      </section>

      {/* Aspect Grid */}
      <section className={styles.aspectsSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>
            <Zap size={24} />
            Planetary Aspects
          </h2>
        </div>
        
        <AspectGrid aspects={chartData.aspects} />
      </section>

      {/* House Analysis */}
      <section className={styles.housesSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>House Analysis</h2>
        </div>
        
        <div className={styles.housesGrid}>
          {chartData.houses.map((house) => (
            <div key={house.number} className={styles.houseCard}>
              <div className={styles.houseHeader}>
                <span className={styles.houseNumber}>{house.number}</span>
                <span className={styles.houseSign}>{house.sign}</span>
              </div>
              <div className={styles.houseLord}>Lord: {house.lord}</div>
              {house.planets.length > 0 && (
                <div className={styles.housePlanets}>
                  {house.planets.map((planet) => (
                    <span key={planet} className={styles.housePlanet}>{planet}</span>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>
      </section>

      {/* Yogas Section */}
      <section className={styles.yogasSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>
            <Star size={24} />
            Yogas Present in Chart
          </h2>
        </div>
        
        <div className={styles.yogasGrid}>
          {/* Major Yogas */}
          <div className={styles.yogaCategory}>
            <h3>Major Yogas</h3>
            {sampleChartData.yogas.major.filter(y => y.present).map((yoga, idx) => (
              <div key={idx} className={styles.yogaCard}>
                <h4>{yoga.name}</h4>
                <p>{yoga.description}</p>
              </div>
            ))}
          </div>

          {/* Chandra Yogas */}
          <div className={styles.yogaCategory}>
            <h3>Chandra Yogas</h3>
            {sampleChartData.yogas.chandra.filter(y => y.present).map((yoga, idx) => (
              <div key={idx} className={styles.yogaCard}>
                <h4>{yoga.name}</h4>
                <p>{yoga.description}</p>
              </div>
            ))}
          </div>

          {/* Soorya Yogas */}
          <div className={styles.yogaCategory}>
            <h3>Soorya Yogas</h3>
            {sampleChartData.yogas.soorya.filter(y => y.present).map((yoga, idx) => (
              <div key={idx} className={styles.yogaCard}>
                <h4>{yoga.name}</h4>
                <p>{yoga.description}</p>
              </div>
            ))}
          </div>

          {/* Inauspicious Yogas */}
          {sampleChartData.yogas.inauspicious.filter(y => y.present).length > 0 && (
            <div className={styles.yogaCategory}>
              <h3>Inauspicious Yogas & Remedies</h3>
              {sampleChartData.yogas.inauspicious.filter(y => y.present).map((yoga, idx) => (
                <div key={idx} className={`${styles.yogaCard} ${styles.inauspicious}`}>
                  <h4>{yoga.name}</h4>
                  <p>{yoga.description}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
