# import/no-internal-modules
Source: https://bun.com/docs/lint/rules/import/no-internal-modules

Disallow importing a file from inside another directory or package


A directory with an `index.js` works like a package. It decides what the outside gets to see. An import that reaches past it, such as `./api/users` or `lodash/get`, depends on how the inside is laid out, so it breaks when someone moves or renames a file in there.

An import path can have one step, like `./api`, `../api`, `lodash` or `@scope/package`. A longer path is reported if the file exists. The rule also checks `export ... from`, `import()` and `require()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-internal-modules" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-internal-modules" = ["error", {
  allow = [], # list of strings
  # forbid = <list of strings>,
}]
```


## Examples

Reported:

**File:** `api/index.js`
```js
export { listUsers } from "./users";
```

**File:** `api/users.js`
```js
export const listUsers = () => fetch("/users");
```

```js
import { listUsers } from "./api/users";
```

Not reported:

**File:** `api/index.js`
```js
export { listUsers } from "./users";
```

**File:** `api/users.js`
```js
export const listUsers = () => fetch("/users");
```

```js
import { listUsers } from "./api";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allow` | `[]` | Globs. A longer path is allowed if a glob matches the import path (without its `./` or `../`) or the file's full path. |
| `forbid` | none | Globs, matched the same way. Only paths that match a glob are reported, and every other path is allowed. |

Use `allow` or `forbid`, not both.

With `{ "allow": ["api/*"] }`:

**File:** `api/users.js`
```js
export const listUsers = () => fetch("/users");
```

```js
import { listUsers } from "./api/users";
```

With `{ "forbid": ["db/*"] }`, only the second import is reported:

**File:** `api/users.js`
```js
export const listUsers = () => fetch("/users");
```

**File:** `db/pool.js`
```js
export const pool = [];
```

```js
import { listUsers } from "./api/users";
import { pool } from "./db/pool";
```
