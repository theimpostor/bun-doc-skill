# unicorn/prefer-date-now
Source: https://bun.com/docs/lint/rules/unicorn/prefer-date-now

Require `Date.now()` to get the current time in milliseconds


`new Date().getTime()` creates a `Date` object only to read one number from it. `Date.now()` returns the same number without the object.

Turning a `new Date()` into a number is reported too, as in `+new Date()`, `Number(new Date())`, or arithmetic such as `new Date() - start`.

`--fix` rewrites everything except the arithmetic.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-date-now" = "error" # or "warn"
```


## Examples

Reported:

```js
const start = new Date().getTime();
const stamp = +new Date();
const elapsed = new Date() - start;
```

Not reported:

```js
const start = Date.now();
const stamp = Date.now();
const elapsed = Date.now() - start;

const created = new Date(user.createdAt).getTime();
```
