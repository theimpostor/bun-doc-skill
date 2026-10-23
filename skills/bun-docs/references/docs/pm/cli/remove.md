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

In a monorepo, remove the package from the matching workspace(s) instead of the current directory's package, using the same patterns as [`bun add --filter`](/pm/cli/add#--filter). Use `--filter '*'` to remove it from every workspace package. Workspaces that don't list the package are left untouched.

```bash
bun remove zod --filter api
bun remove zod --filter '*'
```

---

## CLI Usage

```bash
bun remove <package>
```

### General Information

### `--help`

Type: `boolean`
Print this help menu. Alias: `-h`

### Configuration

### `--config`

Type: `string`
Specify path to config file (`bunfig.toml`). Alias: `-c`

### Package.json Interaction

### `--no-save`

Type: `boolean`
Don't update `package.json` or save a lockfile

### `--save`

Type: `boolean`; Default: `true`
Save to `package.json` (true by default)

### `--trust`

Type: `boolean`
Add to `trustedDependencies` in the project's `package.json` and install the package(s)

### `--filter`

Type: `string`
Remove the package(s) from the matching workspaces instead of the current package. Alias: `-F`

### Lockfile Behavior

### `--yarn`

Type: `boolean`
Write a `yarn.lock` file (yarn v1). Alias: `-y`

### `--frozen-lockfile`

Type: `boolean`
Disallow changes to lockfile

### `--save-text-lockfile`

Type: `boolean`
Save a text-based lockfile

### `--lockfile-only`

Type: `boolean`
Generate a lockfile without installing dependencies

### Dependency Filtering

### `--production`

Type: `boolean`
Don't install devDependencies. Alias: `-p`

### `--omit`

Type: `string`
Exclude `dev`, `optional`, or `peer` dependencies from install

### Network & Registry

### `--ca`

Type: `string`
Provide a Certificate Authority signing certificate

### `--cafile`

Type: `string`
Same as `--ca`, but as a file path to the certificate

### `--use-system-ca`

Type: `boolean`
Use the system's trusted certificate authorities

### `--registry`

Type: `string`
Use a specific registry by default, overriding `.npmrc`, `bunfig.toml` and environment variables

### Execution Control & Validation

### `--dry-run`

Type: `boolean`
Resolve the change but don't remove packages, update `package.json`, save a lockfile, or run the project's
lifecycle scripts

### `--force`

Type: `boolean`
Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

### `--no-verify`

Type: `boolean`
Skip verifying integrity of newly downloaded packages

### Output & Logging

### `--silent`

Type: `boolean`
Don't log anything

### `--verbose`

Type: `boolean`
Excessively verbose logging

### `--no-progress`

Type: `boolean`
Disable the progress bar

### `--no-summary`

Type: `boolean`
Don't print a summary

### Caching

### `--cache-dir`

Type: `string`
Store & load cached data from a specific directory path

### `--no-cache`

Type: `boolean`
Ignore manifest cache entirely

### Script Execution

### `--ignore-scripts`

Type: `boolean`
Skip lifecycle scripts for all packages, including the project's `package.json` and trusted dependencies

### `--concurrent-scripts`

Type: `number`
Maximum number of concurrent jobs for lifecycle scripts (default: 2x CPU cores)

### Scope & Path

### `--global`

Type: `boolean`
Install globally. Alias: `-g`

### `--cwd`

Type: `string`
Set a specific cwd

### `--env-file`

Type: `string`
Load environment variables from the specified file(s)

### `--no-env-file`

Type: `boolean`
Disable automatic loading of .env files

### Advanced & Performance

### `--backend`

Type: `string`
Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default on
macOS), `hardlink` (default on Linux and Windows), `symlink`, `copyfile`

### `--network-concurrency`

Type: `number`; Default: `64`
Maximum number of concurrent network requests (default 64)
