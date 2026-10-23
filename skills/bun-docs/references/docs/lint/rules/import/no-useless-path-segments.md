# import/no-useless-path-segments
Source: https://bun.com/docs/lint/rules/import/no-useless-path-segments

Disallow path segments in imports that can be removed


`./../format.js` works, and so does `../pages/header.js` written inside `pages`, but each has a shorter spelling that points to the same file. The long ones are usually left over from moving a file, and they make one module look like two when you search for it.

Only relative paths are checked. `--fix` writes the shorter path.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-useless-path-segments" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-useless-path-segments" = ["error", {
  commonjs = false,
  noUselessIndex = false,
}]
```


## Examples

Reported:

**File:** `src/format.js`
```js
export function formatDate() {}
```

**File:** `src/pages/header.js`
```js
export function Header() {}
```

**File:** `src/pages/home.js`
```js
import { formatDate } from "./../format.js";
import { Header } from "../pages/header.js";
```

Not reported:

**File:** `src/format.js`
```js
export function formatDate() {}
```

**File:** `src/pages/header.js`
```js
export function Header() {}
```

**File:** `src/pages/home.js`
```js
import { formatDate } from "../format.js";
import { Header } from "./header.js";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `commonjs` | `false` | Also check `require()`. |
| `noUselessIndex` | `false` | Also report a path that ends in `/index` or `/index.js`, because the folder's name resolves to the same file. |

With `noUselessIndex`, the first import is reported and the second isn't:

**File:** `parts/index.js`
```js
export function Footer() {}
```

```js
import { Footer } from "./parts/index.js";
import { Footer as SameFooter } from "./parts";
```

## When not to use it

Leave `noUselessIndex` off for code that runs as ES modules in Node.js or in a browser. There, an import needs to name the file, and `./parts` doesn't find `./parts/index.js`.
