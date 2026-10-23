# react/react-in-jsx-scope
Source: https://bun.com/docs/lint/rules/react/react-in-jsx-scope

Require `React` to be in scope in files that use JSX


With the classic JSX transform, `<App />` compiles to `React.createElement(App)`. If the file doesn't import `React`, that line throws `ReferenceError: React is not defined` when it runs.

If the file has a `@jsx` comment, or you set `settings.react.pragma` (`[lint.settings.react]` in `bunfig.toml`, or `settings` in an ESLint config), the rule looks for that name instead of `React`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/react-in-jsx-scope" = "error" # or "warn"
```


## Examples

Reported:

```jsx
export function App() {
  return <h1>Hello</h1>;
}
```

Not reported:

```jsx
import React from "react";

export function App() {
  return <h1>Hello</h1>;
}
```

```jsx
/** @jsx h */
import { h } from "preact";

export function App() {
  return <h1>Hello</h1>;
}
```

## When not to use it

Turn it off if you use the automatic JSX transform (`"jsx": "react-jsx"` in `tsconfig.json`), which is what Bun does by default. That transform imports what it needs by itself, so `React` doesn't need to be in scope.
