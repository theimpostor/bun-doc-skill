# require-yield
Source: https://bun.com/docs/lint/rules/eslint/require-yield

Require generator functions to contain `yield`


A generator that never yields produces no values, so a `for...of` loop over it ends right away. Either the `yield` is missing or the `*` is a mistake.

A generator with an empty body isn't reported. A `yield` in a nested generator doesn't count for the outer one.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"require-yield" = "off" # or "error"
```


## Examples

Reported:

```js
function* ids() {
  return nextId();
}
```

Not reported:

```js
function* ids() {
  while (true) {
    yield nextId();
  }
}

function* nothing() {}
```
