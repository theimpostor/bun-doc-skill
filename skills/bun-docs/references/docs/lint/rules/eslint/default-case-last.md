# default-case-last
Source: https://bun.com/docs/lint/rules/eslint/default-case-last

Require `default` to be the last clause of a `switch`


`default` runs when no `case` matches, wherever you write it. If you put it first or in the middle, it looks like it's tested in order, and without a `break` it falls through into the `case` below it. At the end, it reads like the `else` that it is.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"default-case-last" = "error" # or "warn"
```


## Examples

Reported:

```js
switch (level) {
  default:
    log(message);
    break;
  case "error":
    alert(message);
    break;
}
```

Not reported:

```js
switch (level) {
  case "error":
    alert(message);
    break;
  default:
    log(message);
    break;
}
```
