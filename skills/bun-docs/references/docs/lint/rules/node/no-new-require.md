# n/no-new-require
Source: https://bun.com/docs/lint/rules/node/no-new-require

Disallow `new require()`


`new require("./app")` applies `new` to `require`, not to what `require` returns. You get the class the module exports, not an instance of it.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/no-new-require" = "error" # or "warn"
```


## Examples

Reported:

```js
const app = new require("./app");
```

Not reported:

```js
const App = require("./app");
const app = new App();
```

With parentheses around the `require()` call, `new` applies to the class:

```js
const app = new (require("./app"))();
```
