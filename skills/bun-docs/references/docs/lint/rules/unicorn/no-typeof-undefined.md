# unicorn/no-typeof-undefined
Source: https://bun.com/docs/lint/rules/unicorn/no-typeof-undefined

Require comparing with `undefined` directly instead of `typeof x === "undefined"`


`typeof value === "undefined"` is a long way to write `value === undefined`. You only need `typeof` for a name that may not be declared at all, where reading it throws a `ReferenceError`. That's why a variable that isn't declared in the file isn't reported by default.

`--fix` rewrites the comparison to `=== undefined` or `!== undefined`. For a variable that isn't declared in the file, only `--fix-suggestions` does.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-typeof-undefined" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-typeof-undefined" = ["error", {
  checkGlobalVariables = false,
}]
```


## Examples

Reported:

```js
function greet(name, options) {
  if (typeof name === "undefined") {
    name = "stranger";
  }
  return typeof options.loud !== "undefined";
}
```

Not reported:

```js
function greet(name, options) {
  if (name === undefined) {
    name = "stranger";
  }
  return options.loud !== undefined;
}

// `window` is not declared in this file
const isServer = typeof window === "undefined";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `checkGlobalVariables` | `false` | Also report `typeof` on a variable that isn't declared in the file. |

```js
const isServer = typeof window === "undefined";
```
