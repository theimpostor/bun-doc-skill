# unicorn/prefer-node-protocol
Source: https://bun.com/docs/lint/rules/unicorn/prefer-node-protocol

Require the `node:` prefix when importing Node.js built-in modules


`import fs from "fs"` looks like it imports an npm package. `node:fs` makes it obvious that the module is built in.

The rule checks `import`, `export { ... } from`, `import()`, `require()` and TypeScript's `import fs = require("fs")`.

`--fix` adds the prefix.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-node-protocol" = "error" # or "warn"
```


## Examples

Reported:

```js
import fs from "fs";
import { readFile } from "fs/promises";
export { EventEmitter } from "events";

const os = await import("os");
```

Not reported:

```js
import fs from "node:fs";
import { readFile } from "node:fs/promises";
export { EventEmitter } from "node:events";

const os = await import("node:os");
```

Packages and your own files aren't reported:

```js
import express from "express";
import fs from "./fs.js";
```
