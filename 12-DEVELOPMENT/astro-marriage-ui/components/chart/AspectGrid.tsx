'use client';

import styles from './AspectGrid.module.scss';

interface AspectGridProps {
  aspects: any[];
}

export default function AspectGrid({ aspects }: AspectGridProps) {
  const getAspectColor = (type: string) => {
    switch (type) {
      case 'conjunction': return '#8b5cf6';
      case 'trine': return '#22c55e';
      case 'sextile': return '#3b82f6';
      case 'square': return '#ef4444';
      case 'opposition': return '#f59e0b';
      default: return '#8b5cf6';
    }
  };

  const getAspectIcon = (type: string) => {
    switch (type) {
      case 'conjunction': return '☌';
      case 'trine': return '△';
      case 'sextile': return '⚹';
      case 'square': return '□';
      case 'opposition': return '☍';
      default: return '○';
    }
  };

  return (
    <div className={styles.aspectGrid}>
      {aspects.length === 0 ? (
        <div className={styles.noAspects}>
          No major aspects detected
        </div>
      ) : (
        <div className={styles.aspectsList}>
          {aspects.map((aspect, index) => (
            <div key={index} className={styles.aspectCard}>
              <div className={styles.aspectHeader}>
                <div 
                  className={styles.aspectIcon}
                  style={{ color: getAspectColor(aspect.type) }}
                >
                  {getAspectIcon(aspect.type)}
                </div>
                <div className={styles.aspectType} style={{ color: getAspectColor(aspect.type) }}>
                  {aspect.type}
                </div>
              </div>
              
              <div className={styles.aspectPlanets}>
                <span className={styles.planet}>{aspect.planet1}</span>
                <span className={styles.separator}>—</span>
                <span className={styles.planet}>{aspect.planet2}</span>
              </div>
              
              <div className={styles.aspectDetails}>
                <div className={styles.detailItem}>
                  <span className={styles.detailLabel}>Angle</span>
                  <span className={styles.detailValue}>{aspect.angle.toFixed(1)}°</span>
                </div>
                <div className={styles.detailItem}>
                  <span className={styles.detailLabel}>Orb</span>
                  <span className={styles.detailValue}>{aspect.orb.toFixed(1)}°</span>
                </div>
              </div>
              
              <div className={styles.strengthBar}>
                <div className={styles.strengthLabel}>Strength</div>
                <div className={styles.bar}>
                  <div 
                    className={styles.barFill}
                    style={{ 
                      width: `${aspect.strength}%`,
                      background: getAspectColor(aspect.type)
                    }}
                  />
                </div>
                <div className={styles.strengthValue}>{aspect.strength}%</div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
