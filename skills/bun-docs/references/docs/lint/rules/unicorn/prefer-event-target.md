# unicorn/prefer-event-target
Source: https://bun.com/docs/lint/rules/unicorn/prefer-event-target

Require `EventTarget` instead of `EventEmitter`


`EventEmitter` comes from `node:events`, so code that uses it needs a polyfill to run in a browser. `EventTarget` is a global in browsers, Bun, Node.js and Deno. It doesn't need an import and adds nothing to a bundle.

The rule goes by the name, so it reports `new EventEmitter()` and `extends EventEmitter`. An `EventEmitter` that comes from `eventemitter3` or `@angular/core` isn't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-event-target" = "error" # or "warn"
```


## Examples

Reported:

```js
import { EventEmitter } from "node:events";

class Download extends EventEmitter {}

const bus = new EventEmitter();
```

Not reported:

```js
class Download extends EventTarget {}

const bus = new EventTarget();
bus.addEventListener("done", () => console.log("done"));
bus.dispatchEvent(new Event("done"));
```

```js
import { EventEmitter } from "eventemitter3";

const bus = new EventEmitter();
```

## When not to use it

The two aren't drop-in replacements. `emit()` passes any arguments to the listeners, and `dispatchEvent()` passes one `Event` object. For code that only runs in Bun or Node.js, `EventEmitter` is fine.
