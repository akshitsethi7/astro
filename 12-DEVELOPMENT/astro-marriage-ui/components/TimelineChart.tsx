'use client'

import { useEffect, useRef } from 'react'
import * as d3 from 'd3'
import styles from './TimelineChart.module.scss'

export function TimelineChart() {
  const svgRef = useRef<SVGSVGElement>(null)

  useEffect(() => {
    if (!svgRef.current) return

    const data = [
      { year: 2024, label: 'Now', value: 20, color: '#667eea' },
      { year: 2025, label: 'Good Period', value: 60, color: '#4facfe' },
      { year: 2026, label: 'Building', value: 40, color: '#667eea' },
      { year: 2027, label: 'Meeting', value: 70, color: '#43e97b' },
      { year: 2028, label: 'Peak Period', value: 95, color: '#f093fb' },
      { year: 2029, label: 'Marriage', value: 100, color: '#f5576c' },
      { year: 2030, label: 'Stable', value: 85, color: '#38f9d7' },
    ]

    const svg = d3.select(svgRef.current)
    svg.selectAll('*').remove()

    const margin = { top: 20, right: 20, bottom: 40, left: 40 }
    const width = svgRef.current.clientWidth - margin.left - margin.right
    const height = 300 - margin.top - margin.bottom

    const g = svg
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`)

    const x = d3.scaleBand()
      .domain(data.map(d => d.year.toString()))
      .range([0, width])
      .padding(0.3)

    const y = d3.scaleLinear()
      .domain([0, 100])
      .range([height, 0])

    // Add gradient definitions
    const defs = svg.append('defs')
    data.forEach((d, i) => {
      const gradient = defs.append('linearGradient')
        .attr('id', `gradient-${i}`)
        .attr('x1', '0%')
        .attr('y1', '0%')
        .attr('x2', '0%')
        .attr('y2', '100%')

      gradient.append('stop')
        .attr('offset', '0%')
        .attr('stop-color', d.color)
        .attr('stop-opacity', 0.8)

      gradient.append('stop')
        .attr('offset', '100%')
        .attr('stop-color', d.color)
        .attr('stop-opacity', 0.2)
    })

    // Add bars
    g.selectAll('.bar')
      .data(data)
      .enter()
      .append('rect')
      .attr('class', 'bar')
      .attr('x', d => x(d.year.toString()) || 0)
      .attr('y', height)
      .attr('width', x.bandwidth())
      .attr('height', 0)
      .attr('rx', 6)
      .attr('fill', (d, i) => `url(#gradient-${i})`)
      .transition()
      .duration(1000)
      .delay((d, i) => i * 100)
      .attr('y', d => y(d.value))
      .attr('height', d => height - y(d.value))

    // Add labels
    g.selectAll('.label')
      .data(data)
      .enter()
      .append('text')
      .attr('class', 'label')
      .attr('x', d => (x(d.year.toString()) || 0) + x.bandwidth() / 2)
      .attr('y', d => y(d.value) - 10)
      .attr('text-anchor', 'middle')
      .attr('fill', '#a0a0a0')
      .attr('font-size', '12px')
      .attr('font-weight', '600')
      .attr('opacity', 0)
      .text(d => d.label)
      .transition()
      .duration(500)
      .delay((d, i) => i * 100 + 1000)
      .attr('opacity', 1)

    // Add x-axis
    g.append('g')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(x))
      .attr('color', '#666666')
      .selectAll('text')
      .attr('font-size', '14px')
      .attr('font-weight', '500')

    // Add y-axis
    g.append('g')
      .call(d3.axisLeft(y).ticks(5))
      .attr('color', '#666666')
      .selectAll('text')
      .attr('font-size', '12px')

  }, [])

  return (
    <div className={styles.container}>
      <svg ref={svgRef} className={styles.svg} />
    </div>
  )
}
