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

Pass `--save` to also add `cool-pkg` to the `dependencies` field of your app's package.json, with a version specifier that tells Bun to load from the registered local directory instead of installing from `npm`:

```bash
bun link --save cool-pkg
```

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

## Linking a directory by path

`link:` also accepts a path, as in Yarn and pnpm. The path is relative to the `package.json` that declares it, and Bun installs a symlink to that directory. Nothing has to be registered with `bun link` first.

**File:** `package.json`
```json
{
  "dependencies": {
    "design-tokens": "link:./vendor/design-tokens",
    "shared": "link:../shared"
  }
}
```

- Anything that is not a package name is a path: `link:./dir`, `link:../dir`, `link:vendor/dir`, an absolute path. `link:dir` and `link:@scope/dir` are names registered with `bun link`; write `link:./dir` for the directory.
- The directory must exist. It does not need a `package.json`.
- The directory's own dependencies are not installed. Use `file:` for a copy whose dependencies are installed, or make the directory a [workspace](/pm/workspaces).
- Only your project may use a path: the root `package.json`, a workspace, a `file:` directory one of them depends on, or a top-level `overrides` / `resolutions` entry. `bun install` fails when a package from the registry, git or a tarball declares one, so replace a `link:` path before you publish a package.

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

---

# CLI Usage

```bash
bun link <packages>
```

### Installation Scope

### `--global`

Type: `boolean`
Has no effect: `bun link` always registers packages in the global folder. Alias: `-g`

### Dependency Management

### `--production`

Type: `boolean`
Don't install devDependencies. Alias: `-p`

### `--omit`

Type: `string`
Exclude `dev`, `optional`, or `peer` dependencies from install

### Project Files & Lockfiles

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

### `--no-save`

Type: `boolean`
Don't update `package.json` or save a lockfile (the default)

### `--save`

Type: `boolean`
Update `package.json` and save a lockfile (false by default)

### `--trust`

Type: `boolean`
Add to `trustedDependencies` in the project's `package.json` and install the package(s)

### Installation Control

### `--force`

Type: `boolean`
Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

### `--no-verify`

Type: `boolean`
Skip verifying integrity of newly downloaded packages

### `--backend`

Type: `string`
Platform-specific optimizations for installing dependencies. One of `clonefile`, `hardlink`,{" "}
`symlink`, or `copyfile`

### `--linker`

Type: `string`
Linker strategy (one of `isolated` or `hoisted`)

### `--dry-run`

Type: `boolean`
With `bun link <package>`, resolve but don't install packages, update `package.json`, or
save a lockfile. Has no effect on bare `bun link`, which still registers the current package

### `--ignore-scripts`

Type: `boolean`
Skip lifecycle scripts for all packages, including the project's `package.json` and trusted dependencies

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
Use a specific registry by default, overriding `.npmrc`, `bunfig.toml`, and environment
variables

### `--network-concurrency`

Type: `number`; Default: `64`
Maximum number of concurrent network requests

### Performance & Resource

### `--concurrent-scripts`

Type: `number`
Maximum number of concurrent jobs for lifecycle scripts (default: 2x CPU cores)

### Caching

### `--cache-dir`

Type: `string`
Store & load cached data from a specific directory path

### `--no-cache`

Type: `boolean`
Ignore manifest cache entirely

### Output & Logging

### `--silent`

Type: `boolean`
Don't log anything

### `--quiet`

Type: `boolean`
Disable the progress bar

### `--verbose`

Type: `boolean`
Excessively verbose logging

### `--no-progress`

Type: `boolean`
Disable the progress bar

### `--no-summary`

Type: `boolean`
Don't print a summary

### Platform Targeting

### `--cpu`

Type: `string`
Override CPU architecture for optional dependencies (e.g., `x64`, `arm64`, `*` for
all)

### `--os`

Type: `string`
Override operating system for optional dependencies (e.g., `linux`, `darwin`, `*` for
all)

### `--libc`

Type: `string`
Override libc for optional dependencies (e.g., `glibc`, `musl`, `*` for all)

### Global Configuration & Context

### `--config`

Type: `string`
Specify path to config file (`bunfig.toml`). Alias: `-c`

### `--cwd`

Type: `string`
Set a specific current working directory

### `--env-file`

Type: `string`
Load environment variables from the specified file(s)

### `--no-env-file`

Type: `boolean`
Disable automatic loading of .env files

### Help

### `--help`

Type: `boolean`
Print this help menu. Alias: `-h`
