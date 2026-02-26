'use client'

import { useEffect, useRef } from 'react'
import * as d3 from 'd3'
import styles from './BirthChart.module.scss'

interface Planet {
  name: string
  sign: string
  degree: number
  house: number
  color: string
}

const planets: Planet[] = [
  { name: 'Sun', sign: 'Sagittarius', degree: 10.92, house: 5, color: '#FF6B35' },
  { name: 'Moon', sign: 'Virgo', degree: 22.73, house: 2, color: '#F7F7F7' },
  { name: 'Mars', sign: 'Leo', degree: 8.55, house: 1, color: '#E63946' },
  { name: 'Mercury', sign: 'Sagittarius', degree: 18.10, house: 5, color: '#06FFA5' },
  { name: 'Jupiter', sign: 'Scorpio', degree: 9.87, house: 4, color: '#FFD60A' },
  { name: 'Venus', sign: 'Libra', degree: 25.40, house: 3, color: '#F72585' },
  { name: 'Saturn', sign: 'Aquarius', degree: 13.77, house: 7, color: '#4361EE' },
  { name: 'Rahu', sign: 'Libra', degree: 18.25, house: 3, color: '#8338EC' },
  { name: 'Ketu', sign: 'Aries', degree: 18.25, house: 9, color: '#FB5607' },
]

const houses = [
  { number: 1, sign: 'Leo', lord: 'Sun' },
  { number: 2, sign: 'Virgo', lord: 'Mercury' },
  { number: 3, sign: 'Libra', lord: 'Venus' },
  { number: 4, sign: 'Scorpio', lord: 'Mars' },
  { number: 5, sign: 'Sagittarius', lord: 'Jupiter' },
  { number: 6, sign: 'Capricorn', lord: 'Saturn' },
  { number: 7, sign: 'Aquarius', lord: 'Saturn' },
  { number: 8, sign: 'Pisces', lord: 'Jupiter' },
  { number: 9, sign: 'Aries', lord: 'Mars' },
  { number: 10, sign: 'Taurus', lord: 'Venus' },
  { number: 11, sign: 'Gemini', lord: 'Mercury' },
  { number: 12, sign: 'Cancer', lord: 'Moon' },
]

export function BirthChart() {
  const svgRef = useRef<SVGSVGElement>(null)

  useEffect(() => {
    if (!svgRef.current) return

    const svg = d3.select(svgRef.current)
    svg.selectAll('*').remove()

    const width = svgRef.current.clientWidth
    const height = 500
    const centerX = width / 2
    const centerY = height / 2
    const outerRadius = Math.min(width, height) / 2 - 40
    const innerRadius = outerRadius * 0.6

    const g = svg.append('g')

    // Draw outer circle
    g.append('circle')
      .attr('cx', centerX)
      .attr('cy', centerY)
      .attr('r', outerRadius)
      .attr('fill', 'none')
      .attr('stroke', '#667eea')
      .attr('stroke-width', 2)

    // Draw inner circle
    g.append('circle')
      .attr('cx', centerX)
      .attr('cy', centerY)
      .attr('r', innerRadius)
      .attr('fill', 'none')
      .attr('stroke', '#667eea')
      .attr('stroke-width', 1)
      .attr('stroke-dasharray', '5,5')

    // Draw house divisions (12 houses)
    houses.forEach((house, i) => {
      const angle = (i * 30 - 90) * (Math.PI / 180)
      const x1 = centerX + innerRadius * Math.cos(angle)
      const y1 = centerY + innerRadius * Math.sin(angle)
      const x2 = centerX + outerRadius * Math.cos(angle)
      const y2 = centerY + outerRadius * Math.sin(angle)

      // House division lines
      g.append('line')
        .attr('x1', x1)
        .attr('y1', y1)
        .attr('x2', x2)
        .attr('y2', y2)
        .attr('stroke', '#2a2a2a')
        .attr('stroke-width', 1)

      // House numbers
      const labelAngle = ((i * 30 + 15) - 90) * (Math.PI / 180)
      const labelRadius = (innerRadius + outerRadius) / 2
      const labelX = centerX + labelRadius * Math.cos(labelAngle)
      const labelY = centerY + labelRadius * Math.sin(labelAngle)

      g.append('text')
        .attr('x', labelX)
        .attr('y', labelY)
        .attr('text-anchor', 'middle')
        .attr('dominant-baseline', 'middle')
        .attr('fill', '#666666')
        .attr('font-size', '12px')
        .attr('font-weight', '600')
        .text(house.number)

      // Sign names
      const signRadius = outerRadius + 20
      const signX = centerX + signRadius * Math.cos(labelAngle)
      const signY = centerY + signRadius * Math.sin(labelAngle)

      g.append('text')
        .attr('x', signX)
        .attr('y', signY)
        .attr('text-anchor', 'middle')
        .attr('dominant-baseline', 'middle')
        .attr('fill', '#a0a0a0')
        .attr('font-size', '10px')
        .text(house.sign.substring(0, 3))
    })

    // Group planets by house
    const planetsByHouse = new Map<number, Planet[]>()
    planets.forEach(planet => {
      if (!planetsByHouse.has(planet.house)) {
        planetsByHouse.set(planet.house, [])
      }
      planetsByHouse.get(planet.house)!.push(planet)
    })

    // Draw planets
    planetsByHouse.forEach((housePlanets, houseNum) => {
      const houseIndex = houseNum - 1
      const baseAngle = ((houseIndex * 30 + 15) - 90) * (Math.PI / 180)
      const planetRadius = innerRadius * 0.7

      housePlanets.forEach((planet, idx) => {
        const offset = (idx - (housePlanets.length - 1) / 2) * 0.15
        const angle = baseAngle + offset
        const x = centerX + planetRadius * Math.cos(angle)
        const y = centerY + planetRadius * Math.sin(angle)

        // Planet circle
        const planetGroup = g.append('g')
          .attr('class', 'planet-group')
          .style('cursor', 'pointer')

        planetGroup.append('circle')
          .attr('cx', x)
          .attr('cy', y)
          .attr('r', 16)
          .attr('fill', planet.color)
          .attr('opacity', 0.9)
          .on('mouseover', function() {
            d3.select(this)
              .transition()
              .duration(200)
              .attr('r', 20)
              .attr('opacity', 1)
          })
          .on('mouseout', function() {
            d3.select(this)
              .transition()
              .duration(200)
              .attr('r', 16)
              .attr('opacity', 0.9)
          })

        // Planet symbol/initial
        planetGroup.append('text')
          .attr('x', x)
          .attr('y', y)
          .attr('text-anchor', 'middle')
          .attr('dominant-baseline', 'middle')
          .attr('fill', 'white')
          .attr('font-size', '11px')
          .attr('font-weight', '700')
          .attr('pointer-events', 'none')
          .text(planet.name.substring(0, 2))

        // Tooltip on hover
        planetGroup.append('title')
          .text(`${planet.name}\n${planet.sign} ${planet.degree.toFixed(2)}°\nHouse ${planet.house}`)
      })
    })

    // Center text
    g.append('text')
      .attr('x', centerX)
      .attr('y', centerY - 10)
      .attr('text-anchor', 'middle')
      .attr('fill', '#ffffff')
      .attr('font-size', '16px')
      .attr('font-weight', '700')
      .text('D1 Chart')

    g.append('text')
      .attr('x', centerX)
      .attr('y', centerY + 10)
      .attr('text-anchor', 'middle')
      .attr('fill', '#a0a0a0')
      .attr('font-size', '12px')
      .text('Rashi')

  }, [])

  return (
    <div className={styles.container}>
      <svg ref={svgRef} className={styles.svg} />
    </div>
  )
}
