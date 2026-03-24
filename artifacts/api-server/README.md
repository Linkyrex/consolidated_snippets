# @workspace/api-server

Express 5 REST API server for the API Showcase Hub.

## Installation

Part of the pnpm workspace. From the root:

```bash
pnpm install
```

## Quick Start

```bash
# Development with hot reload
pnpm --filter @workspace/api-server run dev

# Production build
pnpm --filter @workspace/api-server run build

# Start production server
pnpm --filter @workspace/api-server start
```

## Scripts

| Script | Description |
|--------|-------------|
| `dev` | Start development server with hot reload |
| `build` | Build for production |
| `start` | Start production server |
| `typecheck` | Type-check the project |

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `3000` |
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `NODE_ENV` | Environment | `development` |

## API Endpoints

### GET /api/health

Health check endpoint.

```bash
curl http://localhost:3000/api/health
```

### GET /api/users

List all users (requires database).

## Tech Stack

- Express 5
- TypeScript
- Drizzle ORM
- Zod validation