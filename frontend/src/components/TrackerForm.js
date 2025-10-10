import React, { useState } from 'react';
import axios from 'axios';

const TrackerForm = ({ setResult }) => {
  const [number, setNumber] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('http://localhost:5000/api/track_number', { number });
    setResult(response.data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter phone number"
        value={number}
        onChange={(e) => setNumber(e.target.value)}
      />
      <button type="submit">Track</button>
    </form>
  );
};

export default TrackerForm;


