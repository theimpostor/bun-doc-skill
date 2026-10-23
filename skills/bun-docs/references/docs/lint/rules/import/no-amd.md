# import/no-amd
Source: https://bun.com/docs/lint/rules/import/no-amd

Disallow AMD `define()` and `require()` calls


AMD is RequireJS's module format: `define(["dep"], function (dep) { ... })`. Bun, Node.js and browsers don't run it without a loader, and tools can't follow its dependencies the way they follow `import`. In a project that uses ES modules, an AMD call is a leftover.

A call to `define` or `require` is reported if it has exactly two arguments and the first is an array. Only calls at the top level of a module are reported, not calls inside a function or a block. A CommonJS `require("name")` is fine.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-amd" = "error" # or "warn"
```


## Examples

Reported:

```js
define(["./logger"], function (logger) {
  logger.info("ready");
});
```

```js
require(["./logger", "./config"], function (logger, config) {
  logger.info(config.name);
});
```

Not reported:

```js
import logger from "./logger.js";
import config from "./config.js";

logger.info(config.name);
```

```js
const logger = require("./logger");

function loadLegacyPlugin(done) {
  require(["./legacy-plugin"], done);
}
```
