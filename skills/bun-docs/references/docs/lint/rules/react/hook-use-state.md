# react/hook-use-state
Source: https://bun.com/docs/lint/rules/react/hook-use-state

Require `useState` to be destructured into a `[value, setValue]` pair


`useState` returns a value and the function that updates it. When the two names don't match, as in `[color, setFlavor]`, you can't tell which setter belongs to which state. When you keep the result in one variable, every use becomes `state[0]` and `state[1]`.

The setter's name must be `set` followed by the value's name with a capital first letter. The rule only looks at `useState` and `React.useState` imported from `"react"`. A `useState()` call that's returned directly, as in a custom hook, is allowed.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/hook-use-state" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/hook-use-state" = ["error", {
  allowDestructuredState = false,
}]
```


## Examples

Reported:

```jsx
import React, { useState } from "react";

function Picker() {
  const color = useState("red");
  const [size, updateSize] = React.useState(1);
  const [open] = useState(false);
  return <div />;
}
```

Not reported:

```jsx
import { useState } from "react";

function Picker() {
  const [color, setColor] = useState("red");
  const [size, setSize] = useState(1);
  return <div />;
}

function useToggle() {
  return useState(false);
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowDestructuredState` | `false` | Allow the value to be destructured further. The setter can then have any name. |

```jsx
import { useState } from "react";

function Profile() {
  const [{ name, email }, setUser] = useState({ name: "", email: "" });
  return <div />;
}
```

```jsx
import { useState } from "react";

function Profile() {
  const [{ name, email }, setUser] = useState({ name: "", email: "" });
  return <div />;
}
```
