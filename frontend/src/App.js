import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/health');
        if (!response.ok) throw new Error('API Error');
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>🌍 West Bengal Monitor AI</h1>
        <p>Real-time Monitoring & Predictions</p>
      </header>
      
      <main className="container">
        {loading && <p>Loading...</p>}
        {error && <p className="error">Error: {error}</p>}
        {data && (
          <div className="status-card">
            <h2>API Status</h2>
            <p>Status: {data.status}</p>
            <p>Service: {data.service}</p>
            <p>Time: {new Date(data.timestamp).toLocaleString()}</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
