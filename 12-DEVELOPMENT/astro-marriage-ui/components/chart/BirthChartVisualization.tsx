'use client';

import { useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { getPlanetColor } from '@/lib/calculations/planets';
import styles from './BirthChartVisualization.module.scss';

interface BirthChartVisualizationProps {
  chartData: any;
  selectedPlanet: string | null;
  onPlanetSelect: (planet: string | null) => void;
}

export default function BirthChartVisualization({ 
  chartData, 
  selectedPlanet,
  onPlanetSelect 
}: BirthChartVisualizationProps) {
  const svgRef = useRef<SVGSVGElement>(null);

  useEffect(() => {
    if (!svgRef.current) return;

    const svg = d3.select(svgRef.current);
    const width = svgRef.current.clientWidth;
    const height = 600;
    const centerX = width / 2;
    const centerY = height / 2;
    const radius = Math.min(width, height) / 2 - 60;

    svg.selectAll('*').remove();
    svg.attr('height', height);

    const g = svg.append('g')
      .attr('transform', `translate(${centerX}, ${centerY})`);

    // Draw zodiac wheel
    const signs = [
      'Aries', 'Taurus', 'Gemini', 'Cancer',
      'Leo', 'Virgo', 'Libra', 'Scorpio',
      'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ];

    const signColors: Record<string, string> = {
      'Aries': '#ef4444', 'Taurus': '#22c55e', 'Gemini': '#eab308',
      'Cancer': '#3b82f6', 'Leo': '#f59e0b', 'Virgo': '#84cc16',
      'Libra': '#ec4899', 'Scorpio': '#dc2626', 'Sagittarius': '#8b5cf6',
      'Capricorn': '#06b6d4', 'Aquarius': '#6366f1', 'Pisces': '#14b8a6'
    };

    // Draw sign segments
    signs.forEach((sign, i) => {
      const startAngle = (i * 30 - 90) * (Math.PI / 180);
      const endAngle = ((i + 1) * 30 - 90) * (Math.PI / 180);

      const arc = d3.arc()
        .innerRadius(radius * 0.7)
        .outerRadius(radius)
        .startAngle(startAngle)
        .endAngle(endAngle);

      g.append('path')
        .attr('d', arc as any)
        .attr('fill', signColors[sign])
        .attr('opacity', 0.1)
        .attr('stroke', signColors[sign])
        .attr('stroke-width', 2)
        .attr('stroke-opacity', 0.3);

      // Sign labels
      const labelAngle = (i * 30 + 15 - 90) * (Math.PI / 180);
      const labelRadius = radius * 0.85;
      const labelX = Math.cos(labelAngle) * labelRadius;
      const labelY = Math.sin(labelAngle) * labelRadius;

      g.append('text')
        .attr('x', labelX)
        .attr('y', labelY)
        .attr('text-anchor', 'middle')
        .attr('dominant-baseline', 'middle')
        .attr('fill', signColors[sign])
        .attr('font-size', '14px')
        .attr('font-weight', '700')
        .text(sign.substring(0, 3));
    });

    // Draw house divisions
    for (let i = 0; i < 12; i++) {
      const angle = (i * 30 - 90) * (Math.PI / 180);
      const x1 = Math.cos(angle) * (radius * 0.7);
      const y1 = Math.sin(angle) * (radius * 0.7);
      const x2 = Math.cos(angle) * radius;
      const y2 = Math.sin(angle) * radius;

      g.append('line')
        .attr('x1', x1)
        .attr('y1', y1)
        .attr('x2', x2)
        .attr('y2', y2)
        .attr('stroke', 'rgba(255, 255, 255, 0.2)')
        .attr('stroke-width', 1);
    }

    // Draw inner circle
    g.append('circle')
      .attr('r', radius * 0.7)
      .attr('fill', 'none')
      .attr('stroke', 'rgba(255, 255, 255, 0.3)')
      .attr('stroke-width', 2);

    // Draw outer circle
    g.append('circle')
      .attr('r', radius)
      .attr('fill', 'none')
      .attr('stroke', 'rgba(255, 255, 255, 0.3)')
      .attr('stroke-width', 2);

    // Plot planets
    chartData.planets.forEach((planetData: any) => {
      const signIndex = signs.indexOf(planetData.sign);
      const angle = ((signIndex * 30 + planetData.degree) - 90) * (Math.PI / 180);
      const planetRadius = radius * 0.55;
      const x = Math.cos(angle) * planetRadius;
      const y = Math.sin(angle) * planetRadius;

      const planetGroup = g.append('g')
        .attr('class', 'planet-group')
        .style('cursor', 'pointer')
        .on('click', () => onPlanetSelect(planetData.planet))
        .on('mouseenter', function() {
          d3.select(this).select('circle')
            .transition()
            .duration(200)
            .attr('r', 20);
        })
        .on('mouseleave', function() {
          d3.select(this).select('circle')
            .transition()
            .duration(200)
            .attr('r', 16);
        });

      // Planet circle
      planetGroup.append('circle')
        .attr('cx', x)
        .attr('cy', y)
        .attr('r', selectedPlanet === planetData.planet ? 20 : 16)
        .attr('fill', getPlanetColor(planetData.planet))
        .attr('opacity', 0.9)
        .attr('stroke', 'white')
        .attr('stroke-width', selectedPlanet === planetData.planet ? 3 : 2);

      // Planet symbol/initial
      planetGroup.append('text')
        .attr('x', x)
        .attr('y', y)
        .attr('text-anchor', 'middle')
        .attr('dominant-baseline', 'middle')
        .attr('fill', 'white')
        .attr('font-size', '12px')
        .attr('font-weight', '700')
        .attr('pointer-events', 'none')
        .text(planetData.planet.substring(0, 2));

      // Retrograde indicator
      if (planetData.retrograde) {
        planetGroup.append('text')
          .attr('x', x + 12)
          .attr('y', y - 12)
          .attr('text-anchor', 'middle')
          .attr('fill', '#ef4444')
          .attr('font-size', '10px')
          .attr('font-weight', '700')
          .attr('pointer-events', 'none')
          .text('R');
      }
    });

    // Draw ascendant marker
    g.append('line')
      .attr('x1', 0)
      .attr('y1', 0)
      .attr('x2', radius * 0.7)
      .attr('y2', 0)
      .attr('stroke', '#FFD23F')
      .attr('stroke-width', 3);

    g.append('text')
      .attr('x', radius * 0.75)
      .attr('y', 0)
      .attr('text-anchor', 'start')
      .attr('dominant-baseline', 'middle')
      .attr('fill', '#FFD23F')
      .attr('font-size', '14px')
      .attr('font-weight', '700')
      .text('ASC');

  }, [chartData, selectedPlanet, onPlanetSelect]);

  return (
    <div className={styles.chartViz}>
      <svg ref={svgRef} width="100%"></svg>
    </div>
  );
}
