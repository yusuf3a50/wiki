
import React, { useState } from 'react';

// Simple React component demonstrating state management with server-side database persistence
function App() {
  // State variable to track button click count locally
  const [count, setCount] = useState(0);

  // Function to handle button click and increment the counter
  const handleIncrement = async () => {
    setCount(count + 1);
    
    // Call serverless function to record button press in database
    // This keeps database credentials secure on the server-side
    try {
      const response = await fetch('/.netlify/functions/record-button-press', {
        method: 'POST',
      });
      
      if (!response.ok) {
        throw new Error('Failed to record button press');
      }
      
      const data = await response.json();
      console.log('Button press recorded:', data);
    } catch (error) {
      console.error('Error recording button press:', error);
    }
  };

  return (
    <div className="App" style={{ textAlign: 'center', marginTop: '2rem' }}>
      <h1>Simple React State Example</h1>
      <p>The current count is: <strong>{count}</strong></p>
      <button onClick={handleIncrement}>Increment</button>
      <div style={{ marginTop: '2rem', color: '#888' }}>
        <p>The frontend demonstrates how to use <code>useState</code> to manage state in a React component.</p>
        <p>The backend handles Neon database interactions logging the times of when the button is pressed.</p>
        <p>The database implementation uses serverless functions, allowing you to persist data without exposing credentials on the client-side.</p>
      </div>
    </div>
  );
}

export default App;
