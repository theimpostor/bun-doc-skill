# jsx-a11y/scope
Source: https://bun.com/docs/lint/rules/jsx-a11y/scope

Disallow the `scope` attribute on elements other than `<th>`


`scope` tells a screen reader whether a header cell names its column or its row. It only means something on `<th>`. On a `<td>` or anything else it's ignored, so the cell you meant as a header is read as ordinary data.

Components aren't checked.

`--fix` removes the attribute. If the cell is a header, change it to a `<th>` instead.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/scope" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const row = (
  <tr>
    <td scope="row">Total</td>
    <td>{total}</td>
  </tr>
);
```

Not reported:

```jsx
const row = (
  <tr>
    <th scope="row">Total</th>
    <td>{total}</td>
  </tr>
);
```
