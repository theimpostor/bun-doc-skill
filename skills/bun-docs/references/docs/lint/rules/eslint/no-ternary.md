# no-ternary
Source: https://bun.com/docs/lint/rules/eslint/no-ternary

Disallow the `? :` operator


`test ? a : b` puts a branch in the middle of an expression. Some teams find `if` and `else` easier to read, step through in a debugger and extend later, so they ban the operator everywhere. This rule reports every use of it.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-ternary" = "error" # or "warn"
```


## Examples

Reported:

```js
const label = count === 1 ? "item" : "items";
```

Not reported:

```js
let label = "items";
if (count === 1) {
  label = "item";
}
```

## When not to use it

A short ternary is often the clearest way to choose between two values, and it lets the variable stay `const`. If only the nested ones bother you, use `no-nested-ternary`.
