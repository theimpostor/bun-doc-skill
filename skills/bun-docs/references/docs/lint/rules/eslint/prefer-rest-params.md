# prefer-rest-params
Source: https://bun.com/docs/lint/rules/eslint/prefer-rest-params

Require rest parameters instead of `arguments`


`arguments` looks like an array but isn't one. It has no `map`, `slice` or `join`. And `function log(level)` doesn't show that the function takes more than one argument. A rest parameter such as `...parts` is a real array, and you can see it in the signature.

Reading a named property, such as `arguments.length`, isn't reported.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"prefer-rest-params" = "off" # or "error"
```


## Examples

Reported:

```js
function log(level) {
  const parts = Array.prototype.slice.call(arguments, 1);
  console.log(level, parts.join(" "));
}
```

Not reported:

```js
function log(level, ...parts) {
  console.log(level, parts.join(" "));
}

function hasOptions() {
  return arguments.length > 1;
}
```
