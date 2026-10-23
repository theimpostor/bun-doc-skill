# oxc/no-barrel-file
Source: https://bun.com/docs/lint/rules/oxc/no-barrel-file

Disallow files that load too many modules through `export *`


A barrel file re-exports other files with `export *`. Importing one name from it loads every file behind it, and every file those import. In a large project, that slows down startup, tests, and bundling for code that's never used.

Each `export *` or `export * as name` counts as one module, plus every module the re-exported file imports, directly or through other files. The file is reported when the total is more than `threshold`.

With an oxlint config, other files are only read if the `import` plugin is on. Without it, only the `export *` lines count.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/no-barrel-file" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/no-barrel-file" = ["error", {
  threshold = 100,
}]
```


## Examples

With `threshold` set to `3`, this `index.js` is reported. Each `export *` loads two modules, which makes four:

```js
export const db = new Map();
```

```js
import { db } from "./db.js";
export const findUser = id => db.get(`user:${id}`);
```

```js
import { db } from "./db.js";
export const findOrder = id => db.get(`order:${id}`);
```

```js
export * from "./users.js";
export * from "./orders.js";
```

`db.js` counts twice, once for each `export *` that reaches it.

Exports that name what they export are never counted:

```js
export { findUser } from "./users.js";
export { findOrder } from "./orders.js";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `threshold` | `100` | The largest number of modules a file can load through `export *`. |

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/no-barrel-file" = ["error", { threshold = 20 }]
```
