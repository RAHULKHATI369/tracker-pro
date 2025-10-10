import React from 'react';
import MapView from './MapView';

const TrackerResult = ({ data }) => {
  return (
    <div className="result-card">
      <h3>📞 {data.number}</h3>
      <p>Location: {data.location}</p>
      <p>Provider: {data.provider}</p>
      <p>Last Updated: {data.last_updated}</p>
      <MapView coords={data.coordinates} />
    </div>
  );
};

export default TrackerResult;
