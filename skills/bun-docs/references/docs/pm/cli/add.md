# bun add
Source: https://bun.com/docs/pm/cli/add

Add packages to your project with Bun's fast package manager

To add a particular package:

```bash
bun add preact
```

To specify a version, version range, or tag:

```bash
bun add zod@3.20.0
bun add zod@^3.0.0
bun add zod@latest
```

Bun writes the package to `dependencies` unless you pass `--dev`, `--optional`, or `--peer`. If `package.json` already lists it in another group, Bun updates that entry in place.

## `--dev`

> Note: **Alias** — `--development`, `-d`, `-D`

To add a package as a dev dependency (`"devDependencies"`):

```bash
bun add --dev @types/react
bun add -d @types/react
```

## `--optional`

To add a package as an optional dependency (`"optionalDependencies"`):

```bash
bun add --optional lodash
```

## `--peer`

To add a package as a peer dependency (`"peerDependencies"`):

```bash
bun add --peer @types/bun
```

Bun installs peer dependencies by default, so no additional `devDependencies` entry is needed.

## `--exact`

> Note: **Alias** — `-E`

To pin a package to the resolved version, use `--exact`. Bun writes the exact version number to your `package.json` instead of a version range.

```bash
bun add react --exact
bun add react -E
```

The difference in `package.json`:

**File:** `package.json`
```json
{
  "dependencies": {
    // without --exact
    "react": "^18.2.0", // this matches >= 18.2.0 < 19.0.0

    // with --exact
    "react": "18.2.0" // this matches only 18.2.0 exactly
  }
}
```

To view a complete list of options for this command:

```bash
bun add --help
```

## `--catalog`

In a workspace, `--catalog` writes the version to the root `package.json` [catalog](/docs/pm/catalogs) and adds `"catalog:"` to the current package. `--catalog=<name>` uses a named catalog (`workspaces.catalogs.<name>`) and writes `"catalog:<name>"`.

```bash
bun add react --catalog
bun add vitest --catalog=testing
```

**File:** `package.json`
```json
// root package.json
{
  "workspaces": {
    "packages": ["packages/*"],
    "catalog": {
      "react": "^18.2.0"
    }
  }
}
```

**File:** `packages/app/package.json`
```json
{
  "dependencies": {
    "react": "catalog:"
  }
}
```

* If the catalog already has an entry, Bun reuses it and writes only `"catalog:"` to the current package. Pass an explicit version (`bun add react@19 --catalog`) to replace the entry — this affects every package that references it.
* If you omit the version and the current `package.json` already has a range (`"react": "^18.2.0"`), Bun catalogs that range.
* A package that already references `"catalog:<name>"` keeps using that catalog.
* Attach the name with `=`: `--catalog=testing`, not `--catalog testing`.
* Bun catalogs tarball and git specifiers under the package's real name. It rejects relative paths and workspace packages.

Even without the flag, `bun add react` (no version) writes `"catalog:"` if the default catalog already lists `react`. Pass a version to write a concrete range instead.

## `--filter`

> Note: **Alias** — `-F`

In a monorepo, add the package to the matching workspace(s) instead of the current directory's package. See [filtering](/docs/pm/filter) for the pattern syntax. Repeat the flag to combine patterns; `!pattern` excludes.

```bash
bun add zod --filter api
bun add -d typescript --filter './packages/*'
bun add ./vendor/logger --filter '*'
bun remove zod --filter '*' --filter '!api'
```

* `*` matches every workspace package but not the root. To include the root, name it: `--filter '*' --filter '<root-name>'`.
* If no workspace matches, Bun writes nothing and the command fails.
* Bun resolves local paths from the current directory and rewrites them relative to each selected package.
* Bun updates `bun.lock` for the whole repo but links only the selected workspaces into `node_modules`, as with `bun install --filter`.
* Cannot be combined with `--global`.

## `--global`

> Note: **Alias** — `bun add --global`, `bun add -g`, `bun install --global` and `bun install -g`

To install a package globally, use the `-g`/`--global` flag. This does not modify the `package.json` of your current project. Use it to install command-line tools.

```bash
bun add --global cowsay # or `bun add -g cowsay`
cowsay "Bun!"
```

```txt
 ______
< Bun! >
 ------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

### Configuring global installation behavior
**File:** `bunfig.toml`
```toml
[install]
# where `bun add --global` installs packages
globalDir = "~/.bun/install/global"

# where globally-installed package bins are linked
globalBinDir = "~/.bun/bin"
```

## Trusted dependencies

Unlike other npm clients, Bun does not execute arbitrary lifecycle scripts for installed dependencies, such as `postinstall`. These scripts represent a potential security risk, as they can execute arbitrary code on your machine.

To tell Bun to allow lifecycle scripts for a particular package, add the package to `trustedDependencies` in your package.json.

**File:** `package.json`
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "trustedDependencies": ["my-trusted-package"]
}
```

Bun reads this field and runs lifecycle scripts for `my-trusted-package`.

## Git dependencies

To add a dependency from a public or private git repository:

```bash
bun add git@github.com:moment/moment.git
```

> Note
To install private repositories, your system needs the appropriate SSH credentials to access the repository.

Bun supports a variety of protocols, including [`github`](https://docs.npmjs.com/cli/v9/configuring-npm/package-json#github-urls), [`git`](https://docs.npmjs.com/cli/v9/configuring-npm/package-json#git-urls-as-dependencies), `git+ssh`, and `git+https`.

**File:** `package.json`
```json
{
  "dependencies": {
    "dayjs": "git+https://github.com/iamkun/dayjs.git",
    "lodash": "git+ssh://github.com/lodash/lodash.git#4.17.21",
    "moment": "git@github.com:moment/moment.git",
    "zod": "github:colinhacks/zod"
  }
}
```

## Tarball dependencies

A package name can correspond to a publicly hosted `.tgz` file. Bun downloads and installs the package from that tarball URL rather than from the package registry.

```sh
bun add zod@https://registry.npmjs.org/zod/-/zod-3.21.4.tgz
```

`bun add` writes the URL to your `package.json`:

**File:** `package.json`
```json
{
  "dependencies": {
    "zod": "https://registry.npmjs.org/zod/-/zod-3.21.4.tgz"
  }
}
```

***

## CLI Usage

```bash
bun add <package> <@version>
```

### Dependency Management

- (boolean) Don't install devDependencies. Alias: `-p`

- (string) Exclude `dev`, `optional`, or `peer` dependencies from install

- (boolean) Install globally. Alias: `-g`

- (boolean) Add dependency to `devDependencies`. Alias: `-d`

- (boolean) Add dependency to `optionalDependencies`

- (boolean) Add dependency to `peerDependencies`

- (boolean) Add the exact version instead of the `^` range. Alias: `-E`

- (boolean) Only add dependencies to `package.json` if they are not already present

- (string) Add the resolved version to the root `package.json` catalog and depend on it as `catalog:`; `--catalog=NAME` targets `catalogs.NAME`

- (string) Add the package(s) to the matching workspaces instead of the current package. Alias: `-F`

### Project Files & Lockfiles

- (boolean) Write a `yarn.lock` file (yarn v1). Alias: `-y`

- (boolean) Don't update `package.json` or save a lockfile

- (boolean) Save to `package.json`

- (boolean) Disallow changes to lockfile

- (boolean) Add to `trustedDependencies` in the project's `package.json` and install the package(s)

- (boolean) Save a text-based lockfile

- (boolean) Generate a lockfile without installing dependencies

### Installation Control

- (boolean) Perform a dry run without making changes

- (boolean) Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

- (boolean) Skip verifying integrity of newly downloaded packages

- (boolean) Skip lifecycle scripts for all packages, including the project's `package.json` and trusted dependencies

- (boolean) Recursively analyze & install dependencies of files passed as arguments (using Bun's bundler). Alias: `-a`

### Network & Registry

- (string) Provide a Certificate Authority signing certificate

- (string) Same as `--ca`, but as a file path to the certificate

- (string) Use a specific registry by default, overriding `.npmrc`, `bunfig.toml`, and environment variables

- (number) Maximum number of concurrent network requests

### Performance & Resource

- (string) Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default on macOS), `hardlink` (default on Linux and Windows), `symlink`, `copyfile`

- (number) Maximum number of concurrent jobs for lifecycle scripts (default: 2x CPU cores)

### Caching

- (string) Store & load cached data from a specific directory path

- (boolean) Ignore manifest cache entirely

### Output & Logging

- (boolean) Don't log anything

- (boolean) Excessively verbose logging

- (boolean) Disable the progress bar

- (boolean) Don't print a summary

### Global Configuration & Context

- (string) Specify path to config file (`bunfig.toml`). Alias: `-c`

- (string) Set a specific current working directory

### Help

- (boolean) Print this help menu. Alias: `-h`
