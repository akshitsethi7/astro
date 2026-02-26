'use client'

import styles from './PlanetaryTable.module.scss'

interface PlanetData {
  planet: string
  sign: string
  degree: string
  house: number
  nakshatra: string
  lord: string
  dignity: string
  color: string
}

const planetaryData: PlanetData[] = [
  { planet: 'Lagna', sign: 'Leo', degree: '23°03\'', house: 1, nakshatra: 'P.Phalguni', lord: 'Venus', dignity: '-', color: '#FFD60A' },
  { planet: 'Sun', sign: 'Sagittarius', degree: '10°55\'', house: 5, nakshatra: 'Mula', lord: 'Ketu', dignity: 'Neutral', color: '#FF6B35' },
  { planet: 'Moon', sign: 'Virgo', degree: '22°44\'', house: 2, nakshatra: 'Chitra', lord: 'Mars', dignity: 'Neutral', color: '#F7F7F7' },
  { planet: 'Mars', sign: 'Leo', degree: '8°33\'', house: 1, nakshatra: 'Magha', lord: 'Ketu', dignity: 'Neutral', color: '#E63946' },
  { planet: 'Mercury', sign: 'Sagittarius', degree: '18°06\'', house: 5, nakshatra: 'P.Ashadha', lord: 'Venus', dignity: 'Neutral', color: '#06FFA5' },
  { planet: 'Jupiter', sign: 'Scorpio', degree: '9°52\'', house: 4, nakshatra: 'Anuradha', lord: 'Saturn', dignity: 'Neutral', color: '#FFD60A' },
  { planet: 'Venus', sign: 'Libra', degree: '25°24\'', house: 3, nakshatra: 'Vishakha', lord: 'Jupiter', dignity: 'Own Sign ✓', color: '#F72585' },
  { planet: 'Saturn', sign: 'Aquarius', degree: '13°46\'', house: 7, nakshatra: 'Shatabhisha', lord: 'Rahu', dignity: 'Own Sign ✓', color: '#4361EE' },
  { planet: 'Rahu', sign: 'Libra', degree: '18°15\'', house: 3, nakshatra: 'Swati', lord: 'Rahu', dignity: 'Retrograde', color: '#8338EC' },
  { planet: 'Ketu', sign: 'Aries', degree: '18°15\'', house: 9, nakshatra: 'Bharani', lord: 'Venus', dignity: 'Retrograde', color: '#FB5607' },
]

export function PlanetaryTable() {
  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h3 className={styles.title}>Planetary Positions</h3>
        <span className={styles.subtitle}>D1 - Rashi Chart</span>
      </div>
      
      <div className={styles.tableWrapper}>
        <table className={styles.table}>
          <thead>
            <tr>
              <th>Planet</th>
              <th>Sign</th>
              <th>Degree</th>
              <th>House</th>
              <th>Nakshatra</th>
              <th>Lord</th>
              <th>Dignity</th>
            </tr>
          </thead>
          <tbody>
            {planetaryData.map((data, index) => (
              <tr key={index} className={styles.row}>
                <td>
                  <div className={styles.planetCell}>
                    <div 
                      className={styles.planetDot}
                      style={{ backgroundColor: data.color }}
                    />
                    <span className={styles.planetName}>{data.planet}</span>
                  </div>
                </td>
                <td>{data.sign}</td>
                <td className={styles.mono}>{data.degree}</td>
                <td className={styles.center}>{data.house}</td>
                <td>{data.nakshatra}</td>
                <td>{data.lord}</td>
                <td>
                  <span className={
                    data.dignity.includes('Own Sign') ? styles.dignityGood :
                    data.dignity.includes('Retrograde') ? styles.dignityWarning :
                    styles.dignityNeutral
                  }>
                    {data.dignity}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
