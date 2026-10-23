# n/global-require
Source: https://bun.com/docs/lint/rules/node/global-require

Require `require()` calls to be at the top level of the file


`require()` loads a module synchronously. Inside a function, it reads from disk and blocks the first time that function runs, and a missing module throws then instead of at startup. It also hides what the file depends on.

A `require()` inside a function, an `if`, a `try` or any other block is reported. A `require` that the file declares itself isn't.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/global-require" = "error" # or "warn"
```


## Examples

Reported:

```js
function readConfig(file) {
  const fs = require("fs");
  return fs.readFileSync(file, "utf8");
}

if (process.env.DEBUG) {
  require("./debug");
}
```

Not reported:

```js
const fs = require("fs");
const join = require("path").join;
const log = require("./log")("config");
const debug = process.env.DEBUG ? require("./debug") : null;

function readConfig(file) {
  return fs.readFileSync(file, "utf8");
}
```

At the top level, a `require()` inside an object or array literal, or after `&&` or `||`, is reported too. Put it in its own variable:

```js
module.exports = {
  parse: require("./parse"),
};

const debug = process.env.DEBUG && require("./debug");
```

## When not to use it

Loading a heavy or optional module only when you need it is a good reason to call `require()` inside a function. Turn the rule off for that line.
