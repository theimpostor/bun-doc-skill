# symbol-description
Source: https://bun.com/docs/lint/rules/eslint/symbol-description

Require a description when creating a `Symbol`


A symbol made with `Symbol()` prints as `Symbol()` in logs and in the debugger, so you can't tell them apart. With a description it prints as `Symbol(userId)`, and `symbol.description` returns the text.

Any argument counts as a description, not only a string literal. Your own function named `Symbol` isn't checked.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"symbol-description" = "error" # or "warn"
```


## Examples

Reported:

```js
const userId = Symbol();
```

Not reported:

```js
const userId = Symbol("userId");

function makeKey(name) {
  return Symbol(name);
}
```
