import { useState, useEffect } from 'react';
import './App.css';

export default function App() {
  return (
    <>
      <h1>Click Per Second</h1>
      <MyCPSButton />
    </>
  );
}

function MyCPSButton() {
  const [count, setCount] = useState(0);

  const [time, setTime] = useState(0);

  // state to check stopwatch running or not
  const [isRunning, setIsRunning] = useState(false);

  const [cps, setCps] = useState(0);

  useEffect(() => {
    let intervalId;
    if (isRunning) {
      // setting time from 0 to 1 every 10 milisecond using javascript setInterval method
      intervalId = setInterval(() => setTime(time + 1), 10);
      setCps(count / seconds);
      if (seconds == 5) {
        setIsRunning(false);
        setTime(0);
        setCount(0);
      }
    } else {
      setCps(0);
    }
    return () => clearInterval(intervalId);
  }, [isRunning, time]);

  // Seconds calculation
  const seconds = Math.floor((time % 6000) / 100);

  // Milliseconds calculation
  const milliseconds = time % 100;

  const startCPS = () => {
    if (isRunning == true) {
      setCount(count + 1);
    } else {
      setIsRunning(true);
    }
  };

  return (
    <>
      <button onClick={startCPS}>Click's {count}</button>
      <p>CPS: {cps}</p>
      <p>
        {seconds.toString().padStart(2, '0')}:
        {milliseconds.toString().padStart(2, '0')}
      </p>

      <button
        onClick={() => {
          setTime(0);
        }}>
        Reset
      </button>
    </>
  );
}
