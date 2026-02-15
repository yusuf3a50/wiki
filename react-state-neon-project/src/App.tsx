
import React, { useState } from 'react';
import { db } from './db';
import { buttonPresses } from './db/schema';

// This is a simple React component demonstrating state management using useState.
// It displays a counter and a button to increment the counter.
function App() {
  // Declare a state variable 'count' and a function to update it, 'setCount'.
  // The initial value of 'count' is 0.
  const [count, setCount] = useState(0);

  // Function to handle button click and increment the counter
  const handleIncrement = async () => {
    setCount(count + 1);
    
    // Record the button press to the database with automatic timestamp
    // The empty values object uses the default timestamp from the schema
    try {
      await db.insert(buttonPresses).values({});
      console.log('Button press recorded in database');
    } catch (error) {
      console.error('Error recording button press:', error);
    }
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
