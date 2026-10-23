# bun/no-side-effects-on-import
Source: https://bun.com/docs/lint/rules/bun/no-side-effects-on-import

Disallow top-level statements that call something or assign to a property


A file that does something at its top level does it for everyone who imports it. A test that imports one helper from the file also starts the server, and a bundler has to keep the file even if nothing from it is used. Export a function instead, and let the importer decide when to call it.

The rule reports a statement that isn't inside a function if it calls something, uses `new`, `import()`, or a tagged template, or assigns to, deletes, or increments a property.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-side-effects-on-import" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-side-effects-on-import" = ["error", {
  # allow = <list of strings>,
}]
```


## Examples

Reported:

```js
import { createServer } from "./server.js";

createServer().listen(3000);
```

```js
globalThis.appVersion = "1.4.0";
```

Not reported:

```js
import { createServer } from "./server.js";

export function start() {
  createServer().listen(3000);
}
```

Declarations aren't checked, so a module can still build its constants. `require()` and assigning to `module.exports` or `exports` are allowed too:

```js
require("./polyfills.js");

const cache = new Map();

module.exports = { cache };
exports.size = 100;
```

A call in the assigned value is still reported:

```js
module.exports = createApp();
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allow` | `after`, `afterAll`, `afterEach`, `before`, `beforeAll`, `beforeEach`, `describe`, `expect`, `it`, `jest`, `mock`, `suite`, `test`, `vi` | Names that can be called at the top level. It replaces the default list. |

The default list covers the functions that declare tests, hooks, and mocks, so test files pass:

```js
import { expect, mock, test } from "bun:test";

mock.module("./database.js", () => ({ connect: mock() }));

test.each([1, 2])("is positive", value => {
  expect(value).toBeGreaterThan(0);
});
```

A plain name such as `"test"` allows everything that starts with it, like `test()` and `test.each()()`. A name with a dot such as `"customElements.define"` only allows that call:

```js
customElements.define("user-card", UserCard);
```

```js
customElements.upgrade(document.body);
```

## When not to use it

An entry point, a script, or a polyfill exists to do something when it runs. Turn the rule off for those files.
