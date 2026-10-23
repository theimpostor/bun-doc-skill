# react-hooks/globals
Source: https://bun.com/docs/lint/rules/react/globals

Disallow reassigning variables declared outside a component or hook during render


React decides when and how often a component renders. In development, Strict Mode renders it twice. If rendering assigns to a variable that lives outside the component, that variable's value depends on how many times React happened to render.

You can assign in an effect or an event handler, because that code doesn't run during render.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react-hooks/globals" = "error" # or "warn"
```


## Examples

Reported:

```jsx
let renderCount = 0;

function Counter() {
  renderCount = renderCount + 1;
  return <div>Rendered {renderCount} times</div>;
}
```

A function that's called during render counts too:

```jsx
let total = 0;

function Cart({ items }) {
  const add = item => {
    total = total + item.price;
  };
  items.forEach(add);
  return <div>{total}</div>;
}
```

Not reported:

```jsx
function Cart({ items }) {
  let total = 0;
  for (const item of items) {
    total = total + item.price;
  }
  return <div>{total}</div>;
}
```

```jsx
import { useEffect } from "react";

let mountedPages = 0;
let lastClicked = null;

function Page({ id }) {
  useEffect(() => {
    mountedPages = mountedPages + 1;
  }, []);
  return <button onClick={() => { lastClicked = id; }}>Open</button>;
}
```

Changing a property of an outside object is a job for `react-hooks/immutability`, not this rule:

```jsx
const config = { theme: "light" };

function Page() {
  config.theme = "dark";
  return <div className={config.theme} />;
}
```
