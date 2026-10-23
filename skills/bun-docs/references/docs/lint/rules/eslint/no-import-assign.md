# no-import-assign
Source: https://bun.com/docs/lint/rules/eslint/no-import-assign

Disallow assigning to imported bindings


An import is a read-only view of what the other module exports. Assigning to it throws a `TypeError` when the line runs. The members of a namespace import (`import * as name`) are read-only too.

This rule is on by default in JavaScript files. It's off in TypeScript files, where TypeScript reports the same mistake.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-import-assign" = "off" # or "warn"
```


## Examples

Reported:

```js
import config, { retries } from "./config.js";
import * as settings from "./settings.js";

config = {};
retries += 1;
settings.debug = true;
delete settings.debug;
Object.assign(settings, { debug: true });
```

Not reported. The object that a default or a named import points to is an ordinary object, so you can change its properties. To change a variable in another module, call a function that the module exports for that purpose:

```js
import config, { setRetries } from "./config.js";

config.debug = true;
setRetries(3);
```
