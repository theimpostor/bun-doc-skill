# unicorn/prefer-array-index-of
Source: https://bun.com/docs/lint/rules/unicorn/prefer-array-index-of

Require `.indexOf()` instead of `.findIndex()` when looking for a value


`.findIndex()` is for a test that `===` can't express. If the callback only compares the element with a value, `.indexOf(value)` does the same thing without a function. The same goes for `.findLastIndex()` and `.lastIndexOf()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-array-index-of" = "error" # or "warn"
```


## Examples

Reported:

```js
const index = names.findIndex(name => name === "admin");
const last = names.findLastIndex(name => name === current);
```

Not reported:

```js
const index = names.indexOf("admin");
const last = names.lastIndexOf(current);
```

A callback that compares a property of the element, or compares with `==`, isn't reported:

```js
const index = users.findIndex(user => user.name === "admin");
const loose = ids.findIndex(id => id == "7");
```
