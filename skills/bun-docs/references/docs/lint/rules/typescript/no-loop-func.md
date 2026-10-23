# @typescript-eslint/no-loop-func
Source: https://bun.com/docs/lint/rules/typescript/no-loop-func

Disallow functions in loops that use a variable the loop changes


A function keeps the variable it uses, not the value the variable had when the function was created. If a loop creates functions that use a `var`, or a `let` declared outside the loop, and the loop changes that variable, every one of them sees the last value.

A `const` never changes, and a `let` declared in the loop is new in each iteration, so both are safe. A function that's called right where it's written isn't reported either.

This rule is deprecated. Use `no-loop-func` instead.

## Examples

Reported:

```ts
const handlers: Array<() => void> = [];

for (var i = 0; i < 3; i++) {
  handlers.push(() => console.log(i)); // 3, 3, 3
}
```

```ts
const prices = [5, 10, 20];
const totals: Array<() => number> = [];
let total = 0;

for (const price of prices) {
  total += price;
  totals.push(() => total); // 35, 35, 35
}
```

Not reported:

```ts
const handlers: Array<() => void> = [];

for (let i = 0; i < 3; i++) {
  handlers.push(() => console.log(i)); // 0, 1, 2
}
```

```ts
const prices = [5, 10, 20];
const totals: Array<() => number> = [];
let total = 0;

for (const price of prices) {
  total += price;
  const soFar = total;
  totals.push(() => soFar); // 5, 15, 35
}
```
