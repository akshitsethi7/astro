'use client';

import styles from './TransitChart.module.scss';

export default function TransitChart({ transits, selectedDate }: any) {
  return (
    <div className={styles.transitChart}>
      <div className={styles.placeholder}>
        <div className={styles.icon}>🌍</div>
        <h3>Transit Chart Visualization</h3>
        <p>Dual-circle chart showing natal (inner) and transit (outer) positions</p>
        <div className={styles.date}>
          {selectedDate.toLocaleDateString('en-US', { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
          })}
        </div>
      </div>
    </div>
  );
}
