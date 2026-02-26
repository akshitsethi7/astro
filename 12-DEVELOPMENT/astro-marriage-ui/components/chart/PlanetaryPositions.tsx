'use client';

import { getPlanetColor } from '@/lib/calculations/planets';
import styles from './PlanetaryPositions.module.scss';

interface PlanetaryPositionsProps {
  planets: any[];
  selectedPlanet: string | null;
  onPlanetSelect: (planet: string | null) => void;
}

export default function PlanetaryPositions({ 
  planets, 
  selectedPlanet,
  onPlanetSelect 
}: PlanetaryPositionsProps) {
  const getDignityColor = (dignity: string) => {
    switch (dignity) {
      case 'exalted': return '#22c55e';
      case 'own': return '#10b981';
      case 'friend': return '#3b82f6';
      case 'neutral': return '#8b5cf6';
      case 'enemy': return '#f59e0b';
      case 'debilitated': return '#ef4444';
      default: return '#8b5cf6';
    }
  };

  return (
    <div className={styles.positions}>
      <div className={styles.table}>
        <div className={styles.tableHeader}>
          <div className={styles.headerCell}>Planet</div>
          <div className={styles.headerCell}>Sign</div>
          <div className={styles.headerCell}>Degree</div>
          <div className={styles.headerCell}>House</div>
          <div className={styles.headerCell}>Nakshatra</div>
          <div className={styles.headerCell}>Dignity</div>
          <div className={styles.headerCell}>Status</div>
        </div>
        
        <div className={styles.tableBody}>
          {planets.map((planet) => (
            <div 
              key={planet.planet}
              className={`${styles.tableRow} ${selectedPlanet === planet.planet ? styles.selected : ''}`}
              onClick={() => onPlanetSelect(planet.planet)}
            >
              <div className={styles.cell}>
                <div className={styles.planetName}>
                  <div 
                    className={styles.planetDot}
                    style={{ background: getPlanetColor(planet.planet) }}
                  />
                  {planet.planet}
                </div>
              </div>
              <div className={styles.cell}>{planet.sign}</div>
              <div className={styles.cell}>
                <span className={styles.mono}>{planet.degree.toFixed(2)}°</span>
              </div>
              <div className={styles.cell}>
                <span className={styles.mono}>{planet.house}</span>
              </div>
              <div className={styles.cell}>{planet.nakshatra}</div>
              <div className={styles.cell}>
                <span 
                  className={styles.dignityBadge}
                  style={{ 
                    background: `${getDignityColor(planet.dignity)}20`,
                    color: getDignityColor(planet.dignity),
                    borderColor: getDignityColor(planet.dignity)
                  }}
                >
                  {planet.dignity}
                </span>
              </div>
              <div className={styles.cell}>
                {planet.retrograde && (
                  <span className={styles.retrograde}>Retrograde</span>
                )}
                {!planet.retrograde && (
                  <span className={styles.direct}>Direct</span>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
