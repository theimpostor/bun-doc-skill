# unicorn/no-unnecessary-slice-end
Source: https://bun.com/docs/lint/rules/unicorn/no-unnecessary-slice-end

Disallow `.length` or `Infinity` as the end of `slice()`


`slice(start)` already goes to the end of the array or string. Passing the value's `.length`, `Infinity` or `Number.POSITIVE_INFINITY` as the second argument does the same thing with more code.

`--fix` removes the second argument.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-unnecessary-slice-end" = "error" # or "warn"
```


## Examples

Reported:

```js
const rest = items.slice(1, items.length);
const extension = filename.slice(dot, Infinity);
const tail = lines.slice(-5, Number.POSITIVE_INFINITY);
```

Not reported:

```js
const rest = items.slice(1);
const extension = filename.slice(dot);
const tail = lines.slice(-5);

// a real end, or the length of something else
const page = items.slice(0, 10);
const prefix = filename.slice(0, base.length);
```
