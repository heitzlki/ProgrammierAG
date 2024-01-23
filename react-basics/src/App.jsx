// import { useState, useEffect } from 'react';

// export default function MyCPSButton() {
//   const [count, setCount] = useState(0);
//   const [time, setTime] = useState(0);
//   const [isRunning, setIsRunning] = useState(false);
//   const [cps, setCps] = useState(0);
//   const [remainingTime, setRemainingTime] = useState(5);

//   useEffect(() => {
//     let intervalId;
//     if (isRunning) {
//       intervalId = setInterval(() => {
//         setTime((time) => time + 1);
//         setRemainingTime(5 - time / 100);
//         if (time >= 500) {
//           // 500 * 10ms = 5 seconds
//           clearInterval(intervalId);
//           setCps(count / 5);
//           setIsRunning(false);
//           setTime(0);
//         }
//       }, 10);
//     }
//     return () => clearInterval(intervalId);
//   }, [isRunning, time, count]);

//   const buttonStyle = {
//     padding: '10px 20px',
//     margin: '10px',
//     fontSize: '16px',
//     borderRadius: '5px',
//     border: 'none',
//     backgroundColor: '#646cff',
//     color: 'white',
//     cursor: 'pointer',
//   };

//   return (
//     <div
//       style={{
//         display: 'flex',
//         flexDirection: 'column',
//         justifyContent: 'center',
//         alignItems: 'center',
//         backgroundColor: '#F8F9FA',
//         height: '100vh',
//         width: '100vw',
//       }}>
//       <button
//         onClick={() => {
//           setCount(0);
//           setIsRunning(true);
//         }}
//         style={buttonStyle}
//         disabled={isRunning}>
//         Start
//       </button>
//       <button
//         onClick={() => setCount((count) => count + 1)}
//         style={{
//           ...buttonStyle,
//           backgroundColor: '#61dafb',
//           padding: '40px 60px',
//         }}
//         disabled={!isRunning}>
//         {count}
//       </button>
//       <p>CPS: {cps}</p>
//       <p>Remaining Time: {remainingTime.toFixed(2)} seconds</p>
//     </div>
//   );
// }
import { useState } from 'react';

function MeineZahl({ dieZahl = 1 }) {
  return <p style={{ fontSize: '100px' }}>{dieZahl}</p>;
}

function MeinKnop({ gedrueckt = () => {} }) {
  return (
    <button
      onClick={() => {
        gedrueckt();
      }}>
      Knopf
    </button>
  );
}

function App() {
  const [counter, setCounter] = useState(0);

  const rechner = (x, y) => {
    return x * y;
  };

  const design = {
    backgroundColor: 'red',
    width: '100vw',
    height: '100vh',
  };

  const schriftDesign = {
    backgroundColor: 'green',
    fontSize: `${counter}px`,
  };

  return (
    <div style={design}>
      <h1>My App</h1>
      <MeinKnop
        gedrueckt={() => {
          setCounter(counter + 1);
        }}
      />
      <MeinKnop
        gedrueckt={() => {
          setCounter(counter + 1);
        }}
      />
      <MeinKnop
        gedrueckt={() => {
          setCounter(counter + 1);
        }}
      />
      <MeineZahl dieZahl={counter} />
      {[1, 2, 3].map(() => {
        return <p>aa</p>;
      })}
    </div>
  );
}

export default App;
