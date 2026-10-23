# unicorn/no-unnecessary-array-splice-count
Source: https://bun.com/docs/lint/rules/unicorn/no-unnecessary-array-splice-count

Disallow `.length` or `Infinity` as the count of `splice()` and `toSpliced()`


`splice(start)` and `toSpliced(start)` already remove everything from `start` to the end of the array. Passing the array's `.length`, `Infinity` or `Number.POSITIVE_INFINITY` as the second argument does the same thing with more code.

`--fix` removes the second argument.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-unnecessary-array-splice-count" = "error" # or "warn"
```


## Examples

Reported:

```js
queue.splice(3, queue.length);
queue.splice(3, Infinity);

const firstThree = queue.toSpliced(3, Number.POSITIVE_INFINITY);
```

Not reported:

```js
queue.splice(3);

const firstThree = queue.toSpliced(3);

// a real count, the length of another array, or items to insert
queue.splice(3, 2);
queue.splice(3, removed.length);
queue.splice(3, queue.length, next);
```
