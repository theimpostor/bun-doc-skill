# n/no-mixed-requires
Source: https://bun.com/docs/lint/rules/node/no-mixed-requires

Disallow `require()` calls mixed with other variables in one declaration


A declaration that lists modules and ordinary variables together makes it hard to see what the file depends on. This rule wants the `require()` calls in their own declaration.

`require("x")` and a property of it, such as `require("x").y`, count as a `require()`. Everything else is an ordinary variable, including one without a value.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/no-mixed-requires" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/no-mixed-requires" = ["error", {
  grouping = false,
  allowCall = false,
}]
```


## Examples

Reported:

```js
const fs = require("fs"),
  retries = 3;
```

Not reported:

```js
const fs = require("fs"),
  join = require("path").join;

const retries = 3;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `grouping` | `false` | Also report a declaration that mixes kinds of modules: Node.js built-ins, packages, files (`./`, `../`, `/`), and computed names. |
| `allowCall` | `false` | Count a module that's called right away, such as `require("debug")("app")`, as a `require()`. |

You can write `true` instead of `{ "grouping": true }`.

```js
const fs = require("fs"),
  express = require("express"),
  routes = require("./routes");
```

```js
const fs = require("fs"),
  path = require("path");

const express = require("express");

const routes = require("./routes");
```

A name with the `node:` prefix counts as a package, not as a built-in:

```js
const fs = require("node:fs"),
  path = require("path");
```

Without `allowCall`, a module that's called counts as an ordinary variable:

```js
const express = require("express"),
  debug = require("debug")("app");
```

```js
const express = require("express"),
  debug = require("debug")("app");
```
