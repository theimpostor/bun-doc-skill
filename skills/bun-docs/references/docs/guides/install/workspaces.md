# Configuring a monorepo using workspaces
Source: https://bun.com/docs/guides/install/workspaces


Bun's package manager supports npm `"workspaces"`. Workspaces split a codebase into distinct packages that live in the same repository, can depend on each other, and (when possible) share a `node_modules` directory.

Clone [this sample project](https://github.com/colinhacks/bun-workspaces) to experiment with workspaces.

***

The root `package.json` should not contain `"dependencies"`, `"devDependencies"`, or other dependency fields. Each package should be self-contained and declare its own dependencies. It's conventional to declare `"private": true` to avoid accidentally publishing the root package to `npm`.

**File:** `package.json`
```json
{
  "name": "my-monorepo",
  "private": true,
  "workspaces": ["packages/*"]
}
```

***

It's common to place all packages in a `packages` directory. The `"workspaces"` field in `package.json` supports glob patterns, so `packages/*` treats each subdirectory of `packages` as a separate *package* (also known as a workspace).

**File:** `File`
```txt
.
├── package.json
├── node_modules
└── packages
    ├── stuff-a
    │   └── package.json
    └── stuff-b
        └── package.json
```

***

To add dependencies between workspaces, use the `"workspace:*"` syntax. The following adds `stuff-a` as a dependency of `stuff-b`.

**File:** `packages/stuff-b/package.json`
```json
{
  "name": "stuff-b",
  "dependencies": {
    "stuff-a": "workspace:*"
  }
}
```

***

Once you add the dependency, run `bun install` from the project root to install dependencies for all workspaces.

```sh
bun install
```

***

To add npm dependencies to a particular workspace, `cd` to that directory and run `bun add` as you normally would. Bun detects that you are in a workspace, adds the dependency to that workspace's `package.json`, and updates the root lockfile. New workspaces use [isolated installs](/docs/pm/isolated-installs) by default, so Bun installs the package into the root `node_modules/.bun` store and symlinks it from the workspace's own `node_modules`. With `--linker hoisted`, Bun hoists the package into the root `node_modules` instead.

```sh
cd packages/stuff-a
bun add zod
```

***

See [`bun install`](/docs/pm/cli/install).
