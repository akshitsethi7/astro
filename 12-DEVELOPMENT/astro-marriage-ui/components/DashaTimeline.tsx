'use client'

import { useEffect, useRef, useState } from 'react'
import * as d3 from 'd3'
import styles from './DashaTimeline.module.scss'

interface DashaPeriod {
  planet: string
  start: Date
  end: Date
  color: string
  significance: string
}

const dashaData: DashaPeriod[] = [
  { planet: 'Jupiter-Mercury', start: new Date('2025-02-06'), end: new Date('2027-05-14'), color: '#FFD60A', significance: 'Good period' },
  { planet: 'Jupiter-Ketu', start: new Date('2027-05-14'), end: new Date('2028-04-20'), color: '#FB5607', significance: 'Spiritual' },
  { planet: 'Jupiter-Venus', start: new Date('2028-04-20'), end: new Date('2030-12-20'), color: '#F72585', significance: 'Best for marriage' },
  { planet: 'Jupiter-Sun', start: new Date('2030-12-20'), end: new Date('2031-10-26'), color: '#FF6B35', significance: 'Authority' },
  { planet: 'Jupiter-Moon', start: new Date('2031-10-26'), end: new Date('2033-02-26'), color: '#F7F7F7', significance: 'Emotional' },
  { planet: 'Jupiter-Mars', start: new Date('2033-02-26'), end: new Date('2034-02-01'), color: '#E63946', significance: 'Action' },
]

export function DashaTimeline() {
  const svgRef = useRef<SVGSVGElement>(null)
  const [selectedDasha, setSelectedDasha] = useState<DashaPeriod | null>(null)

  useEffect(() => {
    if (!svgRef.current) return

    const svg = d3.select(svgRef.current)
    svg.selectAll('*').remove()

    const margin = { top: 40, right: 20, bottom: 60, left: 20 }
    const width = svgRef.current.clientWidth - margin.left - margin.right
    const height = 200 - margin.top - margin.bottom

    const g = svg
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`)

    // Time scale
    const xScale = d3.scaleTime()
      .domain([new Date('2025-01-01'), new Date('2035-01-01')])
      .range([0, width])

    // Current date marker
    const now = new Date()
    const nowX = xScale(now)

    // Draw timeline base
    g.append('line')
      .attr('x1', 0)
      .attr('y1', height / 2)
      .attr('x2', width)
      .attr('y2', height / 2)
      .attr('stroke', '#2a2a2a')
      .attr('stroke-width', 2)

    // Draw dasha periods
    dashaData.forEach((dasha, i) => {
      const x1 = xScale(dasha.start)
      const x2 = xScale(dasha.end)
      const barWidth = x2 - x1
      const barHeight = 40
      const y = height / 2 - barHeight / 2

      // Dasha bar
      const dashaGroup = g.append('g')
        .attr('class', 'dasha-period')
        .style('cursor', 'pointer')
        .on('click', () => setSelectedDasha(dasha))

      dashaGroup.append('rect')
        .attr('x', x1)
        .attr('y', y)
        .attr('width', barWidth)
        .attr('height', barHeight)
        .attr('fill', dasha.color)
        .attr('opacity', 0.8)
        .attr('rx', 6)
        .on('mouseover', function() {
          d3.select(this)
            .transition()
            .duration(200)
            .attr('opacity', 1)
            .attr('y', y - 5)
            .attr('height', barHeight + 10)
        })
        .on('mouseout', function() {
          d3.select(this)
            .transition()
            .duration(200)
            .attr('opacity', 0.8)
            .attr('y', y)
            .attr('height', barHeight)
        })

      // Planet name
      dashaGroup.append('text')
        .attr('x', x1 + barWidth / 2)
        .attr('y', height / 2)
        .attr('text-anchor', 'middle')
        .attr('dominant-baseline', 'middle')
        .attr('fill', 'white')
        .attr('font-size', '12px')
        .attr('font-weight', '600')
        .attr('pointer-events', 'none')
        .text(dasha.planet.split('-')[1])

      // Start year label
      if (i === 0 || dasha.start.getFullYear() !== dashaData[i - 1].end.getFullYear()) {
        g.append('text')
          .attr('x', x1)
          .attr('y', height / 2 + 50)
          .attr('text-anchor', 'middle')
          .attr('fill', '#a0a0a0')
          .attr('font-size', '11px')
          .text(dasha.start.getFullYear())
      }
    })

    // Current date indicator
    if (nowX >= 0 && nowX <= width) {
      g.append('line')
        .attr('x1', nowX)
        .attr('y1', 0)
        .attr('x2', nowX)
        .attr('y2', height)
        .attr('stroke', '#667eea')
        .attr('stroke-width', 2)
        .attr('stroke-dasharray', '5,5')

      g.append('text')
        .attr('x', nowX)
        .attr('y', -10)
        .attr('text-anchor', 'middle')
        .attr('fill', '#667eea')
        .attr('font-size', '11px')
        .attr('font-weight', '600')
        .text('Now')
    }

    // Title
    g.append('text')
      .attr('x', width / 2)
      .attr('y', -20)
      .attr('text-anchor', 'middle')
      .attr('fill', '#ffffff')
      .attr('font-size', '14px')
      .attr('font-weight', '600')
      .text('Jupiter Mahadasha Timeline (2025-2035)')

  }, [])

  return (
    <div className={styles.container}>
      <svg ref={svgRef} className={styles.svg} />
      
      {selectedDasha && (
        <div className={styles.info}>
          <div className={styles.infoHeader}>
            <span className={styles.infoPlanet}>{selectedDasha.planet}</span>
            <button 
              className={styles.closeBtn}
              onClick={() => setSelectedDasha(null)}
            >
              ×
            </button>
          </div>
          <div className={styles.infoContent}>
            <div className={styles.infoRow}>
              <span className={styles.infoLabel}>Period:</span>
              <span className={styles.infoValue}>
                {selectedDasha.start.toLocaleDateString()} - {selectedDasha.end.toLocaleDateString()}
              </span>
            </div>
            <div className={styles.infoRow}>
              <span className={styles.infoLabel}>Significance:</span>
              <span className={styles.infoValue}>{selectedDasha.significance}</span>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
