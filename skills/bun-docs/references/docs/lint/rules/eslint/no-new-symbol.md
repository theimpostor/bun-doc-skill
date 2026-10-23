# no-new-symbol
Source: https://bun.com/docs/lint/rules/eslint/no-new-symbol

Disallow `new Symbol()`


`Symbol` starts with a capital letter but isn't a constructor. `new Symbol("id")` throws a `TypeError` when it runs. Call it without `new`.

ESLint has deprecated this rule. Use `no-new-native-nonconstructor` instead, which also covers `BigInt`.

## Examples

Reported:

```js
const id = new Symbol("id");
```

Not reported:

```js
const id = Symbol("id");
```
