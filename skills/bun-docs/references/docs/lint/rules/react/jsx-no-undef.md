# react/jsx-no-undef
Source: https://bun.com/docs/lint/rules/react/jsx-no-undef

Disallow components in JSX that are not declared or imported


`<Header />` reads a variable named `Header`. If nothing declares or imports it, usually because of a typo or a forgotten import, rendering throws a `ReferenceError`.

Names that start with a lowercase letter, such as `<div>` or `<my-element>`, are HTML elements, so the rule skips them. In `<Menu.Item>`, it only checks `Menu`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-no-undef" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-no-undef" = ["error", {
  allowGlobals = false,
}]
```


## Examples

Reported:

```jsx
export function Page() {
  return <Header title="Home" />;
}
```

Not reported:

```jsx
import { Header } from "./header";

export function Page() {
  return <Header title="Home" />;
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowGlobals` | `false` | Accept components that are global variables. |

By default a global doesn't count in a module, even one you declared:

```jsx
/* global Header */

export function Page() {
  return <Header title="Home" />;
}
```

```jsx
/* global Header */

export function Page() {
  return <Header title="Home" />;
}
```
