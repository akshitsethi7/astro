'use client';

import { useState } from 'react';
import { useChart } from '@/lib/context/ChartContext';
import { Calendar, MapPin, Clock, User, X, Search } from 'lucide-react';
import styles from './BirthChartForm.module.scss';

interface BirthChartFormProps {
  onClose?: () => void;
}

interface LocationResult {
  name: string;
  lat: number;
  lon: number;
  country: string;
  state?: string;
}

export default function BirthChartForm({ onClose }: BirthChartFormProps) {
  const { birthDetails, setBirthDetails, isLoading } = useChart();
  
  const [formData, setFormData] = useState({
    name: birthDetails?.name || '',
    date: birthDetails?.date || '1995-01-01',
    time: birthDetails?.time || '10:30',
    latitude: birthDetails?.latitude || 28.6139,
    longitude: birthDetails?.longitude || 77.2090,
    timezone: birthDetails?.timezone || 'Asia/Kolkata',
    place: 'New Delhi, India',
  });

  const [locationSearch, setLocationSearch] = useState('');
  const [locationResults, setLocationResults] = useState<LocationResult[]>([]);
  const [isSearching, setIsSearching] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setBirthDetails(formData);
    if (onClose) onClose();
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'latitude' || name === 'longitude' ? parseFloat(value) : value,
    }));
  };

  // Search for location using Nominatim (OpenStreetMap)
  const searchLocation = async () => {
    if (!locationSearch.trim()) return;
    
    setIsSearching(true);
    try {
      const response = await fetch(
        `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(locationSearch)}&format=json&limit=5`
      );
      const data = await response.json();
      
      const results: LocationResult[] = data.map((item: any) => ({
        name: item.display_name,
        lat: parseFloat(item.lat),
        lon: parseFloat(item.lon),
        country: item.address?.country || '',
        state: item.address?.state || '',
      }));
      
      setLocationResults(results);
    } catch (error) {
      console.error('Location search error:', error);
      alert('Failed to search location. Please try again.');
    } finally {
      setIsSearching(false);
    }
  };

  const selectLocation = (location: LocationResult) => {
    setFormData(prev => ({
      ...prev,
      latitude: location.lat,
      longitude: location.lon,
      place: location.name,
    }));
    setLocationResults([]);
    setLocationSearch('');
  };

  // Common locations
  const locations = [
    { name: 'New Delhi, India', lat: 28.6139, lon: 77.2090, tz: 'Asia/Kolkata' },
    { name: 'Mumbai, India', lat: 19.0760, lon: 72.8777, tz: 'Asia/Kolkata' },
    { name: 'Bangalore, India', lat: 12.9716, lon: 77.5946, tz: 'Asia/Kolkata' },
    { name: 'New York, USA', lat: 40.7128, lon: -74.0060, tz: 'America/New_York' },
    { name: 'London, UK', lat: 51.5074, lon: -0.1278, tz: 'Europe/London' },
  ];

  const setLocation = (location: typeof locations[0]) => {
    setFormData(prev => ({
      ...prev,
      latitude: location.lat,
      longitude: location.lon,
      timezone: location.tz,
      place: location.name,
    }));
  };

  return (
    <div className={styles.formContainer}>
      <div className={styles.formHeader}>
        <h2 className={styles.formTitle}>Enter Birth Details</h2>
        {onClose && (
          <button onClick={onClose} className={styles.closeBtn}>
            <X size={24} />
          </button>
        )}
      </div>

      <form onSubmit={handleSubmit} className={styles.form}>
        <div className={styles.formGroup}>
          <label className={styles.label}>
            <User size={18} />
            Name (Optional)
          </label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Enter name"
            className={styles.input}
          />
        </div>

        <div className={styles.formRow}>
          <div className={styles.formGroup}>
            <label className={styles.label}>
              <Calendar size={18} />
              Birth Date
            </label>
            <input
              type="date"
              name="date"
              value={formData.date}
              onChange={handleChange}
              required
              className={styles.input}
            />
          </div>

          <div className={styles.formGroup}>
            <label className={styles.label}>
              <Clock size={18} />
              Birth Time
            </label>
            <input
              type="time"
              name="time"
              value={formData.time}
              onChange={handleChange}
              required
              className={styles.input}
            />
          </div>
        </div>

        {/* Location Search */}
        <div className={styles.formGroup}>
          <label className={styles.label}>
            <MapPin size={18} />
            Search Birth Place
          </label>
          <div className={styles.searchContainer}>
            <input
              type="text"
              value={locationSearch}
              onChange={(e) => setLocationSearch(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && (e.preventDefault(), searchLocation())}
              placeholder="Search city, town, or place..."
              className={styles.input}
            />
            <button
              type="button"
              onClick={searchLocation}
              disabled={isSearching}
              className={styles.searchBtn}
            >
              <Search size={18} />
              {isSearching ? 'Searching...' : 'Search'}
            </button>
          </div>
          
          {locationResults.length > 0 && (
            <div className={styles.searchResults}>
              {locationResults.map((result, index) => (
                <button
                  key={index}
                  type="button"
                  onClick={() => selectLocation(result)}
                  className={styles.searchResult}
                >
                  <MapPin size={16} />
                  <div className={styles.resultInfo}>
                    <div className={styles.resultName}>{result.name}</div>
                    <div className={styles.resultCoords}>
                      {result.lat.toFixed(4)}°, {result.lon.toFixed(4)}°
                    </div>
                  </div>
                </button>
              ))}
            </div>
          )}
        </div>

        <div className={styles.formGroup}>
          <label className={styles.label}>Quick Locations</label>
          <div className={styles.locationButtons}>
            {locations.map((loc) => (
              <button
                key={loc.name}
                type="button"
                onClick={() => setLocation(loc)}
                className={styles.locationBtn}
              >
                {loc.name}
              </button>
            ))}
          </div>
        </div>

        <div className={styles.formRow}>
          <div className={styles.formGroup}>
            <label className={styles.label}>Latitude</label>
            <input
              type="number"
              name="latitude"
              value={formData.latitude}
              onChange={handleChange}
              step="0.0001"
              required
              className={styles.input}
            />
          </div>

          <div className={styles.formGroup}>
            <label className={styles.label}>Longitude</label>
            <input
              type="number"
              name="longitude"
              value={formData.longitude}
              onChange={handleChange}
              step="0.0001"
              required
              className={styles.input}
            />
          </div>
        </div>

        <div className={styles.formGroup}>
          <label className={styles.label}>Timezone</label>
          <select
            name="timezone"
            value={formData.timezone}
            onChange={handleChange}
            required
            className={styles.select}
          >
            <option value="Asia/Kolkata">Asia/Kolkata (IST +5:30)</option>
            <option value="America/New_York">America/New_York (EST -5:00)</option>
            <option value="America/Los_Angeles">America/Los_Angeles (PST -8:00)</option>
            <option value="America/Chicago">America/Chicago (CST -6:00)</option>
            <option value="Europe/London">Europe/London (GMT +0:00)</option>
            <option value="Europe/Paris">Europe/Paris (CET +1:00)</option>
            <option value="Australia/Sydney">Australia/Sydney (AEST +10:00)</option>
            <option value="Asia/Dubai">Asia/Dubai (GST +4:00)</option>
            <option value="Asia/Singapore">Asia/Singapore (SGT +8:00)</option>
            <option value="Asia/Tokyo">Asia/Tokyo (JST +9:00)</option>
          </select>
        </div>

        <div className={styles.infoBox}>
          <strong>Note:</strong> For accurate calculations, ensure:
          <ul>
            <li>Birth time is in 24-hour format (HH:MM)</li>
            <li>Timezone matches your birth location</li>
            <li>Coordinates are accurate (use location search)</li>
          </ul>
        </div>

        <button
          type="submit"
          disabled={isLoading}
          className={styles.submitBtn}
        >
          {isLoading ? 'Calculating...' : 'Calculate Chart'}
        </button>
      </form>
    </div>
  );
}

