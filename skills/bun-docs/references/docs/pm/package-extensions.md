# Package extensions
Source: https://bun.com/docs/pm/package-extensions

Add missing dependencies and peerDependencies to third-party packages with packageExtensions


Some packages `require()` a package they never declare. With a hoisted `node_modules` this often goes unnoticed; with [isolated installs](/pm/isolated-installs) a package only sees what it declares, so the import fails.

`packageExtensions` in the root `package.json` adds the missing entries, without a fork or a patch. It has the shape of pnpm's and Yarn's setting of the same name.

**File:** `package.json`
```json
{
  "name": "my-app",
  "dependencies": {
    "react": "^18.0.0",
    "react-redux": "^7.0.0",
    "legacy-plugin": "^2.0.0"
  },
  "packageExtensions": {
    "react-redux@7": {
      "peerDependencies": { "react": "*" }
    },
    "legacy-plugin": {
      "dependencies": { "lodash": "^4.17.21" },
      "peerDependenciesMeta": { "webpack": { "optional": true } }
    }
  }
}
```

- **Key**: a package name, optionally with a semver range (`react-redux@7`, `@scope/pkg@^1.2`). Without a range it applies to every version.
- **Value**: `dependencies`, `optionalDependencies`, `peerDependencies` and `peerDependenciesMeta`, as in a `package.json`.
- **The package wins**: an entry is ignored when the package declares a dependency of that name itself, in any group. To change a version that a package declares, use [`overrides`](/pm/overrides).
- `peerDependenciesMeta` with `"optional": true` also makes a peer optional that the package declares itself.
- When several keys match a package, the first one that names a dependency wins.
- A specifier is a version, a range, a tag, an `npm:` alias, a git repository or a tarball URL. A key that holds `file:`, `link:`, `workspace:` or `catalog:` is ignored with a warning.
- Only packages from a registry are extended. Edit the `package.json` of a workspace, `file:` or `link:` dependency instead.

## Lockfile

The added entries are written to `bun.lock` with the package's own dependencies, so `bun install --frozen-lockfile` reproduces them. A `packageExtensions` section in `bun.lock` lists which entries were added:

**File:** `bun.lock`
```json
{
  "packageExtensions": {
    "legacy-plugin@2.0.3": { "dependencies": ["lodash"], "optionalPeers": ["webpack"] },
    "react-redux@7.2.9": { "peerDependencies": ["react"] }
  }
}
```

After you add, edit or remove an extension, the next `bun install` changes those entries only. Every other version in `bun.lock` stays as it is. `bun install --frozen-lockfile` fails until `bun.lock` is updated.

## Migrating

`bun install` and `bun pm migrate` copy `pnpm.packageExtensions`, `packageExtensions` in `pnpm-workspace.yaml` and `packageExtensions` in `.yarnrc.yml` to the root `package.json` when they migrate a `pnpm-lock.yaml` or a `yarn.lock`.
