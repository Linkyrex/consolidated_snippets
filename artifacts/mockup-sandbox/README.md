# @workspace/mockup-sandbox

Testing environment for API mockups and prototypes.

## Installation

Part of the pnpm workspace:

```bash
pnpm install
```

## Quick Start

```bash
# Development
pnpm --filter @workspace/mockup-sandbox run dev

# Build
pnpm --filter @workspace/mockup-sandbox run build
```

## Purpose

This package provides a sandbox environment for:
- Testing API designs before implementation
- Creating visual mockups
- Rapid prototyping

## Configuration

Update `vite.config.ts` to configure the mock server and API endpoints.

## Tech Stack

- Vite
- React 18
- TypeScript