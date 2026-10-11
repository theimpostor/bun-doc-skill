# bun patch
Source: https://bun.com/docs/pm/cli/patch

Persistently patch node_modules packages in a git-friendly way


`bun patch` persistently patches packages in `node_modules` in a maintainable, git-friendly way.

Sometimes you need a small change to a package in `node_modules/` to fix a bug or add a feature. `bun patch` lets you do this without vendoring the entire package.

Features:

- Generates `.patch` files that Bun applies to dependencies in `node_modules` on install
- You can commit `.patch` files to your repository and reuse them across installs, projects, and machines
- `"patchedDependencies"` in `package.json` keeps track of patched packages
- Patches packages in `node_modules/` while preserving the integrity of Bun's [Global Cache](/pm/global-cache)
- Test your changes locally before committing them with `bun patch --commit <pkg>`
- To preserve disk space and keep `bun install` fast, Bun commits patched packages to the Global Cache and shares them across projects where possible

#### Step 1. Prepare the package for patching

Use `bun patch <pkg>` to prepare the package for patching:

```bash
# you can supply the package name
bun patch react

# ...and a precise version in case multiple versions are installed
bun patch react@17.0.2

# or the path to the package
bun patch node_modules/react
```

> Note
Always run `bun patch <pkg>` first. It ensures the package folder in `node_modules/` contains a fresh copy of the package with no symlinks or hardlinks to Bun's cache.

If you skip it, you might end up editing the package globally in the cache.


#### Step 2. Test your changes locally

`bun patch <pkg>` makes it safe to edit `<pkg>` in `node_modules/` directly, while preserving the integrity of Bun's [Global Cache](/pm/global-cache). It works by re-creating an unlinked clone of the package in `node_modules/`. `bun patch --commit <pkg>` then diffs that clone against the original package in the Global Cache.

#### Step 3. Commit your changes

Once you're happy with your changes, run `bun patch --commit <path or pkg>`.

Bun generates a patch file in `patches/`, updates your `package.json` and lockfile, and starts using the patched package:

```bash
# you can supply the path to the patched package
bun patch --commit node_modules/react

# ... or the package name and optionally the version
bun patch --commit react@17.0.2

# choose the directory to store the patch files
bun patch --commit react --patches-dir=mypatches

# `patch-commit` is available for compatibility with pnpm
bun patch-commit react
```

---

# CLI Usage

```bash
bun patch <package>@<version>
```

### Patch Generation

### `--commit`

Type: `boolean`
Install a package containing modifications in `dir`

### `--patches-dir`

Type: `string`
The directory to put the patch file in (only if --commit is used)

### Dependency Management

### `--production`

Type: `boolean`
Don't install devDependencies. Alias: `-p`

### `--ignore-scripts`

Type: `boolean`
Skip lifecycle scripts for all packages, including the project's `package.json` and trusted dependencies

### `--trust`

Type: `boolean`
Add to `trustedDependencies` in the project's `package.json` and install the package(s)

### `--global`

Type: `boolean`
Install globally. Alias: `-g`

### `--omit`

Type: `string`
Exclude `dev`, `optional`, or `peer` dependencies from install

### Project Files & Lockfiles

### `--yarn`

Type: `boolean`
Write a `yarn.lock` file (yarn v1). Alias: `-y`

### `--no-save`

Type: `boolean`
Don't update `package.json` or save a lockfile

### `--save`

Type: `boolean`; Default: `true`
Save to `package.json` (true by default)

### `--frozen-lockfile`

Type: `boolean`
Disallow changes to lockfile

### `--save-text-lockfile`

Type: `boolean`
Save a text-based lockfile

### `--lockfile-only`

Type: `boolean`
Generate a lockfile without installing dependencies

### Installation Control

### `--backend`

Type: `string`
Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default on
macOS), `hardlink` (default on Linux and Windows), `symlink`, `copyfile`

### `--linker`

Type: `string`
Linker strategy (one of `isolated` or `hoisted`)

### `--minimum-release-age`

Type: `number`
Only install packages published at least N seconds ago (security feature)

### `--dry-run`

Type: `boolean`
Don't install packages, update `package.json`, or save a lockfile. The package is still copied into{" "}
`node_modules` for patching, and `--commit` still writes the patch file

### `--force`

Type: `boolean`
Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

### `--no-verify`

Type: `boolean`
Skip verifying integrity of newly downloaded packages

### Network & Registry

### `--ca`

Type: `string`
Provide a Certificate Authority signing certificate

### `--cafile`

Type: `string`
Same as `--ca`, but as a file path to the certificate

### `--registry`

Type: `string`
Use a specific registry by default, overriding `.npmrc`, `bunfig.toml`, and environment
variables

### `--network-concurrency`

Type: `number`; Default: `48`
Maximum number of concurrent network requests (default 48)

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

### Global Configuration & Context

### `--config`

Type: `string`
Specify path to config file (`bunfig.toml`). Alias: `-c`

### `--cwd`

Type: `string`
Set a specific current working directory

### Help

### `--help`

Type: `boolean`
Print this help menu. Alias: `-h`
