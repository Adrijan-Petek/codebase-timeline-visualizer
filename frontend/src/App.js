import React, { useState, useEffect } from 'react';
import './App.css';
import Timeline from './components/Timeline';

function App() {
  const [timelineData, setTimelineData] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [maxTime, setMaxTime] = useState(100);

  useEffect(() => {
    // Try to load timeline data from API
    fetch('/api/timeline')
      .then(response => response.json())
      .then(data => {
        setTimelineData(data);
        if (data.timeline && data.timeline.length > 0) {
          setMaxTime(data.timeline.length - 1);
        }
      })
      .catch(error => {
        console.log('No timeline data available:', error);
      });
  }, []);

  const handlePlayPause = () => {
    setIsPlaying(!isPlaying);
  };

  const handleTimeChange = (event) => {
    const newTime = parseInt(event.target.value);
    setCurrentTime(newTime);
  };

  const formatTime = (time) => {
    if (!timelineData || !timelineData.timeline) return '00:00';
    const commit = timelineData.timeline[time];
    if (!commit) return '00:00';
    const date = new Date(commit.timestamp * 1000);
    return date.toLocaleDateString();
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Codebase Timeline Visualizer</h1>
        <p>Interactive visualization of repository evolution over time</p>
      </header>
      <main className="App-main">
        <div className="timeline-container">
          <div className="controls">
            <button className="play-button" onClick={handlePlayPause}>
              {isPlaying ? 'Pause' : 'Play'}
            </button>
            <input
              type="range"
              className="timeline-slider"
              min="0"
              max={maxTime}
              value={currentTime}
              onChange={handleTimeChange}
            />
            <span className="time-display">
              {formatTime(currentTime)} / {formatTime(maxTime)}
            </span>
          </div>
          <div className="visualization-area">
            {timelineData ? (
              <Timeline
                data={timelineData}
                currentTime={currentTime}
                onTimeChange={setCurrentTime}
              />
            ) : (
              <div className="placeholder">
                <p>Timeline visualization will appear here</p>
                <p>Load a timeline.json file to get started</p>
                <p>Or run: <code>codevis analyze ./your-repo</code></p>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;