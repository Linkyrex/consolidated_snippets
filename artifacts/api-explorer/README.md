# @workspace/api-explorer

Interactive API documentation UI built with Vite.

## Installation

Part of the pnpm workspace:

```bash
pnpm install
```

## Quick Start

```bash
# Development
pnpm --filter @workspace/api-explorer run dev

# Build for production
pnpm --filter @workspace/api-explorer run build

# Preview production build
pnpm --filter @workspace/api-explorer run preview
```

## Configuration

The API endpoint is configured in `vite.config.ts`. Update `VITE_API_URL` to point to your API server.

## Features

- Interactive API documentation
- Request/response exploration
- Schema viewer
- Dark mode support

## Tech Stack

- Vite
- React 18
- TypeScript