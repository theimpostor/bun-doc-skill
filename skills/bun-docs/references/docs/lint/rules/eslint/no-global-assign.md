# no-global-assign
Source: https://bun.com/docs/lint/rules/eslint/no-global-assign

Disallow assigning to built-in and other read-only global variables


Assigning to a global such as `Promise` or `window` replaces it for all the code that runs afterwards, including libraries. More often it's an accident. A `const` or `let` is missing, and the name you picked is already a browser global.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-global-assign" = "off" # or "error"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-global-assign" = ["warn", {
  exceptions = [], # list of strings
}]
```


## Examples

Reported:

```js
Promise = loadPromiseLibrary();
window = createFakeWindow();
status = "ready";
```

Not reported:

```js
const Promise = loadPromiseLibrary();
let status = "ready";
status = "done";
```

A global that's declared as writable can be assigned:

```js
/* global analytics:writable */
analytics = createAnalytics();
```

```js
/* global analytics:readonly */
analytics = createAnalytics();
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `exceptions` | `[]` | Names of read-only globals that can be assigned. |

```js
Promise = loadPromiseLibrary();
```
