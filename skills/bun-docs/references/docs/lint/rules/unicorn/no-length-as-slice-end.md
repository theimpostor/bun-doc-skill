# unicorn/no-length-as-slice-end
Source: https://bun.com/docs/lint/rules/unicorn/no-length-as-slice-end

Disallow passing `.length` as the end argument of `.slice()`


Without a second argument, `.slice()` already goes to the end of the array or string. Passing the length of the same value adds nothing.

`--fix` removes the second argument.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-length-as-slice-end" = "error" # or "warn"
```


## Examples

Reported:

```js
const rest = items.slice(1, items.length);
```

Not reported:

```js
const rest = items.slice(1);
const sameSizeAsOther = items.slice(1, other.length);
const allButLast = items.slice(0, items.length - 1);
```
