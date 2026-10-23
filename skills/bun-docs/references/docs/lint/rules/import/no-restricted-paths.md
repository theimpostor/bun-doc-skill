# import/no-restricted-paths
Source: https://bun.com/docs/lint/rules/import/no-restricted-paths

Disallow files in one folder from importing files in another


Some folders shouldn't depend on others. Code that ships to the browser shouldn't pull in server code, and a shared library shouldn't import from the app that uses it. You describe those boundaries as zones, and the rule reports every import that crosses one.

The rule does nothing until you give it zones. It checks `import`, `export .. from`, `import()` and `require()`, and only paths that resolve to a file.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-restricted-paths" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-restricted-paths" = ["error", {
  # zones = <list of objects>,
  # basePath = <string>,
}]
```


## Examples

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-restricted-paths" = ["error", {
  zones = [{ target = "./src/client", from = "./src/server" }],
}]
```

With this zone, files in `src/client` can't import files in `src/server`.

Reported:

**File:** `src/server/db.js`
```js
export function query() {}
```

**File:** `src/client/app.js`
```js
import { query } from "../server/db.js";
```

Not reported:

**File:** `src/shared/format.js`
```js
export function formatDate() {}
```

**File:** `src/client/app.js`
```js
import { formatDate } from "../shared/format.js";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `zones` | `[]` | The list of zones. |
| `basePath` | the directory you run `bun lint` in | The directory that `target` and `from` are relative to. |

Each zone has these keys:

| Key | What it does |
| --- | --- |
| `target` | The files the restriction applies to. A path, a glob, or a list of them. A path to a folder covers everything in it. |
| `from` | The files that `target` can't import. A path, a glob, or a list. A list is either all paths or all globs. |
| `except` | Files inside `from` that you can still import. |
| `message` | Text to add to the report. |

If `from` is a path, each `except` is a path relative to `from` and must be inside it. If `from` is a glob, each `except` must be a glob too, and it needs to match the file's absolute path, like `**/types.js`.

With this zone, `src/client/app.js` can import `../server/types.js` and nothing else from `src/server`:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-restricted-paths" = ["error", {
  zones = [{
    target = "./src/client",
    from = "./src/server",
    except = ["./types.js"],
    message = "Call the API instead.",
  }],
}]
```
