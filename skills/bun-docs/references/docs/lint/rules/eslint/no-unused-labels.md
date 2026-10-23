# no-unused-labels
Source: https://bun.com/docs/lint/rules/eslint/no-unused-labels

Disallow labels that no `break` or `continue` refers to


A label only does something when a `break` or `continue` names it. If nothing names it, either the label is left over, or the `break` that should name it leaves the wrong loop.

An unused label can also be a failed object literal. In `item => { id: item.id }` the braces are a function body and `id:` is a label, so the function returns `undefined`.

`--fix` removes the label.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-unused-labels" = "off" # or "error"
```


## Examples

Reported. The `break` only leaves the inner loop:

```js
rows: for (const row of table) {
  for (const cell of row) {
    if (cell.isEmpty) break;
  }
}
```

```js
const ids = items.map(item => { id: item.id });
```

Not reported:

```js
rows: for (const row of table) {
  for (const cell of row) {
    if (cell.isEmpty) break rows;
  }
}
```

```js
const ids = items.map(item => ({ id: item.id }));
```
