# unicorn/no-instanceof-array
Source: https://bun.com/docs/lint/rules/unicorn/no-instanceof-array

Require `Array.isArray()` instead of `instanceof Array`


Every iframe and every `node:vm` context has its own `Array`. An array created in another one isn't an instance of yours, so `instanceof Array` is `false` for it. `Array.isArray()` is `true` for every array.

`--fix` rewrites `value instanceof Array` to `Array.isArray(value)`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-instanceof-array" = "error" # or "warn"
```


## Examples

Reported:

```js
function toList(value) {
  return value instanceof Array ? value : [value];
}
```

Not reported:

```js
function toList(value) {
  return Array.isArray(value) ? value : [value];
}
```
