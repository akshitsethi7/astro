/**
 * Test script to verify astronomical calculations
 * Run with: node --loader ts-node/esm test-calculations.ts
 */

import { calculateChart } from './lib/calculations/planets.js';
import { calculatePlanetaryPositions } from './lib/calculations/ephemeris.js';

// Test with a known birth chart
// Example: January 1, 1995, 10:30 AM IST, New Delhi (28.6139°N, 77.2090°E)
const testDate = new Date('1995-01-01');
const testTime = '10:30';
const testLatitude = 28.6139;
const testLongitude = 77.2090;
const testTimezone = 'Asia/Kolkata';

console.log('=== Testing Astronomical Calculations ===\n');

// Test 1: Calculate planetary positions
console.log('Test 1: Planetary Positions');
console.log('Date:', testDate.toISOString());
const positions = calculatePlanetaryPositions(testDate);
console.log('\nPlanetary Longitudes (Sidereal):');
positions.forEach(pos => {
  console.log(`${pos.planet.padEnd(10)}: ${pos.longitude.toFixed(4)}° ${pos.isRetrograde ? '(R)' : ''}`);
});

// Test 2: Calculate complete chart
console.log('\n\nTest 2: Complete Chart Calculation');
const chart = calculateChart(
  testDate,
  testTime,
  testTimezone,
  testLatitude,
  testLongitude,
  'Lahiri'
);

console.log('\nAscendant:', chart.ascendant.sign, chart.ascendant.degree.toFixed(2) + '°');
console.log('\nPlanetary Positions:');
chart.planets.forEach((data, planet) => {
  console.log(`${planet.padEnd(10)}: ${data.sign.padEnd(12)} ${data.degree.toFixed(2)}° House ${data.house} ${data.retrograde ? '(R)' : ''}`);
  console.log(`              Nakshatra: ${data.nakshatra} Pada ${data.nakshatraPada}`);
  console.log(`              Dignity: ${data.dignity}`);
});

console.log('\nHouses:');
chart.houses.forEach(house => {
  console.log(`House ${house.number}: ${house.sign} (Lord: ${house.lord}) - Planets: ${house.planets.join(', ') || 'None'}`);
});

console.log('\n=== Calculation Test Complete ===');
