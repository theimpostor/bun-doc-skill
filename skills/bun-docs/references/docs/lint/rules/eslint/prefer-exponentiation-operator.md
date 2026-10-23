# prefer-exponentiation-operator
Source: https://bun.com/docs/lint/rules/eslint/prefer-exponentiation-operator

Require the `**` operator instead of `Math.pow()`


`Math.pow(base, exponent)` and `base ** exponent` compute the same number. The operator is shorter, reads like the arithmetic around it, and also works with `BigInt`, where `Math.pow` throws.

`--fix` rewrites the call and adds parentheses where the result needs them.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"prefer-exponentiation-operator" = "error" # or "warn"
```


## Examples

Reported:

```js
const area = Math.PI * Math.pow(radius, 2);
const distance = Math.sqrt(Math.pow(dx, 2) + Math.pow(dy, 2));
```

Not reported:

```js
const area = Math.PI * radius ** 2;
const distance = Math.sqrt(dx ** 2 + dy ** 2);
```
