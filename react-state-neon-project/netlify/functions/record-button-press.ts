// Netlify serverless function to record button presses
// This runs server-side, keeping database credentials secure

import type { Handler } from '@netlify/functions';
import { neon } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-http';
import { buttonPresses } from '../../src/db/schema';

// Initialize database connection using server-side environment variable
// DATABASE_URL (without REACT_APP_ prefix) is only accessible server-side
const sql = neon(process.env.DATABASE_URL!);
const db = drizzle(sql);

export const handler: Handler = async () => {
  try {
    // Insert new button press with automatic timestamp from schema defaults
    const result = await db.insert(buttonPresses).values({}).returning();
    
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ success: true, data: result[0] }),
    };
  } catch (error) {
    console.error('Database error:', error);
    
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        success: false, 
        error: 'Failed to record button press' 
      }),
    };
  }
};
