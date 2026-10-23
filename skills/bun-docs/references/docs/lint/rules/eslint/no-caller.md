# no-caller
Source: https://bun.com/docs/lint/rules/eslint/no-caller

Disallow `arguments.caller` and `arguments.callee`


Reading `arguments.callee` throws a `TypeError` in strict mode, and every ES module and every class body is in strict mode. `arguments.caller` is no longer part of the language.

To let a function call itself, give it a name.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-caller" = "error" # or "warn"
```


## Examples

Reported:

```js
const factorial = function (n) {
  return n <= 1 ? 1 : n * arguments.callee(n - 1);
};
```

Not reported:

```js
const factorial = function fact(n) {
  return n <= 1 ? 1 : n * fact(n - 1);
};
```
