# unicorn/no-useless-collection-argument
Source: https://bun.com/docs/lint/rules/unicorn/no-useless-collection-argument

Disallow empty arguments and fallbacks in `new Set()`, `Map`, `WeakSet`, and `WeakMap`


`new Set()`, `new Map()`, `new WeakSet()` and `new WeakMap()` make an empty collection when they get no argument, `undefined` or `null`. So `new Set([])` passes an array for nothing, and the fallback in `new Set(items ?? [])` never changes the result.

The rule reports `[]`, `""`, `null` and `undefined`, either as the only argument or on the right of `??`.

`--fix-suggestions` removes the argument or the fallback.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-useless-collection-argument" = "error" # or "warn"
```


## Examples

Reported:

```js
const seen = new Set([]);
const cache = new Map(undefined);

function unique(items) {
  return new Set(items ?? []);
}
```

Not reported:

```js
const seen = new Set();
const cache = new Map();

function unique(items) {
  return new Set(items);
}

const defaults = new Set(items ?? ["all"]);
```
