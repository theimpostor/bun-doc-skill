# no-negated-in-lhs
Source: https://bun.com/docs/lint/rules/eslint/no-negated-in-lhs

Disallow negating the left operand of `in`


`!` binds tighter than `in`, so `!key in cache` means `(!key) in cache`. It asks whether `cache` has a property named `"true"` or `"false"`, which is almost never the question. The negation belongs around the whole test.

ESLint has deprecated this rule. Use `no-unsafe-negation` instead, which also covers `instanceof`.

## Examples

Reported:

```js
if (!key in cache) {
  cache[key] = load(key);
}
```

Not reported:

```js
if (!(key in cache)) {
  cache[key] = load(key);
}
```
