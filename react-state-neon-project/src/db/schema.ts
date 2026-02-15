import { integer, pgTable, timestamp } from 'drizzle-orm/pg-core';

// Table to track button presses with auto-incrementing ID and timestamp
export const buttonPresses = pgTable('button_presses', {
    id: integer().primaryKey().generatedAlwaysAsIdentity(),
    timestamp: timestamp().notNull().defaultNow()
});