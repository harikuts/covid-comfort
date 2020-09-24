import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(1);

  useEffect(() => {
    fetch('/cc').then(res => res.text()).then(data => {
      setCurrentTime(data);
    });
  }, []);

  // useEffect(() => {
  //   fetch('/').then(res => res.text()).then(data => {
  //     setCurrentTime(data);
  //   });
  // });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>{currentTime}</p>
      </header>
    </div>
  );
}

export default App;
