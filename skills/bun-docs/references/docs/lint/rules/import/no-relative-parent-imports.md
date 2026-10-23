# import/no-relative-parent-imports
Source: https://bun.com/docs/lint/rules/import/no-relative-parent-imports

Disallow relative imports from parent directories


An import from `../` ties a directory to its place in the project. Move the directory and the import breaks. With this rule on, a directory only depends on packages and on the files inside it.

To fix a report, move the file you import into the directory, or make it a package and import it by name.

Only imports that resolve to a file are reported. A path that doesn't exist is left to `import/no-unresolved`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-relative-parent-imports" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-relative-parent-imports" = ["error", {
  esmodule = true,
  commonjs = false,
  amd = false,
  # ignore = <list of strings>,
}]
```


## Examples

Reported:

**File:** `src/api.js`
```js
export function getUser() {}
```

**File:** `src/pages/home.js`
```js
import { getUser } from "../api.js";
```

Not reported:

**File:** `src/pages/header.js`
```js
export function Header() {}
```

**File:** `src/pages/parts/footer.js`
```js
export function Footer() {}
```

**File:** `src/pages/home.js`
```js
import { getUser } from "@acme/api";
import { Header } from "./header.js";
import { Footer } from "./parts/footer.js";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `esmodule` | `true` | Check `import`, `export .. from` and `import()`. |
| `commonjs` | `false` | Also check `require()`. |
| `amd` | `false` | Also check the dependencies of `define()` and of `require([..])`. |
| `ignore` | `[]` | Regular expressions. A path that matches one of them is skipped. |

With `ignore`, you can keep one shared directory reachable:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-relative-parent-imports" = ["error", {
  ignore = ["^\\.\\./shared/"],
}]
```

**File:** `src/shared/format.js`
```js
export function formatDate() {}
```

**File:** `src/pages/home.js`
```js
import { formatDate } from "../shared/format.js";
```

## When not to use it

Most projects share code between sibling directories through `../`. This rule fits a project that's built as a strict tree and reaches shared code through packages.
