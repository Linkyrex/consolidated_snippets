# @workspace/api-zod

Generated Zod schemas from the OpenAPI specification.

## Installation

This package is part of the pnpm workspace:

```bash
pnpm install
```

## Usage

Import generated schemas:

```typescript
import { User, Post, CreateUserSchema } from '@workspace/api-zod';

// Validate data
const validData = CreateUserSchema.parse(req.body);
```

## Regeneration

Schemas are generated from the OpenAPI spec using Orval. To regenerate:

```bash
pnpm --filter @workspace/api-spec run codegen
```

## Generated Types

This package contains type-safe Zod schemas for:
- Request/response validation
- API data types
- OpenAPI components