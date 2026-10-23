# @typescript-eslint/no-unsafe-unary-minus
Source: https://bun.com/docs/lint/rules/typescript/no-unsafe-unary-minus

Require the operand of unary `-` to be a number or a bigint


`-value` converts `value` to a number first. For a string that isn't numeric, an object, or an array with several items, the result is `NaN`. TypeScript accepts it without an error.

A union is reported if any of its members isn't a number or a bigint. `any` isn't reported.

`bun lint --type-aware` turns this rule on in TypeScript files.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unsafe-unary-minus" = "error" # or "warn"
```


## Examples

Reported:

```ts
function refund(amount: string) {
  return -amount;
}
```

```ts
function flip(offset: number | string) {
  return -offset;
}
```

Not reported:

```ts
function refund(amount: string) {
  return -Number(amount);
}

function flip(offset: number | bigint) {
  return -offset;
}
```
