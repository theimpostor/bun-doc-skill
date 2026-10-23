# import/no-unused-modules
Source: https://bun.com/docs/lint/rules/import/no-unused-modules

Disallow exports that no other file imports, and files that export nothing


An export that nothing imports is dead code that looks alive, so it still gets maintained, tested and refactored. This rule reads the project's files, collects what each one imports, and reports the exports that are left over.

The rule does nothing until you turn on `unusedExports` or `missingExports`.

`unusedExports` only works in a project with an ESLint 8 config. It needs an `.eslintrc` file, or `eslintConfig` in `package.json`, in or above every folder it searches. Without one it reports nothing, so it has no effect in a project that only has a `bunfig.toml`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-unused-modules" = "error" # or "warn"
```


## Examples

Reported, because nothing imports `formatTime`:

**File:** `shop/.eslintrc.json`
```json
{
  "root": true,
  "plugins": ["import"],
  "parserOptions": { "ecmaVersion": "latest", "sourceType": "module" },
  "rules": { "import/no-unused-modules": ["error", { "unusedExports": true }] }
}
```

**File:** `shop/app.js`
```js
import { formatDate } from "./format.js";

console.log(formatDate(new Date()));
```

**File:** `shop/format.js`
```js
export function formatDate(date) {}
export function formatTime(date) {}
```

Not reported, with the same two other files:

**File:** `shop/.eslintrc.json`
```json
{
  "root": true,
  "plugins": ["import"],
  "parserOptions": { "ecmaVersion": "latest", "sourceType": "module" },
  "rules": { "import/no-unused-modules": ["error", { "unusedExports": true }] }
}
```

**File:** `shop/app.js`
```js
import { formatDate } from "./format.js";

console.log(formatDate(new Date()));
```

**File:** `shop/format.js`
```js
export function formatDate(date) {}
function formatTime(date) {}
```

Here's what counts as a use:

- `import * as format from "./format.js"` and `import("./format.js")` use every export in the file.
- `export * from "./format.js"` uses every export except the default.
- `require("./format.js")` uses nothing.

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `unusedExports` | `false` | Report exports that no other file imports. |
| `missingExports` | `false` | Report files that export nothing. |
| `src` | the directory you run `bun lint` in | Files, folders and globs to search for imports. A file outside them isn't checked for unused exports. |
| `ignoreExports` | `[]` | Files, folders and globs whose exports are never reported, such as entry points and tests. |
| `ignoreUnusedTypeExports` | `false` | Don't report an unused exported `type`, `interface` or `enum`. |

Only `.js`, `.mjs` and `.cjs` files are searched, unless the `import/extensions` setting lists others.

The files that `main`, `bin` and `browser` in the closest `package.json` point to are entry points. Their exports aren't reported, unless the package is `"private": true`.

With `missingExports`, this file is reported:

```js
function formatDate(date) {}
```

## When not to use it

A library's exports are used by other projects, which the rule can't see. List the public files in `ignoreExports`, or leave the rule off.
