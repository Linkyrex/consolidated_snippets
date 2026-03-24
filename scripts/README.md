# @workspace/scripts

Utility scripts for the API Showcase Hub monorepo.

## Installation

Part of the pnpm workspace:

```bash
pnpm install
```

## Usage

Run scripts from the root using pnpm filter:

```bash
pnpm --filter @workspace/scripts run <script-name>
```

## Available Scripts

Check `src/` directory for available scripts.

## Post-Install Hook

The `post-merge.sh` hook runs automatically after `git merge` or `pnpm install` to ensure dependencies are up to date.