# import/no-extraneous-dependencies
Source: https://bun.com/docs/lint/rules/import/no-extraneous-dependencies

Disallow importing a package that `package.json` does not list


A package can end up in `node_modules` only because another package depends on it. Importing it works on your machine until that other package drops or upgrades it. It also fails for anyone who installs your package, because nothing tells the package manager to install it.

The rule reads the closest `package.json` above the file. A package is fine if it's in `dependencies`, `devDependencies`, `optionalDependencies`, `peerDependencies` or `bundledDependencies`. The rule checks `import`, `export ... from`, `import()` and `require()`. It skips relative paths, Node.js builtins, `import type` and packages that aren't installed.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-extraneous-dependencies" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-extraneous-dependencies" = ["error", {
  devDependencies = true,
  optionalDependencies = true,
  peerDependencies = true,
  bundledDependencies = true,
  # packageDir = <string or list>,
  includeInternal = false,
  includeTypes = false,
}]
```


## Examples

Here `ms` is installed, but only `express` is listed. Reported:

**File:** `package.json`
```json
{
  "name": "shop",
  "dependencies": { "express": "^5.0.0" }
}
```

**File:** `node_modules/ms/package.json`
```json
{ "name": "ms", "main": "index.js" }
```

**File:** `node_modules/ms/index.js`
```js
module.exports = text => Number.parseInt(text) * 1000;
```

```js
import express from "express";
import ms from "ms";
```

Not reported, with the same `package.json`:

**File:** `package.json`
```json
{
  "name": "shop",
  "dependencies": { "express": "^5.0.0" }
}
```

```js
import express from "express";
import { join } from "node:path";
import { cart } from "./cart";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `devDependencies` | `true` | `false` reports imports of packages that are only in `devDependencies`. An array of globs lists the files that can import them. |
| `optionalDependencies` | `true` | The same for `optionalDependencies`. |
| `peerDependencies` | `true` | The same for `peerDependencies`. |
| `bundledDependencies` | `true` | The same for `bundledDependencies`. |
| `packageDir` | none | A directory, or an array of directories, to read `package.json` from instead of the closest one. In a monorepo, list the package and the root. |
| `includeInternal` | `false` | Also check names that resolve to a file in your own project. |
| `includeTypes` | `false` | Also check `import type`. |

Globs and `packageDir` are relative to the directory where `bun lint` runs.

Most projects allow `devDependencies` in tests and scripts only:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-extraneous-dependencies" = ["error", {
  devDependencies = ["test/**", "scripts/**"],
}]
```

With that config, code that ships can't import a package that's missing in production:

**File:** `package.json`
```json
{
  "name": "shop",
  "devDependencies": { "ms": "^2.0.0" }
}
```

**File:** `node_modules/ms/package.json`
```json
{ "name": "ms", "main": "index.js" }
```

**File:** `node_modules/ms/index.js`
```js
module.exports = text => Number.parseInt(text) * 1000;
```

**File:** `src/cart.js`
```js
import ms from "ms";
```
