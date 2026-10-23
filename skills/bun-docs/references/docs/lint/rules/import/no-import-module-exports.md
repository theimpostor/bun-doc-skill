# import/no-import-module-exports
Source: https://bun.com/docs/lint/rules/import/no-import-module-exports

Disallow `import` declarations in a file that exports with `module.exports` or `exports.*`


In Node.js a file is either an ES module or a CommonJS module. A file with an `import` declaration is an ES module, where `module` and `exports` don't exist, so `module.exports = ...` throws a `ReferenceError`. Bundlers and transpilers that accept the mix don't agree on what a file like that exports.

The rule reports the import declarations. Any property of `module` counts, so `module.hot` in a file with imports is reported too.

A package's entry point is exempt. That's the file that `main` in the closest `package.json` points to, or its `index.js`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-import-module-exports" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-import-module-exports" = ["error", {
  exceptions = [],
}]
```


## Examples

Reported:

```js
import { parse } from "./parse";

module.exports = { run: text => parse(text) };
```

```js
import { parse } from "./parse";

exports.run = text => parse(text);
```

```js
import { render } from "./render";

if (module.hot) {
  module.hot.accept(render);
}
```

Not reported:

```js
import { parse } from "./parse";

export const run = text => parse(text);
```

```js
const { parse } = require("./parse");

module.exports = { run: text => parse(text) };
```

The entry point:

**File:** `package.json`
```json
{ "name": "runner", "main": "lib/runner.js" }
```

**File:** `lib/runner.js`
```js
import { parse } from "./parse";

module.exports = { run: text => parse(text) };
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `exceptions` | `[]` | Globs for files to skip. They're matched against the full path, so start them with `**/`. |

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-import-module-exports" = ["error", {
  exceptions = ["**/*.config.js"],
}]
```
