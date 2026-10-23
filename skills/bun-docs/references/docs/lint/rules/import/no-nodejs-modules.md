# import/no-nodejs-modules
Source: https://bun.com/docs/lint/rules/import/no-nodejs-modules

Disallow importing Node.js builtin modules such as `fs` and `path`


Browsers don't have an `fs`, `path` or `crypto` module. Importing one either breaks the bundle or pulls in a large polyfill. Turn this rule on for the files that ship to the client.

It checks `import`, `export ... from`, `import()` and `require()`, with and without the `node:` prefix.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-nodejs-modules" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-nodejs-modules" = ["error", {
  allow = [], # list of strings
}]
```


## Examples

Reported:

```js
import fs from "fs";
import { join } from "node:path";

const os = require("os");
```

Not reported:

```js
import { format } from "date-fns";
import { cart } from "./cart";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allow` | `[]` | Builtin modules you can import, spelled the way the import spells them. `"path"` doesn't allow `"node:path"`. |

```js
import { join } from "node:path";
```

```js
import { join } from "path";
```
