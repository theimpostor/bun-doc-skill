# unicorn/no-unreadable-iife
Source: https://bun.com/docs/lint/rules/unicorn/no-unreadable-iife

Disallow calling an arrow function in place when its body is in parentheses


`(() => (value))()` ends in a pile of parentheses. It's hard to see which pair closes the body, which closes the function and which calls it. A block body with `return` reads better. Often you don't need the function at all.

`--fix-suggestions` turns the body into `{ return ...; }`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-unreadable-iife" = "error" # or "warn"
```


## Examples

Reported:

```js
const label = (() => (count === 1 ? "item" : "items"))();
```

Not reported:

```js
const label = (() => {
  return count === 1 ? "item" : "items";
})();

const plain = count === 1 ? "item" : "items";

// no parentheses around the body
const now = (() => Date.now())();

// not called in place
const toPoint = (x, y) => ({ x, y });
```
