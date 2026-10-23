# import/no-relative-packages
Source: https://bun.com/docs/lint/rules/import/no-relative-packages

Disallow relative imports that reach into another package


In a monorepo, `../ui/button.js` only works while both packages stay where they are on disk. It also skips the other package's `exports`, and the dependency never shows up in your `package.json`.

A file belongs to the closest `package.json` above it that has a `name`. The rule reports a relative import that resolves to a file in a package with a different name.

`--fix` rewrites the path so it starts with the package's name.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-relative-packages" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-relative-packages" = ["error", {
  esmodule = true,
  commonjs = false,
  amd = false,
  # ignore = <list of strings>,
}]
```


## Examples

Reported:

**File:** `packages/app/package.json`
```json
{ "name": "app" }
```

**File:** `packages/ui/package.json`
```json
{ "name": "@acme/ui" }
```

**File:** `packages/ui/button.js`
```js
export function Button() {}
```

**File:** `packages/app/index.js`
```js
import { Button } from "../ui/button.js";
```

Not reported:

**File:** `packages/app/theme.js`
```js
export const theme = {};
```

**File:** `packages/app/index.js`
```js
import { Button } from "@acme/ui/button.js";
import { theme } from "./theme.js";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `esmodule` | `true` | Check `import`, `export .. from` and `import()`. |
| `commonjs` | `false` | Also check `require()`. |
| `amd` | `false` | Also check the dependencies of `define()` and of `require([..])`. |
| `ignore` | `[]` | Regular expressions. A path that matches one of them is skipped. |

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-relative-packages" = ["error", { commonjs = true }]
```
