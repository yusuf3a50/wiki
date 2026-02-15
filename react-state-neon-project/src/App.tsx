
import React, { useState } from 'react';

// This is a simple React component demonstrating state management using useState.
// It displays a counter and a button to increment the counter.
function App() {
  // Declare a state variable 'count' and a function to update it, 'setCount'.
  // The initial value of 'count' is 0.
  const [count, setCount] = useState(0);

  // Function to handle button click and increment the counter
  const handleIncrement = () => {
    setCount(count + 1);
  };

  return (
    <div className="App" style={{ textAlign: 'center', marginTop: '2rem' }}>
      <h1>Simple React State Example</h1>
      <p>The current count is: <strong>{count}</strong></p>
      <button onClick={handleIncrement}>Increment</button>
      <p style={{ marginTop: '2rem', color: '#888' }}>
        (This demonstrates how to use <code>useState</code> to manage state in a React component.)
      </p>
    </div>
  );
}

export default App;
