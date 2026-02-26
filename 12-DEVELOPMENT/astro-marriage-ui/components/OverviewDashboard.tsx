'use client'

import { Heart, Calendar, User, Star, TrendingUp, Award } from 'lucide-react'
import { InfoCard } from './InfoCard'
import { BirthChart } from './BirthChart'
import { PlanetaryTable } from './PlanetaryTable'
import { DashaTimeline } from './DashaTimeline'
import { TimelineChart } from './TimelineChart'
import styles from './OverviewDashboard.module.scss'

export function OverviewDashboard() {
  return (
    <div className={styles.dashboard}>
      {/* Quick Stats Grid */}
      <div className={styles.statsGrid}>
        <InfoCard
          title="Marriage Prospects"
          value="⭐⭐⭐⭐⭐"
          subtitle="Exceptional indicators"
          icon={Star}
          gradient="var(--gradient-success)"
          trend="up"
          trendValue="90%"
        />
        <InfoCard
          title="Most Likely Period"
          value="2028-2030"
          subtitle="Age 33-36 years"
          icon={Calendar}
          gradient="var(--gradient-primary)"
        />
        <InfoCard
          title="Spouse Loyalty"
          value="9/10"
          subtitle="Very high commitment"
          icon={Heart}
          gradient="var(--gradient-accent)"
          trend="up"
          trendValue="Excellent"
        />
        <InfoCard
          title="Overall Confidence"
          value="85-90%"
          subtitle="Strong predictions"
          icon={Award}
          gradient="var(--gradient-secondary)"
        />
      </div>

      {/* Main Content Grid */}
      <div className={styles.contentGrid}>
        {/* Birth Chart */}
        <div className={styles.chartSection}>
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>Birth Chart Visualization</h2>
            <span className={styles.sectionBadge}>D1 - Rashi</span>
          </div>
          <BirthChart />
        </div>

        {/* Key Highlights */}
        <div className={styles.highlightsSection}>
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>Key Highlights</h2>
          </div>
          <div className={styles.highlights}>
            <div className={styles.highlight}>
              <div className={styles.highlightIcon} style={{ background: 'var(--gradient-success)' }}>
                ✓
              </div>
              <div className={styles.highlightContent}>
                <h4 className={styles.highlightTitle}>Venus Double Own Sign</h4>
                <p className={styles.highlightText}>
                  Venus in Libra (D1) and Taurus (D9) - Extremely rare and powerful for marriage
                </p>
              </div>
            </div>

            <div className={styles.highlight}>
              <div className={styles.highlightIcon} style={{ background: 'var(--gradient-primary)' }}>
                ✓
              </div>
              <div className={styles.highlightContent}>
                <h4 className={styles.highlightTitle}>Saturn in 7th House</h4>
                <p className={styles.highlightText}>
                  Saturn in own sign Aquarius ensures stable, long-lasting marriage
                </p>
              </div>
            </div>

            <div className={styles.highlight}>
              <div className={styles.highlightIcon} style={{ background: 'var(--gradient-accent)' }}>
                ✓
              </div>
              <div className={styles.highlightContent}>
                <h4 className={styles.highlightTitle}>Moon in Own Sign (Navamsa)</h4>
                <p className={styles.highlightText}>
                  Emotional fulfillment and strong compatibility with spouse
                </p>
              </div>
            </div>

            <div className={styles.highlight}>
              <div className={styles.highlightIcon} style={{ background: 'var(--gradient-secondary)' }}>
                ⚠
              </div>
              <div className={styles.highlightContent}>
                <h4 className={styles.highlightTitle}>Delayed but Quality Marriage</h4>
                <p className={styles.highlightText}>
                  Saturn&apos;s influence delays marriage but ensures the right person at right time
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Planetary Positions */}
      <div className={styles.fullWidth}>
        <PlanetaryTable />
      </div>

      {/* Timeline Sections */}
      <div className={styles.timelineGrid}>
        <div className={styles.timelineSection}>
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>Marriage Probability Timeline</h2>
          </div>
          <TimelineChart />
        </div>

        <div className={styles.timelineSection}>
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>Dasha Periods</h2>
          </div>
          <DashaTimeline />
        </div>
      </div>

      {/* Spouse Profile */}
      <div className={styles.profileSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>Spouse Profile</h2>
          <span className={styles.sectionBadge}>Based on 7th House Analysis</span>
        </div>
        <div className={styles.profileGrid}>
          <div className={styles.profileCard}>
            <div className={styles.profileLabel}>Age Difference</div>
            <div className={styles.profileValue}>1-2 years older</div>
          </div>
          <div className={styles.profileCard}>
            <div className={styles.profileLabel}>Appearance</div>
            <div className={styles.profileValue}>Very attractive, elegant</div>
          </div>
          <div className={styles.profileCard}>
            <div className={styles.profileLabel}>Nature</div>
            <div className={styles.profileValue}>Mature, responsible</div>
          </div>
          <div className={styles.profileCard}>
            <div className={styles.profileLabel}>Background</div>
            <div className={styles.profileValue}>Well-educated, stable</div>
          </div>
          <div className={styles.profileCard}>
            <div className={styles.profileLabel}>Career</div>
            <div className={styles.profileValue}>Professional, independent</div>
          </div>
          <div className={styles.profileCard}>
            <div className={styles.profileLabel}>Compatibility</div>
            <div className={styles.profileValue}>Excellent (9/10)</div>
          </div>
        </div>
      </div>
    </div>
  )
}
