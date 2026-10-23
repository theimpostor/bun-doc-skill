# @typescript-eslint/prefer-for-of
Source: https://bun.com/docs/lint/rules/typescript/prefer-for-of

Require `for...of` instead of a `for` loop that only uses its index to read the array


A `for` loop with a counter has three places you can get wrong: the start, the end, and the step. If you only use the counter to read `items[i]`, a `for...of` loop gives you the element directly and has none of them.

A loop is reported if it starts at `0`, runs while `i < items.length`, goes up by one, and uses `i` in its body only to read `items[i]`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-for-of" = "error" # or "warn"
```


## Examples

Reported:

```ts
for (let i = 0; i < items.length; i++) {
  console.log(items[i]);
}
```

Not reported:

```ts
for (const item of items) {
  console.log(item);
}
```

The loop is left alone when it needs the index for something else, or when it writes to the array:

```ts
for (let i = 0; i < items.length; i++) {
  console.log(i, items[i]);
}

for (let i = 0; i < items.length; i++) {
  items[i] = 0;
}

for (let i = 0; i < items.length; i++) {
  console.log(items[i], others[i]);
}
```
