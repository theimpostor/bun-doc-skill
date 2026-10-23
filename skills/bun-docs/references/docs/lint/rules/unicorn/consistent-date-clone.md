# unicorn/consistent-date-clone
Source: https://bun.com/docs/lint/rules/unicorn/consistent-date-clone

Require `new Date(date)` instead of `new Date(date.getTime())` to copy a date


The `Date` constructor accepts another `Date` and copies it exactly. Converting it to a number first with `.getTime()` adds a call and gives the same result.

`--fix` removes the `.getTime()` call.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/consistent-date-clone" = "error" # or "warn"
```


## Examples

Reported:

```js
const deadline = new Date(start.getTime());
deadline.setDate(deadline.getDate() + 7);
```

Not reported:

```js
const deadline = new Date(start);
deadline.setDate(deadline.getDate() + 7);
```

Arithmetic on the timestamp isn't a plain copy, so it's allowed:

```js
const deadline = new Date(start.getTime() + 60_000);
```
