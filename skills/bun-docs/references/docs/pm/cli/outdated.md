# bun outdated
Source: https://bun.com/docs/pm/cli/outdated

Check for outdated dependencies

`bun outdated` displays a table of the dependencies in your project that have newer versions available.

```sh
bun outdated
```

```txt
| Package                        | Current | Update    | Latest     |
| ------------------------------ | ------- | --------- | ---------- |
| @sinclair/typebox              | 0.34.15 | 0.34.16   | 0.34.16    |
| @types/bun (dev)               | 1.3.0   | 1.3.3     | 1.3.3      |
| eslint (dev)                   | 8.57.1  | 8.57.1    | 9.20.0     |
| eslint-plugin-security (dev)   | 2.1.1   | 2.1.1     | 3.0.1      |
| eslint-plugin-sonarjs (dev)    | 0.23.0  | 0.23.0    | 3.0.1      |
| expect-type (dev)              | 0.16.0  | 0.16.0    | 1.1.0      |
| prettier (dev)                 | 3.4.2   | 3.5.0     | 3.5.0      |
| tsup (dev)                     | 8.3.5   | 8.3.6     | 8.3.6      |
| typescript (dev)               | 5.7.2   | 5.7.3     | 5.7.3      |

```

## Version Information

The output table shows three version columns:

* **Current**: The version currently installed
* **Update**: The latest version that satisfies your package.json version range
* **Latest**: The latest version published to the registry

### Dependency Filters

To check a specific dependency, pass its name as a positional argument:

```sh
bun outdated eslint-plugin-security
```

```txt
| Package                        | Current | Update | Latest    |
| ------------------------------ | ------- | ------ | --------- |
| eslint-plugin-security (dev)   | 2.1.1   | 2.1.1  | 3.0.1     |

```

Glob patterns work too:

```sh
bun outdated 'eslint*'
```

```txt
| Package                        | Current | Update | Latest     |
| ------------------------------ | ------- | ------ | ---------- |
| eslint (dev)                   | 8.57.1  | 8.57.1 | 9.20.0     |
| eslint-plugin-security (dev)   | 2.1.1   | 2.1.1  | 3.0.1      |
| eslint-plugin-sonarjs (dev)    | 0.23.0  | 0.23.0 | 3.0.1      |
```

For example, to check for outdated `@types/*` packages:

```sh
bun outdated '@types/*'
```

```txt
| Package            | Current | Update | Latest |
| ------------------ | ------- | ------ | ------ |
| @types/bun (dev)   | 1.3.0   | 1.3.3  | 1.3.3 |
```

Or to exclude all `@types/*` packages:

```sh
bun outdated '!@types/*'
```

```txt
| Package                        | Current | Update    | Latest     |
| ------------------------------ | ------- | --------- | ---------- |
| @sinclair/typebox              | 0.34.15 | 0.34.16   | 0.34.16    |
| eslint (dev)                   | 8.57.1  | 8.57.1    | 9.20.0     |
| eslint-plugin-security (dev)   | 2.1.1   | 2.1.1     | 3.0.1      |
| eslint-plugin-sonarjs (dev)    | 0.23.0  | 0.23.0    | 3.0.1      |
| expect-type (dev)              | 0.16.0  | 0.16.0    | 1.1.0      |
| prettier (dev)                 | 3.4.2   | 3.5.0     | 3.5.0      |
| tsup (dev)                     | 8.3.5   | 8.3.6     | 8.3.6      |
| typescript (dev)               | 5.7.2   | 5.7.3     | 5.7.3      |
```

### Workspace Filters

Use the `--filter` flag to check for outdated dependencies in a different workspace package:

```sh
bun outdated --filter='@monorepo/types'
```

```txt
| Package            | Current | Update | Latest |
| ------------------ | ------- | ------ | ------ |
| tsup (dev)         | 8.3.5   | 8.3.6  | 8.3.6  |
| typescript (dev)   | 5.7.2   | 5.7.3  | 5.7.3  |
```

`--filter` accepts glob patterns to match multiple workspaces:

```sh
bun outdated --filter='@monorepo/{types,cli}'
```

```txt
| Package                        | Current | Update | Latest     |
| ------------------------------ | ------- | ------ | ---------- |
| eslint (dev)                   | 8.57.1  | 8.57.1 | 9.20.0     |
| eslint-plugin-security (dev)   | 2.1.1   | 2.1.1  | 3.0.1      |
| eslint-plugin-sonarjs (dev)    | 0.23.0  | 0.23.0 | 3.0.1      |
| expect-type (dev)              | 0.16.0  | 0.16.0 | 1.1.0      |
| tsup (dev)                     | 8.3.5   | 8.3.6  | 8.3.6      |
| typescript (dev)               | 5.7.2   | 5.7.3  | 5.7.3      |
```

### Catalog Dependencies

`bun outdated` also checks [catalog](/docs/pm/catalogs) dependencies defined in `package.json`:

```sh
bun outdated -r
```

```txt
┌────────────────────┬─────────┬─────────┬─────────┬────────────────────────────────┐
│ Package            │ Current │ Update  │ Latest  │ Workspace                      │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ body-parser        │ 1.19.0  │ 1.19.0  │ 2.2.0   │ @test/shared                   │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ cors               │ 2.8.0   │ 2.8.0   │ 2.8.5   │ @test/shared                   │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ chalk              │ 4.0.0   │ 4.0.0   │ 5.6.2   │ @test/utils                    │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ uuid               │ 8.0.0   │ 8.0.0   │ 13.0.0  │ @test/utils                    │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ axios              │ 0.21.0  │ 0.21.0  │ 1.12.2  │ catalog (@test/app)            │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ lodash             │ 4.17.15 │ 4.17.15 │ 4.17.21 │ catalog (@test/app)            │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ react              │ 17.0.0  │ 17.0.0  │ 19.1.1  │ catalog (@test/app)            │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ react-dom          │ 17.0.0  │ 17.0.0  │ 19.1.1  │ catalog (@test/app)            │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ express            │ 4.17.0  │ 4.17.0  │ 5.1.0   │ catalog (@test/shared)         │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ moment             │ 2.24.0  │ 2.24.0  │ 2.30.1  │ catalog (@test/utils)          │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ @types/node (dev)  │ 14.0.0  │ 14.0.0  │ 24.5.2  │ @test/shared                   │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ @types/react (dev) │ 17.0.0  │ 17.0.0  │ 19.1.15 │ catalog:testing (@test/app)    │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ eslint (dev)       │ 7.0.0   │ 7.0.0   │ 9.36.0  │ catalog:testing (@test/app)    │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ typescript (dev)   │ 4.9.5   │ 4.9.5   │ 5.9.2   │ catalog:build (@test/app)      │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ jest (dev)         │ 26.0.0  │ 26.0.0  │ 30.2.0  │ catalog:testing (@test/shared) │
├────────────────────┼─────────┼─────────┼─────────┼────────────────────────────────┤
│ prettier (dev)     │ 2.0.0   │ 2.0.0   │ 3.6.2   │ catalog:build (@test/utils)    │
└────────────────────┴─────────┴─────────┴─────────┴────────────────────────────────┘
```

***

## CLI Usage

```bash
bun outdated <filter>
```

### General Options

- (string) Specify path to config file (`bunfig.toml`)

- (string) Set a specific cwd

- (boolean) Print this help menu

- (string) Display outdated dependencies for each matching workspace

- (boolean) Check outdated packages in all workspaces

### Output & Logging

- (boolean) Don't log anything

- (boolean) Excessively verbose logging

- (boolean) Disable the progress bar

- (boolean) Don't print a summary

### Dependency Scope & Target

- (boolean) Don't install devDependencies

- (string) Exclude `dev`, `optional`, or `peer` dependencies from install

- (boolean) Install globally

### Lockfile & Package.json

- (boolean) Write a `yarn.lock` file (yarn v1)

- (boolean) Don't update `package.json` or save a lockfile

- (boolean) Save to `package.json` (true by default)

- (boolean) Disallow changes to lockfile

- (boolean) Save a text-based lockfile

- (boolean) Generate a lockfile without installing dependencies

- (boolean) Add to `trustedDependencies` in the project's `package.json` and install the package(s)

### Network & Registry

- (string) Provide a Certificate Authority signing certificate

- (string) Same as `--ca`, but as a file path to the certificate

- (string) Use a specific registry by default, overriding `.npmrc`, `bunfig.toml` and environment variables

- (number) Maximum number of concurrent network requests (default 48)

### Caching

- (string) Store & load cached data from a specific directory path

- (boolean) Ignore manifest cache entirely

### Execution Behavior

- (boolean) Perform a dry run without making changes

- (boolean) Always request the latest versions from the registry & reinstall all dependencies

- (boolean) Skip verifying integrity of newly downloaded packages

- (boolean) Skip lifecycle scripts for all packages, including the project's `package.json` and trusted dependencies

- (string) Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default on macOS), `hardlink` (default on Linux and Windows), `symlink`, `copyfile`

- (number) Maximum number of concurrent jobs for lifecycle scripts (default: 2x CPU cores)
