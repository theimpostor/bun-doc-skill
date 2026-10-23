# promise/avoid-new
Source: https://bun.com/docs/lint/rules/promise/avoid-new

Disallow creating promises with `new Promise()`


With `new Promise()`, you settle the promise by hand. A path that doesn't call `resolve` or `reject` leaves a promise that never settles, and anything that awaits it waits forever. An `async` function, or an API that already returns a promise, settles it for you.

Only the global `Promise` counts. `Promise.resolve()`, `Promise.all()` and the other static methods aren't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/avoid-new" = "error" # or "warn"
```


## Examples

Reported:

```js
import fs from "node:fs";

function readConfig(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, "utf8", (err, text) => {
      if (err) reject(err);
      else resolve(text);
    });
  });
}
```

Not reported:

```js
import { readFile } from "node:fs/promises";

function readConfig(path) {
  return readFile(path, "utf8");
}
```

## When not to use it

You need `new Promise()` to wrap a timer, an event, or a library that only takes callbacks. If your code does that in more than a few places, leave this rule off.
