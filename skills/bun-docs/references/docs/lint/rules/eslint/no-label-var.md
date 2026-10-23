# no-label-var
Source: https://bun.com/docs/lint/rules/eslint/no-label-var

Disallow labels that share a name with a variable


Labels and variables live in separate namespaces, so a label can have the same name as a variable that's in scope. Then the same word means two things a few lines apart. `continue rows` jumps to the label, and `rows.length` reads the variable.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-label-var" = "error" # or "warn"
```


## Examples

Reported:

```js
const rows = table.rows;

rows: for (const row of rows) {
  for (const cell of row.cells) {
    if (cell.isEmpty) continue rows;
  }
  print(row);
}
```

Not reported:

```js
const rows = table.rows;

eachRow: for (const row of rows) {
  for (const cell of row.cells) {
    if (cell.isEmpty) continue eachRow;
  }
  print(row);
}
```

Globals count as variables too. `top` is a global in browsers:

```js
top: for (const row of table.rows) {
  for (const cell of row.cells) {
    if (cell.isEmpty) continue top;
  }
  print(row);
}
```
