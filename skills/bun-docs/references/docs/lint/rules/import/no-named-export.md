# import/no-named-export
Source: https://bun.com/docs/lint/rules/import/no-named-export

Disallow named exports, so that a module only has a default export


Some projects want each file to export one thing, as its default export. This rule reports every other export: `export const`, `export function`, `export { name }`, `export * from` and, in TypeScript, `export type` and `export interface`.

`export { name as default }` is a default export, so it's allowed.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-named-export" = "error" # or "warn"
```


## Examples

Reported:

```js
export const taxRate = 0.2;

export function formatPrice(cents) {
  return `$${(cents / 100).toFixed(2)}`;
}
```

```ts
export * from "./prices";
export type Price = number;
export interface Cart {
  total: Price;
}
```

Not reported:

```js
export default function formatPrice(cents) {
  return `$${(cents / 100).toFixed(2)}`;
}
```

```js
const formatPrice = cents => `$${(cents / 100).toFixed(2)}`;

export { formatPrice as default };
```

## When not to use it

This is the opposite of `import/no-default-export`. With both on, a module can't export anything.
