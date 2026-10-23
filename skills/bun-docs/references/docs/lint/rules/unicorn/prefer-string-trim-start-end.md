# unicorn/prefer-string-trim-start-end
Source: https://bun.com/docs/lint/rules/unicorn/prefer-string-trim-start-end

Require `trimStart()` and `trimEnd()` instead of `trimLeft()` and `trimRight()`


`trimLeft()` and `trimRight()` are old aliases for `trimStart()` and `trimEnd()`. The names are also wrong for text written from right to left, where the start of the string is on the right.

`--fix` renames the method.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-string-trim-start-end" = "error" # or "warn"
```


## Examples

Reported:

```js
const command = input.trimLeft();
const line = text.trimRight();
```

Not reported:

```js
const command = input.trimStart();
const line = text.trimEnd();
```
