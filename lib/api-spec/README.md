# @workspace/api-spec

OpenAPI 3.1 specification and Orval configuration for the API Showcase Hub.

## Installation

This package is part of the pnpm workspace:

```bash
pnpm install
```

## OpenAPI Specification

The OpenAPI spec is defined in `openapi.yaml`. It describes:
- REST endpoints
- Request/response schemas
- Authentication requirements
- API metadata

## Code Generation

Run Orval to generate Zod schemas and React Query hooks:

```bash
pnpm run codegen
```

This generates:
- `@workspace/api-zod` - Type-safe Zod schemas
- `@workspace/api-client-react` - React Query hooks

## Viewing the API

Start the API server and visit `/api/docs` for the interactive Swagger UI:

```bash
pnpm --filter @workspace/api-server run dev
```

## Editing the Spec

The spec uses OpenAPI 3.1 format. Example endpoint:

```yaml
/users:
  get:
    summary: List users
    responses:
      '200':
        description: List of users
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/User'
```