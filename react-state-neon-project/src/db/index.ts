import { neon } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-http';

import * as schema from './schema';

// Initialize Neon serverless database connection
// Uses Neon's HTTP API which is safe for browser use (not raw PostgreSQL protocol)
// The REACT_APP_ prefix makes this available in the React build process
const sql = neon(process.env.REACT_APP_DATABASE_URL!);

// Create Drizzle ORM instance with our schema for type-safe database operations
export const db = drizzle(sql, { schema });