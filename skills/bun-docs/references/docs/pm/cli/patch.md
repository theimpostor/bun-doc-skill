# bun patch
Source: https://bun.com/docs/pm/cli/patch

Persistently patch node_modules packages in a git-friendly way

`bun patch` lets you persistently patch node_modules in a maintainable, git-friendly way.

Sometimes, you need to make a small change to a package in `node_modules/` to fix a bug or add a feature. `bun patch` lets you do this without vendoring the entire package and reuse the patch across multiple installs, multiple projects, and multiple machines.

Features:

* Generates `.patch` files applied to dependencies in `node_modules` on install
* `.patch` files can be committed to your repository, reused across multiple installs, projects, and machines
* `"patchedDependencies"` in `package.json` keeps track of patched packages
* `bun patch` lets you patch packages in `node_modules/` while preserving the integrity of Bun's [Global Cache](/pm/global-cache)
* Test your changes locally before committing them with `bun patch --commit <pkg>`
* To preserve disk space and keep `bun install` fast, patched packages are committed to the Global Cache and shared across projects where possible

#### Step 1. Prepare the package for patching

To get started, use `bun patch <pkg>` to prepare the package for patching:

```bash
# you can supply the package name
bun patch react

# ...and a precise version in case multiple versions are installed
bun patch react@17.0.2

# or the path to the package
bun patch node_modules/react
```

> Note
Don't forget to call `bun patch <pkg>`! This ensures the package folder in `node_modules/` contains a fresh copy of the package with no symlinks/hardlinks to Bun's cache.

If you forget to do this, you might end up editing the package globally in the cache!

#### Step 2. Test your changes locally

`bun patch <pkg>` makes it safe to edit the `<pkg>` in `node_modules/` directly, while preserving the integrity of Bun's [Global Cache](/pm/global-cache). This works by re-creating an unlinked clone of the package in `node_modules/` and diffing it against the original package in the Global Cache.

#### Step 3. Commit your changes

Once you're happy with your changes, run `bun patch --commit <path or pkg>`.

Bun will generate a patch file in `patches/`, update your `package.json` and lockfile, and Bun will start using the patched package:

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

***

# CLI Usage

```bash
bun patch <package>@<version>
```

### Patch Generation

- (boolean) Install a package containing modifications in `dir`

- (string) The directory to put the patch file in (only if --commit is used)

### Dependency Management

- (boolean) Don't install devDependencies. Alias: `-p`

- (boolean) Skip lifecycle scripts in the project's `package.json` (dependency scripts are never run)

- (boolean) Add to `trustedDependencies` in the project's `package.json` and install the package(s)

- (boolean) Install globally. Alias: `-g`

- (string) Exclude `dev`, `optional`, or `peer` dependencies from install

### Project Files & Lockfiles

- (boolean) Write a `yarn.lock` file (yarn v1). Alias: `-y`

- (boolean) Don't update `package.json` or save a lockfile

- (boolean) Save to `package.json` (true by default)

- (boolean) Disallow changes to lockfile

- (boolean) Save a text-based lockfile

- (boolean) Generate a lockfile without installing dependencies

### Installation Control

- (string) Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default), `hardlink`, `symlink`, `copyfile`

- (string) Linker strategy (one of `isolated` or `hoisted`)

- (boolean) Don't install anything

- (boolean) Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

- (boolean) Skip verifying integrity of newly downloaded packages

### Network & Registry

- (string) Provide a Certificate Authority signing certificate

- (string) Same as `--ca`, but as a file path to the certificate

- (string) Use a specific registry by default, overriding `.npmrc`, `bunfig.toml`, and environment variables

- (number) Maximum number of concurrent network requests (default 48)

### Performance & Resource

- (number) Maximum number of concurrent jobs for lifecycle scripts (default 5)

### Caching

- (string) Store & load cached data from a specific directory path

- (boolean) Ignore manifest cache entirely

### Output & Logging

- (boolean) Don't log anything

- (boolean) Only show tarball name when packing

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
