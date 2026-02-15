import { integer, pgTable, varchar, text, timestamp } from 'drizzle-orm/pg-core';

export const posts = pgTable('posts', {
    id: integer().primaryKey().generatedAlwaysAsIdentity(),
    title: varchar({ length: 255 }).notNull(),
    content: text().notNull().default('')
});

export const buttonPresses = pgTable('button_presses', {
    id: integer().primaryKey().generatedAlwaysAsIdentity(),
    timestamp: timestamp().notNull().defaultNow()
});