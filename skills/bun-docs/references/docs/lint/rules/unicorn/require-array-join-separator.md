# unicorn/require-array-join-separator
Source: https://bun.com/docs/lint/rules/unicorn/require-array-join-separator

Require the separator argument of `Array#join()`


Without an argument, `join()` puts a comma between the items. A reader might expect no separator at all, or a comma and a space. Writing the separator out removes the guesswork.

The rule only looks at the method name, so it reports `.join()` without arguments on any object. It also reports `Array.prototype.join.call(items)` and `[].join.call(items)`.

`--fix` adds `","`, which keeps the result the same.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/require-array-join-separator" = "error" # or "warn"
```


## Examples

Reported:

```js
const header = columns.join();
const names = Array.prototype.join.call(arguments);
```

Not reported:

```js
const header = columns.join(",");
const names = Array.prototype.join.call(arguments, ", ");
const word = letters.join("");
```
