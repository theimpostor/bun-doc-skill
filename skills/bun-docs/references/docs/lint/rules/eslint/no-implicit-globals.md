# no-implicit-globals
Source: https://bun.com/docs/lint/rules/eslint/no-implicit-globals

Disallow declarations and assignments that create global variables by accident


In a classic script (one loaded with `<script>` and no `type="module"`), every top-level `var` and `function` becomes a global that all scripts on the page share. Two scripts that both declare `var config` overwrite each other. Outside strict mode, assigning to a name that was never declared creates a global too.

Modules and CommonJS files have their own top-level scope, so declarations in them are never reported. Without a config, `bun lint` takes every file for [one or the other](/lint#es-modules-and-commonjs). To lint files as scripts, set `sourceType` to `"script"` under `[lint.parserOptions]` in `bunfig.toml`, or in an ESLint config, as the examples do.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-implicit-globals" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-implicit-globals" = ["error", {
  lexicalBindings = false,
}]
```


## Examples

Reported in a script:

```js
export default [{ languageOptions: { sourceType: "script" } }];
```

```js
var config = { debug: false };

function start() {
  console.log(config.debug);
}
```

Not reported. The function keeps `config` and `start` private, and anything other scripts need is set on `window` explicitly:

```js
export default [{ languageOptions: { sourceType: "script" } }];
```

```js
(function () {
  var config = { debug: false };

  function start() {
    console.log(config.debug);
  }

  window.start = start;
})();
```

Reported in a CommonJS file, which isn't strict unless it says `"use strict"`. `total` is never declared:

```js
module.exports = function sum(prices) {
  total = 0;
  for (const price of prices) total += price;
  return total;
};
```

Reported in every kind of file, because `Promise` is a read-only built-in:

```js
import Bluebird from "bluebird";

Promise = Bluebird;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `lexicalBindings` | `false` | Also report `let`, `const` and `class` at the top level of a script. |

These don't become properties of `window`, but other scripts still see them, and a second script that declares the same name fails to load. Wrap them in a block or a function to keep them private.

```js
export default [{ languageOptions: { sourceType: "script" } }];
```

```js
const config = { debug: false };
class Store {}
```

## When not to use it

If all your files are modules, the only thing left is the report about built-ins such as `Promise`.
