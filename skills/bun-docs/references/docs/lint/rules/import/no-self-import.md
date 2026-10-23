# import/no-self-import
Source: https://bun.com/docs/lint/rules/import/no-self-import

Disallow a module from importing itself


A file that imports itself is almost always a mistake left over from a rename, a move, or an editor's auto-import. Everything it gets that way is already in scope, and `require()` returns the `exports` object before the file has finished filling it.

The rule resolves each path, so it also catches other spellings of the same file, such as `.` in an `index.js`. It checks `import`, `export .. from`, `import()` and `require()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-self-import" = "error" # or "warn"
```


## Examples

Reported:

**File:** `cart.js`
```js
import * as cart from "./cart.js";

export function total(items) {
  return items.length;
}

export function print(items) {
  console.log(cart.total(items));
}
```

**File:** `index.js`
```js
const { version } = require("."); // undefined

exports.version = "1.0.0";
```

Not reported:

**File:** `cart.js`
```js
export function total(items) {
  return items.length;
}

export function print(items) {
  console.log(total(items));
}
```
