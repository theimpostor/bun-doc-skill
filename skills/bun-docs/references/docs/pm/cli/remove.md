# bun remove
Source: https://bun.com/docs/pm/cli/remove

Remove dependencies from your project

## Basic Usage

> Note: **Alias** — `bun rm`, `bun uninstall`, `bun r`

```bash
bun remove ts-node
```

Bun removes the package from every dependency group in `package.json` that lists it and updates `bun.lock`. Once nothing else depends on the package, Bun deletes it from `node_modules`.

## `--filter`

> Note: **Alias** — `-F`

In a monorepo, remove the package from the matching workspace(s) instead of the current directory's package, using the same patterns as [`bun add --filter`](/docs/pm/cli/add#--filter). Use `--filter '*'` to remove it from every workspace package. Workspaces that don't list the package are left untouched.

```bash
bun remove zod --filter api
bun remove zod --filter '*'
```

***

## CLI Usage

```bash
bun remove <package>
```

### General Information

- (boolean) Print this help menu. Alias: `-h`

### Configuration

- (string) Specify path to config file (`bunfig.toml`). Alias: `-c`

### Package.json Interaction

- (boolean) Don't update `package.json` or save a lockfile

- (boolean) Save to `package.json` (true by default)

- (boolean) Add to `trustedDependencies` in the project's `package.json` and install the package(s)

- (string) Remove the package(s) from the matching workspaces instead of the current package. Alias: `-F`

### Lockfile Behavior

- (boolean) Write a `yarn.lock` file (yarn v1). Alias: `-y`

- (boolean) Disallow changes to lockfile

- (boolean) Save a text-based lockfile

- (boolean) Generate a lockfile without installing dependencies

### Dependency Filtering

- (boolean) Don't install devDependencies. Alias: `-p`

- (string) Exclude `dev`, `optional`, or `peer` dependencies from install

### Network & Registry

- (string) Provide a Certificate Authority signing certificate

- (string) Same as `--ca`, but as a file path to the certificate

- (string) Use a specific registry by default, overriding `.npmrc`, `bunfig.toml` and environment variables

### Execution Control & Validation

- (boolean) Perform a dry run without making changes

- (boolean) Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

- (boolean) Skip verifying integrity of newly downloaded packages

### Output & Logging

- (boolean) Don't log anything

- (boolean) Excessively verbose logging

- (boolean) Disable the progress bar

- (boolean) Don't print a summary

### Caching

- (string) Store & load cached data from a specific directory path

- (boolean) Ignore manifest cache entirely

### Script Execution

- (boolean) Skip lifecycle scripts for all packages, including the project's `package.json` and trusted dependencies

- (number) Maximum number of concurrent jobs for lifecycle scripts (default: 2x CPU cores)

### Scope & Path

- (boolean) Install globally. Alias: `-g`

- (string) Set a specific cwd

### Advanced & Performance

- (string) Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default on macOS), `hardlink` (default on Linux and Windows), `symlink`, `copyfile`

- (number) Maximum number of concurrent network requests (default 48)
