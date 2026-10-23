# @typescript-eslint/no-unnecessary-type-constraint
Source: https://bun.com/docs/lint/rules/typescript/no-unnecessary-type-constraint

Disallow `extends any` and `extends unknown` on a type parameter


A type parameter without a constraint already accepts every type. `<T extends unknown>` and `<T extends any>` say the same thing with more words.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unnecessary-type-constraint" = "off" # or "error"
```


## Examples

Reported:

```ts
function first<Item extends unknown>(items: Item[]) {
  return items[0];
}

class Box<Value extends any> {
  constructor(public value: Value) {}
}

type Pair<Left, Right extends unknown> = [Left, Right];
```

Not reported:

```ts
function first<Item>(items: Item[]) {
  return items[0];
}

class Box<Value> {
  constructor(public value: Value) {}
}

function longest<Item extends { length: number }>(a: Item, b: Item) {
  return a.length >= b.length ? a : b;
}
```

In a `.tsx` file, `<Item>(item: Item) => item` reads as a JSX tag. Write a trailing comma instead of `extends unknown`:

```tsx
const identity = <Item,>(item: Item) => item;
```
