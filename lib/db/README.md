# @workspace/db

Drizzle ORM schema definitions and PostgreSQL client for the API Showcase Hub.

## Installation

This package is part of the pnpm workspace. Install dependencies from the root:

```bash
pnpm install
```

## Usage

### Database Client

```typescript
import { db } from '@workspace/db';

const result = await db.query.users.findMany();
```

### Schema

Import schema types directly:

```typescript
import { users, posts } from '@workspace/db/schema';
```

## Scripts

| Script | Description |
|--------|-------------|
| `pnpm run push` | Push schema to database (development) |
| `pnpm run push-force` | Force push (drops tables) |

## Environment

Requires `DATABASE_URL` environment variable with a PostgreSQL connection string.

## Dependencies

- `drizzle-orm` - SQL query builder
- `drizzle-zod` - Zod schema generation from Drizzle
- `pg` - PostgreSQL driver
- `zod` - Schema validation