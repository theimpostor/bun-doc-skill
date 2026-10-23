# react/display-name
Source: https://bun.com/docs/lint/rules/react/display-name

Require every component to have a name that React can show


React DevTools, warnings, and component stacks show a component by its name. A component without one shows up as `Anonymous` or `Unknown`, so you can't tell which one failed.

React takes the name from the function or class, or from the variable it's assigned to. So the rule mostly reports anonymous functions that are exported directly or passed to `memo` or `forwardRef`. A `displayName` property also counts.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/display-name" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/display-name" = ["error", {
  ignoreTranspilerName = false,
  checkContextObjects = false,
}]
```


## Examples

Reported:

```jsx
export default () => <nav>Menu</nav>;
```

```jsx
import { forwardRef } from "react";

export const TextField = forwardRef((props, ref) => <input ref={ref} {...props} />);
```

Not reported:

```jsx
export default function Menu() {
  return <nav>Menu</nav>;
}
```

```jsx
import { forwardRef } from "react";

export const TextField = forwardRef(function TextField(props, ref) {
  return <input ref={ref} {...props} />;
});

export const Search = forwardRef((props, ref) => <input type="search" ref={ref} {...props} />);
Search.displayName = "Search";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreTranspilerName` | `false` | Don't count the name of the function, class, or variable. Only an explicit `displayName` counts. |
| `checkContextObjects` | `false` | Also require a `displayName` on the result of `createContext()`. |

```jsx
export default function Menu() {
  return <nav>Menu</nav>;
}
```

```jsx
export default function Menu() {
  return <nav>Menu</nav>;
}
Menu.displayName = "Menu";
```

```jsx
import { createContext } from "react";

const ThemeContext = createContext("light");
```

```jsx
import { createContext } from "react";

const ThemeContext = createContext("light");
ThemeContext.displayName = "ThemeContext";
```
