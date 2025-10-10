import React, { useState } from 'react';
import TrackerForm from './components/TrackerForm';
import TrackerResult from './components/TrackerResult';
import './App.css';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="app-container">
      <h1>📱 Tracker Pro App</h1>
      <TrackerForm setResult={setResult} />
      {result && <TrackerResult data={result} />}
    </div>
  );
}

export default App;

