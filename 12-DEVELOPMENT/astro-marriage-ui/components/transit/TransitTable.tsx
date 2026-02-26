'use client';

import { getPlanetColor } from '@/lib/calculations/planets';
import styles from './TransitTable.module.scss';

export default function TransitTable({ transits }: any) {
  return (
    <div className={styles.table}>
      {transits.map((transit: any) => (
        <div key={transit.planet} className={styles.row}>
          <div className={styles.planet}>
            <div className={styles.dot} style={{ background: getPlanetColor(transit.planet) }} />
            {transit.planet}
          </div>
          <div className={styles.sign}>{transit.sign}</div>
          <div className={styles.degree}>{transit.degree.toFixed(2)}°</div>
          <div className={styles.house}>House {transit.house}</div>
          <div className={styles.speed}>
            {transit.speed > 0 ? '+' : ''}{transit.speed.toFixed(2)}°/day
          </div>
        </div>
      ))}
    </div>
  );
}
