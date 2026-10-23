# import/no-absolute-path
Source: https://bun.com/docs/lint/rules/import/no-absolute-path

Disallow importing a module by an absolute file system path


An absolute path such as `/home/ana/app/src/config.js` only exists on the machine where it was written. The import breaks for everyone else who clones the project, in CI, and in production.

`--fix` rewrites the path to one that's relative to the importing file.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-absolute-path" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-absolute-path" = ["error", {
  esmodule = true,
  commonjs = true,
  amd = false,
  # ignore = <list of strings>,
}]
```


## Examples

Reported:

```js
import config from "/home/ana/app/src/config.js";

const logger = require("/home/ana/app/src/logger.js");
```

Not reported:

```js
import config from "./config.js";
import express from "express";

const logger = require("../lib/logger.js");
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `esmodule` | `true` | Check `import`, `export ... from` and `import()`. |
| `commonjs` | `true` | Check `require()`. |
| `amd` | `false` | Check the dependency lists of AMD `define()` and `require()` calls. |
| `ignore` | `[]` | Regular expressions. A path that matches one of them isn't checked. |

```js
const logger = require("/home/ana/app/src/logger.js");
```

```js
define(["/home/ana/app/src/logger.js"], function (logger) {
  logger.info("ready");
});
```

## When not to use it

Some dev servers and bundlers read a path that starts with `/` as relative to the project or its public folder. Exempt those paths with `ignore`, or leave the rule off.

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-absolute-path" = ["error", { ignore = ["^/assets/"] }]
```

```js
import logo from "/assets/logo.svg";
```
