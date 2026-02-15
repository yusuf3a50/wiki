# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

## Setup Instructions

### Database Setup

This project uses [Neon](https://neon.tech) serverless PostgreSQL with Drizzle ORM and Netlify Functions.

```bash
# Install dependencies
npm install

# Link to Netlify project
npx netlify link

# Initialize Neon database
npx netlify db init

# Run migrations to create tables
npm run db:migrate:manual

# Verify tables were created
npm run db:verify
```

### Environment Variables

Create a `.env.local` file with your Neon database URL:

```bash
DATABASE_URL="postgresql://user:password@host/database?sslmode=require"
```

**Important:** Also set `DATABASE_URL` in Netlify UI under Site Settings → Environment Variables.

**Security Note:** This project uses serverless functions to keep database credentials secure:
- The React app never accesses the database directly
- Database operations happen server-side via Netlify Functions
- `DATABASE_URL` (without `REACT_APP_` prefix) is never exposed to the browser

### Local Development

```bash
# Start development server with Netlify Functions
netlify dev
```

This starts both the React app and Netlify Functions locally.

### Database Scripts

- `npm run db:generate` - Generate new migrations from schema changes
- `npm run db:migrate` - Run migrations (via Netlify)
- `npm run db:migrate:manual` - Run migrations directly
- `npm run db:verify` - Check which tables exist in the database
