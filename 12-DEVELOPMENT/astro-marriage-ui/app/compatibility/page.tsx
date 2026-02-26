'use client'

import BirthChartForm from '@/components/BirthChartForm'
import styles from './page.module.scss'

export default function CompatibilityPage() {
  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1>Compatibility Analysis</h1>
        <p>Ashtakoot matching for marriage compatibility</p>
        <p style={{ marginTop: '1rem', color: 'rgba(255,255,255,0.6)', fontSize: '0.9rem' }}>
          This feature is under development. It will support comparing two birth charts for compatibility analysis using the Ashtakoot system.
        </p>
      </div>

      <div className={styles.formSection}>
        <div className={styles.formGrid}>
          <div className={styles.personSection}>
            <h3>Person 1</h3>
            <BirthChartForm />
          </div>
          
          <div className={styles.personSection}>
            <h3>Person 2</h3>
            <p style={{ color: 'rgba(255,255,255,0.5)' }}>Second person&apos;s chart input coming soon...</p>
          </div>
        </div>
      </div>
    </div>
  )
}
