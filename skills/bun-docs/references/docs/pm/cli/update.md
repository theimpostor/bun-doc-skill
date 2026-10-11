# bun update
Source: https://bun.com/docs/pm/cli/update

Update dependencies to the newest versions their ranges allow


> Note: To upgrade your Bun CLI version, see [`bun upgrade`](/installation#upgrading).

`bun update` (alias `bun up`) updates every dependency, direct and transitive, to the newest version allowed by the ranges that request it. It then rewrites `package.json` and `bun.lock`. To ignore your declared ranges, use [`--latest`](#--latest).

```sh
bun update
```

To update specific packages, pass their names. Names can be glob patterns, and `!` excludes:

```sh
bun update zod
bun update jquery@3            # move the package.json entry to the newest 3.x
bun update '@types/*'
bun update '@babel/*' '!@babel/core'
```

`bun update <package>` updates `<package>` everywhere it appears in `bun.lock` and leaves everything else alone. This works for transitive dependencies too — `bun update caniuse-lite` picks up a nested fix without adding it to your `package.json`. A name that isn't in `bun.lock` is an error.

Updated packages appear in the install summary as `↑ name old → new`, with `(v3.0.0 available)` when a newer major is out of range. Use `--dry-run` to preview.

### How `package.json` is rewritten

- `^1.1.0` → `^1.2.0`, `~1.1.0` → `~1.1.5`. Bun preserves the operator. With [`install.exact`](/runtime/bunfig#install-exact) or `--exact`, Bun writes an exact version instead.
- Exact pins, dist-tags (`"latest"`, `"next"`), and other range forms (`*`, `1.x`, `>=1.0.0`) are left as written; only `bun.lock` moves. `--latest` rewrites them.
- Bun never rewrites `catalog:` references; it updates the catalog entry in the root `package.json` instead.
- `--no-save` updates `node_modules` only, leaving `package.json` and `bun.lock` untouched.

### What is held back

- Bun never widens ranges. A package that depends on `foo@^1.0.0` never gets `foo@2.x`.
- Versions in `patchedDependencies` stay put as long as their range allows. Bun reports them as `kept name@version (patched, v1.2.3 available)`. `--latest` and [`bun audit fix`](/pm/cli/audit#bun-audit-fix) do move them; re-create the patch with [`bun patch`](/pm/cli/patch) afterwards.
- If a registry request for a transitive package fails, that package keeps its locked version and Bun prints a warning. A failed request for a direct dependency is an error.

## `--interactive`

Use the `--interactive` flag to choose which packages to update:

```sh
bun update --interactive
bun update -i
```

`--interactive` opens a terminal interface listing every outdated direct dependency. Bun updates the packages you select as if you had run `bun update <name> ...`; everything else keeps its locked version.

### Interactive Interface

The interface displays packages grouped by dependency type:

```txt
? Select packages to update - Space to toggle, Enter to confirm, a to select all, n to select none, i to invert, l to toggle latest

  dependencies                Current  Target   Latest
    □ react                   17.0.2   18.2.0   18.3.1
    □ lodash                  4.17.20  4.17.21  4.17.21

  devDependencies             Current  Target   Latest
    □ typescript              4.8.0    5.0.0    5.3.3
    □ @types/node             16.11.7  18.0.0   20.11.5

  optionalDependencies        Current  Target   Latest
    □ some-optional-package   1.0.0    1.1.0    1.2.0
```

**Sections:**

- Packages are grouped under section headers: `dependencies`, `devDependencies`, `peerDependencies`, `optionalDependencies`
- Each section shows column headers aligned with the package data

**Columns:**

- **Package**: Package name (may have a suffix such as ` dev`, ` peer`, or ` optional`)
- **Current**: Currently installed version
- **Target**: Version that would be installed (respects semver constraints)
- **Latest**: Latest available version

### Keyboard Controls

**Selection:**

- **Space**: Toggle package selection
- **Enter**: Confirm selections and update
- **a/A**: Select all packages
- **n/N**: Select none
- **i/I**: Invert selection

**Navigation:**

- **↑/↓ Arrow keys** or **j/k**: Move cursor
- **l/L**: Toggle between target and latest version for current package

**Exit:**

- **Ctrl+C** or **Ctrl+D**: Cancel without updating

### Visual Indicators

- **■** Selected packages (will be updated)
- **□** Unselected packages
- **❯** Current cursor position
- **Colors**: Red (major), yellow (minor), green (patch) version changes
- **Underlined**: Currently selected update target

### Package Grouping

Packages are organized in sections by dependency type:

- **dependencies** - Regular runtime dependencies
- **devDependencies** - Development dependencies
- **peerDependencies** - Peer dependencies
- **optionalDependencies** - Optional dependencies

Within each section, individual packages may have a suffix (` dev`, ` peer`, ` optional`).

## `--recursive` and `--filter`

In a monorepo, `bun update` only rewrites the `package.json` of the workspace you run it in. From the root, it still updates the transitive dependencies of every workspace in `bun.lock`.

- `--recursive` (`-r`) updates every workspace's `package.json`.
- `--filter <pattern>` (`-F`) updates only the matching workspaces, using the [filter syntax](/pm/filter). As with `bun install --filter`, Bun links only the selected workspaces afterwards.

Both combine with package names, `--latest`, `--dry-run`, and `--interactive` (which adds a "Workspace" column).

```sh
bun update --recursive
bun update --filter './packages/*'
bun update -i -r
bun update zod -r
bun update zod --filter '...^ui'
```

## `--dev`, `--prod`, `--no-optional`

Restrict which `package.json` entries Bun updates:

- `--dev` (`-D`) updates `devDependencies` only.
- `--prod` (`-P`) updates `dependencies` and `optionalDependencies` only.
- `--no-optional` skips `optionalDependencies`.

They combine with names, patterns, `--latest`, and `--interactive`.

These flags only select what to update — `bun update --prod` still installs `devDependencies`.

```sh
bun update --dev
bun update --prod --latest
bun update -D '@types/*'
bun update -i --prod
```

## `--global`

`bun update -g` updates packages installed with `bun add -g`:

```sh
bun update -g
bun update -g typescript
```

## `--latest`

By default, `bun update` updates each dependency to the latest version that satisfies the version range in your `package.json`.

To update direct dependencies to the latest version regardless of the declared range, use `--latest` (`-L`). Bun rewrites the `package.json` entry to a range of the same style on the new version. Transitive dependencies still respect the ranges their dependents declare. Bun does not downgrade a dependency that is already ahead of `latest` (e.g. a prerelease).

```sh
bun update --latest
bun update -L
```

In interactive mode, press **l** to toggle a package between its target version (respecting semver) and the latest version.

For example, with the following `package.json`:

**File:** `package.json`
```json
{
  "dependencies": {
    "react": "^17.0.2"
  }
}
```

- `bun update` would update to a version that matches `17.x`.
- `bun update --latest` would update to a version that matches `18.x` or later.

---

## CLI Usage

```bash
bun update [<name>[@<version>] | <pattern>]...
bun up
```

### Update Strategy

### `--force`

Type: `boolean`
Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

### `--latest`

Type: `boolean`
Update packages to their latest versions. Alias: `-L`

### Dependency Scope

### `--dev`

Type: `boolean`
Only update `devDependencies`. Alias: `-D`

### `--prod`

Type: `boolean`
Only update `dependencies` and `optionalDependencies`. Aliases: `-P`,{" "}
`--production`

### `--no-optional`

Type: `boolean`
Don't update `optionalDependencies`

### `--global`

Type: `boolean`
Install globally. Alias: `-g`

### `--omit`

Type: `string`
Exclude `dev`, `optional`, or `peer` dependencies from install

### Project File Management

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

### Network & Registry

### `--ca`

Type: `string`
Provide a Certificate Authority signing certificate

### `--cafile`

Type: `string`
Same as `--ca`, but as a file path to the certificate

### `--registry`

Type: `string`
Use a specific registry by default, overriding `.npmrc`, `bunfig.toml` and environment variables

### `--network-concurrency`

Type: `number`; Default: `48`
Maximum number of concurrent network requests (default 48)

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

### `--verbose`

Type: `boolean`
Excessively verbose logging

### `--no-progress`

Type: `boolean`
Disable the progress bar

### `--no-summary`

Type: `boolean`
Don't print a summary

### Script Execution

### `--ignore-scripts`

Type: `boolean`
Skip lifecycle scripts for all packages, including the project's `package.json` and trusted dependencies

### `--concurrent-scripts`

Type: `number`
Maximum number of concurrent jobs for lifecycle scripts (default: 2x CPU cores)

### Installation Controls

### `--no-verify`

Type: `boolean`
Skip verifying integrity of newly downloaded packages

### `--trust`

Type: `boolean`
Add to `trustedDependencies` in the project's `package.json` and install the package(s)

### `--backend`

Type: `string`
Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default on
macOS), `hardlink` (default on Linux and Windows), `symlink`, `copyfile`

### General & Environment

### `--config`

Type: `string`
Specify path to config file (`bunfig.toml`). Alias: `-c`

### `--dry-run`

Type: `boolean`
Resolve updates but don't install packages, update `package.json`, or save a lockfile (the project's own
lifecycle scripts still run)

### `--cwd`

Type: `string`
Set a specific cwd

### `--help`

Type: `boolean`
Print this help menu. Alias: `-h`
