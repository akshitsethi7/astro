'use client';

import { useState } from 'react';
import Link from 'next/link';
import { Moon, ArrowLeft, Star, TrendingUp, Sparkles, AlertCircle, BookOpen } from 'lucide-react';
import { sampleChartData } from '@/lib/data/sampleChartData';
import styles from './page.module.scss';

export default function ShadowsPage() {
  const [selectedTab, setSelectedTab] = useState<'analysis' | 'yogas' | 'remedies'>('analysis');

  // Get Rahu and Ketu data from sampleChartData
  const rahuData = sampleChartData.planets.find(p => p.planet === 'Rahu')!;
  const ketuData = sampleChartData.planets.find(p => p.planet === 'Ketu')!;
  
  const shadowData = {
    rahu: {
      sign: rahuData.sign,
      degree: rahuData.degree.toFixed(2),
      house: rahuData.house,
      nakshatra: rahuData.nakshatra,
      nakshatraLord: rahuData.nakshatraLord,
      pada: rahuData.pada,
      strength: 75, // Can be calculated from shadbala
      retrograde: rahuData.retrograde,
    },
    ketu: {
      sign: ketuData.sign,
      degree: ketuData.degree.toFixed(2),
      house: ketuData.house,
      nakshatra: ketuData.nakshatra,
      nakshatraLord: ketuData.nakshatraLord,
      pada: ketuData.pada,
      strength: 75,
      retrograde: ketuData.retrograde,
    },
    yogas: sampleChartData.yogas.major.filter(y => y.name.includes('Raja')),
    lifeImpact: [
      {
        area: 'Relationships & Partnership',
        planet: 'Rahu',
        impact: `Rahu in ${rahuData.sign} (${rahuData.house}rd house) amplifies desires in relationships. ${rahuData.nakshatra} nakshatra brings unique karmic lessons.`,
        intensity: 'high',
      },
      {
        area: 'Spirituality & Dharma',
        planet: 'Ketu',
        impact: `Ketu in ${ketuData.sign} (${ketuData.house}th house) brings detachment and spiritual wisdom. ${ketuData.nakshatra} nakshatra indicates past life mastery.`,
        intensity: 'high',
      },
    ],
  };

  return (
    <div className={styles.shadowsPage}>
      {/* Header */}
      <header className={styles.header}>
        <Link href="/" className={styles.backBtn}>
          <ArrowLeft size={20} />
          Back to Home
        </Link>
        
        <div className={styles.headerContent}>
          <div className={styles.titleSection}>
            <h1 className={styles.title}>
              <Moon size={36} />
              Shadow Planets Analysis
            </h1>
            <p className={styles.subtitle}>
              Rahu & Ketu - The karmic nodes revealing your soul&apos;s journey
            </p>
          </div>
          
          <div className={styles.opposition}>
            <div className={styles.oppositionLabel}>Opposition</div>
            <div className={styles.oppositionValue}>180.0°</div>
            <div className={styles.oppositionStatus}>
              <Star size={16} fill="#22c55e" color="#22c55e" />
              Exact (Always opposite)
            </div>
          </div>
        </div>
      </header>

      {/* Shadow Planet Cards */}
      <section className={styles.planetsSection}>
        <div className={styles.planetsGrid}>
          {/* Rahu Card */}
          <div className={styles.planetCard} style={{ borderColor: '#8338ec' }}>
            <div className={styles.planetHeader}>
              <div className={styles.planetIcon} style={{ background: 'linear-gradient(135deg, #8338ec 0%, #fb5607 100%)' }}>
                <Moon size={32} />
              </div>
              <div>
                <h2 className={styles.planetName}>Rahu</h2>
                <p className={styles.planetSubtitle}>North Node - Desires & Ambitions</p>
              </div>
            </div>

            <div className={styles.planetDetails}>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>Sign</span>
                <span className={styles.detailValue}>{shadowData.rahu.sign}</span>
              </div>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>Degree</span>
                <span className={styles.detailValue}>{shadowData.rahu.degree}°</span>
              </div>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>House</span>
                <span className={styles.detailValue}>{shadowData.rahu.house}rd</span>
              </div>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>Nakshatra</span>
                <span className={styles.detailValue}>{shadowData.rahu.nakshatra}</span>
              </div>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>Pada</span>
                <span className={styles.detailValue}>{shadowData.rahu.pada}</span>
              </div>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>Nakshatra Lord</span>
                <span className={styles.detailValue}>{shadowData.rahu.nakshatraLord}</span>
              </div>
            </div>

            <div className={styles.strengthSection}>
              <div className={styles.strengthLabel}>
                <TrendingUp size={16} />
                Strength
              </div>
              <div className={styles.strengthBar}>
                <div 
                  className={styles.strengthFill}
                  style={{ 
                    width: `${shadowData.rahu.strength}%`,
                    background: 'linear-gradient(90deg, #8338ec 0%, #fb5607 100%)'
                  }}
                />
              </div>
              <div className={styles.strengthValue}>{shadowData.rahu.strength}/100</div>
            </div>

            <div className={styles.aspects}>
              <div className={styles.aspectsLabel}>Status</div>
              <div className={styles.aspectsList}>
                <span className={styles.aspectPlanet}>
                  {shadowData.rahu.retrograde ? 'Retrograde' : 'Direct'}
                </span>
              </div>
            </div>
          </div>

          {/* Ketu Card */}
          <div className={styles.planetCard} style={{ borderColor: '#fb5607' }}>
            <div className={styles.planetHeader}>
              <div className={styles.planetIcon} style={{ background: 'linear-gradient(135deg, #fb5607 0%, #ff006e 100%)' }}>
                <Moon size={32} style={{ transform: 'rotate(180deg)' }} />
              </div>
              <div>
                <h2 className={styles.planetName}>Ketu</h2>
                <p className={styles.planetSubtitle}>South Node - Detachment & Wisdom</p>
              </div>
            </div>

            <div className={styles.planetDetails}>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>Sign</span>
                <span className={styles.detailValue}>{shadowData.ketu.sign}</span>
              </div>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>Degree</span>
                <span className={styles.detailValue}>{shadowData.ketu.degree}°</span>
              </div>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>House</span>
                <span className={styles.detailValue}>{shadowData.ketu.house}th</span>
              </div>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>Nakshatra</span>
                <span className={styles.detailValue}>{shadowData.ketu.nakshatra}</span>
              </div>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>Pada</span>
                <span className={styles.detailValue}>{shadowData.ketu.pada}</span>
              </div>
              <div className={styles.detailRow}>
                <span className={styles.detailLabel}>Nakshatra Lord</span>
                <span className={styles.detailValue}>{shadowData.ketu.nakshatraLord}</span>
              </div>
            </div>

            <div className={styles.strengthSection}>
              <div className={styles.strengthLabel}>
                <TrendingUp size={16} />
                Strength
              </div>
              <div className={styles.strengthBar}>
                <div 
                  className={styles.strengthFill}
                  style={{ 
                    width: `${shadowData.ketu.strength}%`,
                    background: 'linear-gradient(90deg, #fb5607 0%, #ff006e 100%)'
                  }}
                />
              </div>
              <div className={styles.strengthValue}>{shadowData.ketu.strength}/100</div>
            </div>

            <div className={styles.aspects}>
              <div className={styles.aspectsLabel}>Status</div>
              <div className={styles.aspectsList}>
                <span className={styles.aspectPlanet}>
                  {shadowData.ketu.retrograde ? 'Retrograde' : 'Direct'}
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Tabs */}
      <section className={styles.tabsSection}>
        <div className={styles.tabs}>
          <button
            className={`${styles.tab} ${selectedTab === 'analysis' ? styles.active : ''}`}
            onClick={() => setSelectedTab('analysis')}
          >
            <BookOpen size={20} />
            Life Impact
          </button>
          <button
            className={`${styles.tab} ${selectedTab === 'yogas' ? styles.active : ''}`}
            onClick={() => setSelectedTab('yogas')}
          >
            <Sparkles size={20} />
            Yogas
          </button>
          <button
            className={`${styles.tab} ${selectedTab === 'remedies' ? styles.active : ''}`}
            onClick={() => setSelectedTab('remedies')}
          >
            <AlertCircle size={20} />
            Remedies
          </button>
        </div>

        <div className={styles.tabContent}>
          {selectedTab === 'analysis' && (
            <div className={styles.impactGrid}>
              {shadowData.lifeImpact.map((impact, index) => (
                <div key={index} className={styles.impactCard}>
                  <div className={styles.impactHeader}>
                    <span className={styles.impactPlanet} style={{ 
                      color: impact.planet === 'Rahu' ? '#8338ec' : '#fb5607' 
                    }}>
                      {impact.planet}
                    </span>
                    <span className={`${styles.impactIntensity} ${styles[impact.intensity]}`}>
                      {impact.intensity}
                    </span>
                  </div>
                  <h3 className={styles.impactArea}>{impact.area}</h3>
                  <p className={styles.impactDescription}>{impact.impact}</p>
                </div>
              ))}
            </div>
          )}

          {selectedTab === 'yogas' && (
            <div className={styles.yogasGrid}>
              {shadowData.yogas.map((yoga, index) => (
                <div key={index} className={styles.yogaCard}>
                  <div className={styles.yogaHeader}>
                    <h3 className={styles.yogaName}>{yoga.name}</h3>
                    <span className={`${styles.yogaImpact} ${styles.positive}`}>
                      beneficial
                    </span>
                  </div>
                  <p className={styles.yogaDescription}>{yoga.description}</p>
                  <div className={styles.yogaStrength}>
                    <span>Present: {yoga.present ? 'Yes' : 'No'}</span>
                  </div>
                </div>
              ))}
              
              {/* Mangal Dosha */}
              {sampleChartData.yogas.inauspicious.find(y => y.name.includes('Kuja')) && (
                <div className={styles.yogaCard}>
                  <div className={styles.yogaHeader}>
                    <h3 className={styles.yogaName}>Kuja Dosha (Mangal Dosha)</h3>
                    <span className={`${styles.yogaImpact} ${styles.mixed}`}>
                      challenging
                    </span>
                  </div>
                  <p className={styles.yogaDescription}>
                    {sampleChartData.yogas.inauspicious.find(y => y.name.includes('Kuja'))?.description}
                  </p>
                </div>
              )}
            </div>
          )}

          {selectedTab === 'remedies' && (
            <div className={styles.remediesGrid}>
              <div className={styles.remedyCard}>
                <div className={styles.remedyHeader}>
                  <span className={styles.remedyType}>Mantra</span>
                  <span className={styles.remedyPlanet}>Rahu</span>
                </div>
                <h3 className={styles.remedyTitle}>Rahu Beej Mantra</h3>
                <p className={styles.remedyDescription}>
                  Om Bhram Bhreem Bhroum Sah Rahave Namah (108 times daily)
                </p>
                <div className={styles.remedyTiming}>
                  <span>⏰ Saturday evenings or Rahu Kaal</span>
                </div>
              </div>

              <div className={styles.remedyCard}>
                <div className={styles.remedyHeader}>
                  <span className={styles.remedyType}>Gemstone</span>
                  <span className={styles.remedyPlanet}>Rahu</span>
                </div>
                <h3 className={styles.remedyTitle}>Hessonite (Gomed)</h3>
                <p className={styles.remedyDescription}>
                  Wear hessonite gemstone in silver on middle finger
                </p>
                <div className={styles.remedyTiming}>
                  <span>⏰ Saturday during Rahu hora</span>
                </div>
              </div>

              <div className={styles.remedyCard}>
                <div className={styles.remedyHeader}>
                  <span className={styles.remedyType}>Mantra</span>
                  <span className={styles.remedyPlanet} style={{ background: '#fb5607' }}>Ketu</span>
                </div>
                <h3 className={styles.remedyTitle}>Ketu Beej Mantra</h3>
                <p className={styles.remedyDescription}>
                  Om Shram Shreem Shroum Sah Ketave Namah (108 times daily)
                </p>
                <div className={styles.remedyTiming}>
                  <span>⏰ Tuesday evenings</span>
                </div>
              </div>

              <div className={styles.remedyCard}>
                <div className={styles.remedyHeader}>
                  <span className={styles.remedyType}>Lifestyle</span>
                  <span className={styles.remedyPlanet} style={{ background: '#fb5607' }}>Ketu</span>
                </div>
                <h3 className={styles.remedyTitle}>Meditation Practice</h3>
                <p className={styles.remedyDescription}>
                  Regular meditation and spiritual practices to balance Ketu energy
                </p>
              </div>
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
