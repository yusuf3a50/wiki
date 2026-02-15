/// <reference types="node" />
// Add a reference to Node types so `process.env` is recognized by TypeScript in this config file.
// This is a minimal local fix that avoids changing tsconfig or requiring an immediate dev-dependency install.

import { defineConfig } from 'drizzle-kit';

export default defineConfig({
    dialect: 'postgresql',
    dbCredentials: {
        url: process.env.DATABASE_URL!
    },
    schema: './src/db/schema.ts',
    /**
     * Never edit the migrations directly, only use drizzle.
     * There are scripts in the package.json "db:generate" and "db:migrate" to handle this.
     */
    out: './migrations'
});
