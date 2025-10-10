import React from 'react';

const MapView = ({ coords }) => {
  const [lat, lng] = coords;
  const url = `https://www.google.com/maps?q=${lat},${lng}&z=15&output=embed`;

  return (
    <iframe
      src={url}
      width="100%"
      height="300"
      title="Google Map"
      style={{ borderRadius: '10px', border: 'none' }}
    ></iframe>
  );
};

export default MapView;
