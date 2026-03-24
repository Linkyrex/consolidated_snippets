# @workspace/api-client-react

Generated React Query hooks for the API Showcase Hub.

## Installation

This package is part of the pnpm workspace:

```bash
pnpm install
```

## Peer Dependencies

This package requires React 18+ as a peer dependency:

```bash
pnpm add react@^18 react-dom@^18 @tanstack/react-query
```

## Usage

```typescript
import { useGetUsers, useCreateUser } from '@workspace/api-client-react';

function Users() {
  const { data, isLoading } = useGetUsers();
  const createUser = useCreateUser();

  if (isLoading) return <div>Loading...</div>;

  return (
    <ul>
      {data?.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

## Regeneration

Hooks are generated from the OpenAPI spec using Orval. To regenerate:

```bash
pnpm --filter @workspace/api-spec run codegen
```

## Features

- Type-safe React Query hooks
- Automatic request/response typing
- Optimistic updates support
- Mutation helpers