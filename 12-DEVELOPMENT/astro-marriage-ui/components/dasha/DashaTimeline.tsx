'use client';

import { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';
import { calculateVimshottariDasha } from '@/lib/calculations/vimshottari';
import { getPlanetColor } from '@/lib/calculations/planets';
import styles from './DashaTimeline.module.scss';

interface DashaTimelineProps {
  birthDate: Date;
  moonDegree: number;
  currentDate?: Date;
  onPeriodSelect?: (period: any) => void;
}

export default function DashaTimeline({ 
  birthDate, 
  moonDegree, 
  currentDate = new Date(),
  onPeriodSelect 
}: DashaTimelineProps) {
  const svgRef = useRef<SVGSVGElement>(null);
  const [expandedPeriod, setExpandedPeriod] = useState<string | null>(null);

  useEffect(() => {
    if (!svgRef.current) return;

    // Calculate Dasha
    const dasha = calculateVimshottariDasha(birthDate, moonDegree);
    
    const svg = d3.select(svgRef.current);
    const width = svgRef.current.clientWidth;
    const height = expandedPeriod ? 400 : 200;

    svg.selectAll('*').remove();
    svg.attr('height', height);

    // Show only next 40 years from current date for better visibility
    const viewStart = new Date(currentDate);
    viewStart.setFullYear(currentDate.getFullYear() - 5);
    const viewEnd = new Date(currentDate);
    viewEnd.setFullYear(currentDate.getFullYear() + 35);

    const xScale = d3.scaleTime()
      .domain([viewStart, viewEnd])
      .range([40, width - 40]);

    const g = svg.append('g');

    // Filter mahadashas in view
    const visibleMahadashas = dasha.mahadashas.filter(md => 
      md.endDate >= viewStart && md.startDate <= viewEnd
    );

    // Draw Mahadasha bars
    const mahadashaHeight = 80;
    const mahadashaY = 40;

    visibleMahadashas.forEach(md => {
      const x = Math.max(40, xScale(md.startDate));
      const endX = Math.min(width - 40, xScale(md.endDate));
      const barWidth = endX - x;

      if (barWidth > 0) {
        const group = g.append('g')
          .attr('class', 'mahadasha-group')
          .style('cursor', 'pointer')
          .on('click', () => {
            setExpandedPeriod(expandedPeriod === md.planet ? null : md.planet);
            if (onPeriodSelect) {
              onPeriodSelect(md);
            }
          });

        // Bar
        group.append('rect')
          .attr('x', x)
          .attr('y', mahadashaY)
          .attr('width', barWidth)
          .attr('height', mahadashaHeight)
          .attr('fill', getPlanetColor(md.planet))
          .attr('opacity', 0.8)
          .attr('rx', 8)
          .on('mouseenter', function() {
            d3.select(this)
              .transition()
              .duration(200)
              .attr('opacity', 1)
              .attr('y', mahadashaY - 4)
              .attr('height', mahadashaHeight + 4);
          })
          .on('mouseleave', function() {
            d3.select(this)
              .transition()
              .duration(200)
              .attr('opacity', 0.8)
              .attr('y', mahadashaY)
              .attr('height', mahadashaHeight);
          });

        // Label
        if (barWidth > 60) {
          group.append('text')
            .attr('x', x + barWidth / 2)
            .attr('y', mahadashaY + mahadashaHeight / 2)
            .attr('text-anchor', 'middle')
            .attr('dominant-baseline', 'middle')
            .attr('fill', 'white')
            .attr('font-size', '16px')
            .attr('font-weight', '700')
            .attr('pointer-events', 'none')
            .text(md.planet);

          // Dates
          group.append('text')
            .attr('x', x + barWidth / 2)
            .attr('y', mahadashaY + mahadashaHeight / 2 + 20)
            .attr('text-anchor', 'middle')
            .attr('fill', 'rgba(255,255,255,0.8)')
            .attr('font-size', '11px')
            .attr('font-family', 'IBM Plex Mono, monospace')
            .attr('pointer-events', 'none')
            .text(`${md.startDate.getFullYear()} - ${md.endDate.getFullYear()}`);
        }

        // Draw Antardashas if expanded
        if (expandedPeriod === md.planet && md.antardashas) {
          const antardashaY = mahadashaY + mahadashaHeight + 20;
          const antardashaHeight = 60;

          md.antardashas.forEach(ad => {
            const adX = Math.max(40, xScale(ad.startDate));
            const adEndX = Math.min(width - 40, xScale(ad.endDate));
            const adWidth = adEndX - adX;

            if (adWidth > 0) {
              const adGroup = g.append('g')
                .style('cursor', 'pointer')
                .on('click', (event) => {
                  event.stopPropagation();
                  if (onPeriodSelect) {
                    onPeriodSelect(ad);
                  }
                });

              adGroup.append('rect')
                .attr('x', adX)
                .attr('y', antardashaY)
                .attr('width', adWidth)
                .attr('height', antardashaHeight)
                .attr('fill', getPlanetColor(ad.planet))
                .attr('opacity', 0.6)
                .attr('rx', 6)
                .on('mouseenter', function() {
                  d3.select(this)
                    .transition()
                    .duration(200)
                    .attr('opacity', 0.9);
                })
                .on('mouseleave', function() {
                  d3.select(this)
                    .transition()
                    .duration(200)
                    .attr('opacity', 0.6);
                });

              if (adWidth > 40) {
                adGroup.append('text')
                  .attr('x', adX + adWidth / 2)
                  .attr('y', antardashaY + antardashaHeight / 2)
                  .attr('text-anchor', 'middle')
                  .attr('dominant-baseline', 'middle')
                  .attr('fill', 'white')
                  .attr('font-size', '12px')
                  .attr('font-weight', '600')
                  .attr('pointer-events', 'none')
                  .text(ad.planet);
              }
            }
          });

          // Label for Antardasha section
          g.append('text')
            .attr('x', 10)
            .attr('y', antardashaY + antardashaHeight / 2)
            .attr('fill', 'rgba(255,255,255,0.6)')
            .attr('font-size', '12px')
            .text('Antardashas');
        }
      }
    });

    // Add current date indicator
    const nowX = xScale(currentDate);
    if (nowX >= 40 && nowX <= width - 40) {
      g.append('line')
        .attr('x1', nowX)
        .attr('x2', nowX)
        .attr('y1', 20)
        .attr('y2', height - 20)
        .attr('stroke', '#FFD23F')
        .attr('stroke-width', 3)
        .attr('stroke-dasharray', '6,4');

      g.append('text')
        .attr('x', nowX)
        .attr('y', 15)
        .attr('text-anchor', 'middle')
        .attr('fill', '#FFD23F')
        .attr('font-size', '12px')
        .attr('font-weight', '700')
        .text('NOW');
    }

    // Add time axis
    const xAxis = d3.axisBottom(xScale)
      .ticks(8)
      .tickFormat(d => d3.timeFormat('%Y')(d as Date));

    g.append('g')
      .attr('transform', `translate(0, ${height - 30})`)
      .call(xAxis)
      .attr('color', 'rgba(255,255,255,0.5)')
      .selectAll('text')
      .attr('font-family', 'IBM Plex Mono, monospace')
      .attr('font-size', '11px');

  }, [birthDate, moonDegree, currentDate, expandedPeriod, onPeriodSelect]);

  return (
    <div className={styles.timeline}>
      <svg ref={svgRef} width="100%" height="200"></svg>
    </div>
  );
}
