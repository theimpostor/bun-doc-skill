# no-extra-label
Source: https://bun.com/docs/lint/rules/eslint/no-extra-label

Disallow labels on `break` and `continue` that name the innermost loop or `switch`


`break` and `continue` without a label already apply to the innermost loop or `switch`. Naming that same statement's label changes nothing, and it sends the reader looking for an outer loop that isn't there.

`--fix` removes the label after `break` or `continue`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-extra-label" = "error" # or "warn"
```


## Examples

Reported:

```js
search: for (const item of items) {
  if (item.id === id) {
    select(item);
    break search;
  }
}
```

Not reported:

```js
for (const item of items) {
  if (item.id === id) {
    select(item);
    break;
  }
}
```

You do need a label to leave an outer loop from an inner one:

```js
rows: for (const row of table) {
  for (const cell of row) {
    if (cell === target) {
      break rows;
    }
  }
}
```
