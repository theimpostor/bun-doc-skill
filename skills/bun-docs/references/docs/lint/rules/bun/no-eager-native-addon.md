# bun/no-eager-native-addon
Source: https://bun.com/docs/lint/rules/bun/no-eager-native-addon

Disallow loading a `.node` native addon as soon as the module is loaded


A native addon is a shared library. Loading one takes time, and it throws if the file is missing or was built for another platform. If that happens at the top level of a file, everything that imports the file fails to start, even code that never calls the addon. Load it in the function that first needs it.

The rule looks at `import` and `export ... from` statements, `require()`, and `import()` with a path that ends in `.node`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-eager-native-addon" = "error" # or "warn"
```


## Examples

Reported:

```js
const native = require("./build/Release/resize.node");

export function resize(image, width) {
  return native.resize(image, width);
}
```

```js
import native from "./build/Release/resize.node";
```

Not reported:

```js
let native;

export function resize(image, width) {
  native ??= require("./build/Release/resize.node");
  return native.resize(image, width);
}
```

A type-only import doesn't load anything:

```ts
import type { Resizer } from "./build/Release/resize.node";
```
