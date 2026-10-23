# react/no-clone-element
Source: https://bun.com/docs/lint/rules/react/no-clone-element

Disallow `React.cloneElement`


`cloneElement` adds props to an element that was created somewhere else. Anyone reading `<Row />` can't see that it receives `isSelected`, and the extra props are lost as soon as someone wraps the child in another component. Pass the data with a render prop or with context instead.

The rule only reports a `cloneElement` that's imported from `"react"`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-clone-element" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import React, { Children, cloneElement } from "react";

function List({ children, selected }) {
  return Children.map(children, (child, i) => cloneElement(child, { isSelected: i === selected }));
}

const disabled = React.cloneElement(<Button />, { disabled: true });
```

Not reported:

```jsx
function List({ items, selected, renderItem }) {
  return items.map((item, i) => renderItem(item, i === selected));
}

const list = (
  <List
    items={rows}
    selected={0}
    renderItem={(row, isSelected) => <Row key={row.id} isSelected={isSelected} />}
  />
);
```
