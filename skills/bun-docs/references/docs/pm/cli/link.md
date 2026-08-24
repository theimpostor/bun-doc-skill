# bun link
Source: https://bun.com/docs/pm/cli/link

Link local packages for development

Use `bun link` in a local directory to register the current package as a "linkable" package.

```bash
cd /path/to/cool-pkg
cat package.json
bun link
```

```txt
bun link v1.3.3 (7416672e)
Success! Registered "cool-pkg"

To use cool-pkg in a project, run:
  bun link cool-pkg

Or add it in dependencies in your package.json file:
  "cool-pkg": "link:cool-pkg"
```

You can now "link" this package into other projects using `bun link cool-pkg`. This command creates a symlink in the target project's `node_modules` directory pointing to the local directory.

```bash
cd /path/to/my-app
bun link cool-pkg
```

The `--save` flag also adds `cool-pkg` to the `dependencies` field of your app's package.json, with a version specifier that tells Bun to load from the registered local directory instead of installing from `npm`:

**File:** `package.json`
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "dependencies": {
    "cool-pkg": "link:cool-pkg"
  }
}
```

## Unlinking

Use `bun unlink` in the root directory to unregister a local package.

```bash
cd /path/to/cool-pkg
bun unlink
```

```txt
bun unlink v1.3.3 (7416672e)
success: unlinked package "cool-pkg"
```

***

# CLI Usage

```bash
bun link <packages>
```

### Installation Scope

- (boolean) Install globally. Alias: `-g`

### Dependency Management

- (boolean) Don't install devDependencies. Alias: `-p`

- (string) Exclude `dev`, `optional`, or `peer` dependencies from install

### Project Files & Lockfiles

- (boolean) Write a `yarn.lock` file (yarn v1). Alias: `-y`

- (boolean) Disallow changes to lockfile

- (boolean) Save a text-based lockfile

- (boolean) Generate a lockfile without installing dependencies

- (boolean) Don't update `package.json` or save a lockfile

- (boolean) Save to `package.json`

- (boolean) Add to `trustedDependencies` in the project's `package.json` and install the package(s)

### Installation Control

- (boolean) Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

- (boolean) Skip verifying integrity of newly downloaded packages

- (string) Platform-specific optimizations for installing dependencies. One of `clonefile`, `hardlink`, `symlink`, or `copyfile`

- (string) Linker strategy (one of `isolated` or `hoisted`)

- (boolean) Perform a dry run without making changes

- (boolean) Skip lifecycle scripts for all packages, including the project's `package.json` and trusted dependencies

### Network & Registry

- (string) Provide a Certificate Authority signing certificate

- (string) Same as `--ca`, but as a file path to the certificate

- (string) Use a specific registry by default, overriding `.npmrc`, `bunfig.toml`, and environment variables

- (number) Maximum number of concurrent network requests

### Performance & Resource

- (number) Maximum number of concurrent jobs for lifecycle scripts (default: 2x CPU cores)

### Caching

- (string) Store & load cached data from a specific directory path

- (boolean) Ignore manifest cache entirely

### Output & Logging

- (boolean) Don't log anything

- (boolean) Disable the progress bar

- (boolean) Excessively verbose logging

- (boolean) Disable the progress bar

- (boolean) Don't print a summary

### Platform Targeting

- (string) Override CPU architecture for optional dependencies (e.g., `x64`, `arm64`, `*` for all)

- (string) Override operating system for optional dependencies (e.g., `linux`, `darwin`, `*` for all)

### Global Configuration & Context

- (string) Specify path to config file (`bunfig.toml`). Alias: `-c`

- (string) Set a specific current working directory

### Help

- (boolean) Print this help menu. Alias: `-h`
