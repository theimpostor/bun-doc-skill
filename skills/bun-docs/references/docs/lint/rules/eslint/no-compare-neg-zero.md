# no-compare-neg-zero
Source: https://bun.com/docs/lint/rules/eslint/no-compare-neg-zero

Disallow comparing against `-0`


`0` and `-0` compare as equal, so `x === -0` is also `true` when `x` is `0`. The minus sign has no effect.

To tell the two apart, use `Object.is(x, -0)`. Otherwise compare with `0`.

This rule is on by default.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-compare-neg-zero" = "off" # or "warn"
```


## Examples

Reported:

```js
if (offset === -0) {
  flipDirection();
}
```

Not reported:

```js
if (Object.is(offset, -0)) {
  flipDirection();
}

if (offset === 0) {
  stop();
}
```

`<`, `<=`, `>` and `>=` are reported too:

```js
const isForward = speed >= -0;
```
