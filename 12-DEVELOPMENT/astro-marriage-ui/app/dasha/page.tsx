'use client';

import { useState, useEffect } from 'react';
import { Calendar, Clock, Info, ChevronRight, ChevronDown } from 'lucide-react';
import DashaBalance from '@/components/dasha/DashaBalance';
import styles from './page.module.scss';

// Import the JSON data directly
import dashaData from '@/../../chartsimp';

interface Pratyantardasha {
  name: string;
  start: string;
  end: string;
  id: number;
}

interface Antardasha {
  name: string;
  start: string;
  end: string;
  id: number;
  pratyantardasha: Pratyantardasha[];
}

interface DashaPeriod {
  name: string;
  start: string;
  end: string;
  id: number;
  antardasha: Antardasha[];
}

export default function DashaPage() {
  const [selectedMahadasha, setSelectedMahadasha] = useState<DashaPeriod | null>(null);
  const [selectedAntardasha, setSelectedAntardasha] = useState<Antardasha | null>(null);
  const [expandedPeriods, setExpandedPeriods] = useState<Set<string>>(new Set());
  const currentDate = new Date();

  // Parse the dasha data from JSON
  const dashaBalance = dashaData.data.dasha_balance;
  const dashaPeriods: DashaPeriod[] = dashaData.data.dasha_periods;

  // Find current dasha period
  const getCurrentDasha = () => {
    for (const mahadasha of dashaPeriods) {
      const start = new Date(mahadasha.start);
      const end = new Date(mahadasha.end);
      
      if (currentDate >= start && currentDate <= end) {
        // Find current antardasha
        for (const antardasha of mahadasha.antardasha) {
          const antarStart = new Date(antardasha.start);
          const antarEnd = new Date(antardasha.end);
          
          if (currentDate >= antarStart && currentDate <= antarEnd) {
            return {
              mahadasha: mahadasha.name,
              mahadashaStart: start,
              mahadashaEnd: end,
              antardasha: antardasha.name,
              antardashaStart: antarStart,
              antardashaEnd: antarEnd,
            };
          }
        }
      }
    }
    return null;
  };

  const currentDasha = getCurrentDasha();

  const togglePeriod = (periodName: string) => {
    const newExpanded = new Set(expandedPeriods);
    if (newExpanded.has(periodName)) {
      newExpanded.delete(periodName);
    } else {
      newExpanded.add(periodName);
    }
    setExpandedPeriods(newExpanded);
  };

  const formatDate = (dateStr: string) => {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', { month: 'short', year: 'numeric' });
  };

  const calculateDuration = (start: string, end: string) => {
    const startDate = new Date(start);
    const endDate = new Date(end);
    const years = (endDate.getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24 * 365.25);
    return years.toFixed(1);
  };

  return (
    <div className={styles.dashaPage}>
      {/* Header */}
      <header className={styles.header}>
        <div className={styles.headerContent}>
          <div className={styles.titleSection}>
            <h1 className={styles.title}>Vimshottari Dasha</h1>
            <p className={styles.subtitle}>
              120-year planetary period system based on Moon&apos;s Nakshatra
            </p>
          </div>
          
          <div className={styles.headerStats}>
            <div className={styles.stat}>
              <Calendar className={styles.statIcon} />
              <div>
                <div className={styles.statLabel}>Birth Date</div>
                <div className={styles.statValue}>
                  June 6, 1985
                </div>
              </div>
            </div>
            
            <div className={styles.stat}>
              <Clock className={styles.statIcon} />
              <div>
                <div className={styles.statLabel}>Dasha Balance</div>
                <div className={styles.statValue}>
                  {dashaBalance.lord.name} - {dashaBalance.description}
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Current Period Overview */}
      {currentDasha && (
        <section className={styles.currentSection}>
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>Current Periods</h2>
            <Info className={styles.infoIcon} />
          </div>
          
          <div className={styles.currentGrid}>
            <div className={styles.currentCard}>
              <div className={styles.currentLabel}>Mahadasha</div>
              <div className={styles.currentPlanet}>{currentDasha.mahadasha}</div>
              <div className={styles.currentDates}>
                {formatDate(currentDasha.mahadashaStart.toISOString())} - {formatDate(currentDasha.mahadashaEnd.toISOString())}
              </div>
              <DashaBalance 
                startDate={currentDasha.mahadashaStart}
                endDate={currentDasha.mahadashaEnd}
                currentDate={currentDate}
              />
            </div>
            
            <ChevronRight className={styles.arrow} />
            
            <div className={styles.currentCard}>
              <div className={styles.currentLabel}>Antardasha</div>
              <div className={styles.currentPlanet}>{currentDasha.antardasha}</div>
              <div className={styles.currentDates}>
                {formatDate(currentDasha.antardashaStart.toISOString())} - {formatDate(currentDasha.antardashaEnd.toISOString())}
              </div>
              <DashaBalance 
                startDate={currentDasha.antardashaStart}
                endDate={currentDasha.antardashaEnd}
                currentDate={currentDate}
              />
            </div>
            
            <ChevronRight className={styles.arrow} />
            
            <div className={styles.currentCard}>
              <div className={styles.currentLabel}>Current Period</div>
              <div className={styles.currentPlanet}>
                {currentDasha.mahadasha}/{currentDasha.antardasha}
              </div>
              <div className={styles.currentDates}>
                Active Now
              </div>
            </div>
          </div>
        </section>
      )}

      {/* Mahadasha Timeline */}
      <section className={styles.timelineSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>Complete Dasha Timeline</h2>
          <p className={styles.sectionSubtitle}>All Mahadasha periods from birth</p>
        </div>
        
        <div className={styles.periodsGrid}>
          {dashaPeriods.map((period, index) => {
            const isExpanded = expandedPeriods.has(period.name);
            const isCurrent = currentDasha?.mahadasha === period.name;
            
            return (
              <div key={index} className={styles.periodWrapper}>
                <div 
                  className={`${styles.periodCard} ${isCurrent ? styles.current : ''}`}
                  onClick={() => togglePeriod(period.name)}
                >
                  <div className={styles.periodHeader}>
                    <span className={styles.periodPlanet}>{period.name}</span>
                    <span className={styles.periodDuration}>
                      {calculateDuration(period.start, period.end)} years
                    </span>
                  </div>
                  <div className={styles.periodDates}>
                    {formatDate(period.start)} - {formatDate(period.end)}
                  </div>
                  <div className={styles.periodFooter}>
                    <span className={styles.periodAntar}>
                      {period.antardasha.length} Antardashas
                    </span>
                    {isExpanded ? <ChevronDown size={16} /> : <ChevronRight size={16} />}
                  </div>
                  {isCurrent && <div className={styles.currentBadge}>Current</div>}
                </div>

                {/* Antardasha List */}
                {isExpanded && (
                  <div className={styles.antardashGrid}>
                    {period.antardasha.map((antar, antarIndex) => {
                      const isCurrentAntar = currentDasha?.antardasha === antar.name && isCurrent;
                      
                      return (
                        <div 
                          key={antarIndex} 
                          className={`${styles.antardashCard} ${isCurrentAntar ? styles.currentAntar : ''}`}
                          onClick={(e) => {
                            e.stopPropagation();
                            setSelectedAntardasha(antar);
                          }}
                        >
                          <div className={styles.antardashPlanet}>{antar.name}</div>
                          <div className={styles.antardashDates}>
                            {formatDate(antar.start)} - {formatDate(antar.end)}
                          </div>
                          {isCurrentAntar && <div className={styles.currentDot} />}
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </section>

      {/* Antardasha Details Modal */}
      {selectedAntardasha && (
        <div className={styles.modal} onClick={() => setSelectedAntardasha(null)}>
          <div className={styles.modalContent} onClick={(e) => e.stopPropagation()}>
            <div className={styles.modalHeader}>
              <h3>{selectedAntardasha.name} Antardasha</h3>
              <button onClick={() => setSelectedAntardasha(null)} className={styles.closeBtn}>×</button>
            </div>
            <div className={styles.modalBody}>
              <div className={styles.modalInfo}>
                <span className={styles.modalLabel}>Period:</span>
                <span className={styles.modalValue}>
                  {formatDate(selectedAntardasha.start)} - {formatDate(selectedAntardasha.end)}
                </span>
              </div>
              <div className={styles.modalInfo}>
                <span className={styles.modalLabel}>Pratyantardashas:</span>
                <span className={styles.modalValue}>{selectedAntardasha.pratyantardasha.length}</span>
              </div>
              
              <div className={styles.pratyantarList}>
                <h4>Pratyantardasha Periods:</h4>
                {selectedAntardasha.pratyantardasha.map((pratyantar, index) => (
                  <div key={index} className={styles.pratyantarItem}>
                    <span className={styles.pratyantarName}>{pratyantar.name}</span>
                    <span className={styles.pratyantarDates}>
                      {formatDate(pratyantar.start)} - {formatDate(pratyantar.end)}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Key Information */}
      <section className={styles.upcomingSection}>
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>Dasha System Information</h2>
        </div>
        
        <div className={styles.upcomingGrid}>
          <div className={styles.upcomingCard}>
            <div className={styles.upcomingDate}>Birth Dasha</div>
            <div className={styles.upcomingEvent}>
              {dashaBalance.lord.name} Mahadasha
            </div>
            <div className={styles.upcomingDescription}>
              Balance at birth: {dashaBalance.description}
            </div>
          </div>
          
          <div className={styles.upcomingCard}>
            <div className={styles.upcomingDate}>Total Periods</div>
            <div className={styles.upcomingEvent}>
              {dashaPeriods.length} Mahadashas
            </div>
            <div className={styles.upcomingDescription}>
              Complete 120-year Vimshottari cycle
            </div>
          </div>
          
          <div className={styles.upcomingCard}>
            <div className={styles.upcomingDate}>System</div>
            <div className={styles.upcomingEvent}>
              Vimshottari Dasha
            </div>
            <div className={styles.upcomingDescription}>
              Based on Moon&apos;s Nakshatra at birth
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
