# unicorn/no-instanceof-builtins
Source: https://bun.com/docs/lint/rules/unicorn/no-instanceof-builtins

Disallow `instanceof` with built-in constructors such as `Array`, `String`, and `Function`


`instanceof` gives the wrong answer for built-ins in two ways. First, a primitive is never an instance, so `"text" instanceof String` is `false`. Second, every iframe and every `node:vm` context has its own built-ins, so an array or a function from another one isn't an instance of your `Array` or `Function`.

By default, the rule reports `instanceof` with `Array`, `Function`, `String`, `Number`, `Boolean`, `BigInt`, and `Symbol`. `--fix-suggestions` rewrites these to `Array.isArray(value)` or a `typeof` check.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-instanceof-builtins" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-instanceof-builtins" = ["error", {
  strategy = "loose",
  useErrorIsError = false,
  include = [], # list of strings
  exclude = [],
}]
```


## Examples

Reported:

```js
function describe(value) {
  if (value instanceof String) return "text";
  if (value instanceof Function) return "callback";
}
```

Not reported:

```js
function describe(value) {
  if (typeof value === "string") return "text";
  if (typeof value === "function") return "callback";
  if (value instanceof Map) return "map";
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `strategy` | `"loose"` | `"strict"` also reports the error classes, `Map`, `Set`, `Date`, `RegExp`, `Promise`, `Object`, the typed arrays, and other built-in classes. |
| `useErrorIsError` | `false` | Also report `instanceof Error`, and suggest `Error.isError(value)`. |
| `include` | `[]` | More constructor names to report. |
| `exclude` | `[]` | Constructor names to never report. |

```js
if (value instanceof Date || value instanceof TypeError) {
  log(value);
}
```

```js
if (reason instanceof Error) {
  log(reason.message);
}
```

```js
if (target instanceof HTMLElement) {
  target.focus();
}
```
