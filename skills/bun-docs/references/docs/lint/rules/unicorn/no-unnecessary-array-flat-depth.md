# unicorn/no-unnecessary-array-flat-depth
Source: https://bun.com/docs/lint/rules/unicorn/no-unnecessary-array-flat-depth

Disallow passing `1` as the depth to `Array#flat()`


`flat()` flattens one level by default, so the `1` in `flat(1)` does nothing.

`--fix-suggestions` removes the argument.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-unnecessary-array-flat-depth" = "error" # or "warn"
```


## Examples

Reported:

```js
const tags = posts.map(post => post.tags).flat(1);
```

Not reported:

```js
const tags = posts.map(post => post.tags).flat();

const leaves = tree.flat(2);
const everything = tree.flat(Infinity);
```
