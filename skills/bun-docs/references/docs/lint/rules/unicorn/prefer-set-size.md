# unicorn/prefer-set-size
Source: https://bun.com/docs/lint/rules/unicorn/prefer-set-size

Require `Set#size` instead of converting the `Set` to an array to read `length`


`[...set].length` copies every item in the `Set` into a new array, reads one number and throws the array away. A `Set` already knows how many items it has, and `set.size` tells you.

The rule reports `[...set].length` and `Array.from(set).length` when `set` is a `new Set()` or a `const` that's initialized with one.

`--fix` rewrites it to `.size`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-set-size" = "error" # or "warn"
```


## Examples

Reported:

```js
const uniqueCount = [...new Set(tags)].length;

const visitors = new Set(ids);
console.log(Array.from(visitors).length);
```

Not reported:

```js
const uniqueCount = new Set(tags).size;

const visitors = new Set(ids);
console.log(visitors.size);
```

If the rule can't tell that the value is a `Set`, it doesn't report anything:

```js
function count(values) {
  return [...values].length;
}
```
