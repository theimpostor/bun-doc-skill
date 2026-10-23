# react-hooks/preserve-manual-memoization
Source: https://bun.com/docs/lint/rules/react/preserve-manual-memoization

Disallow `useMemo` and `useCallback` calls that React Compiler cannot keep memoized


React Compiler replaces your `useMemo` and `useCallback` calls with its own caching. If it can't cache a value that you memoized by hand, it skips the whole component rather than make it slower, and nothing in that component is optimized.

The usual cause is a dependency that the compiler can't cache, such as an object that's created before a hook call and changed after it. That object is new on every render, so the `useMemo` that depends on it never reuses its result.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react-hooks/preserve-manual-memoization" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import { useMemo } from "react";

function Table({ rows }) {
  const columns = ["name"];
  const isWide = useIsWide();
  if (isWide) {
    columns.push("email");
  }
  const header = useMemo(() => columns.map(name => name.toUpperCase()), [columns]);
  return <Grid header={header} rows={rows} />;
}
```

Not reported:

```jsx
import { useMemo } from "react";

function Table({ rows }) {
  const isWide = useIsWide();
  const columns = isWide ? ["name", "email"] : ["name"];
  const header = useMemo(() => columns.map(name => name.toUpperCase()), [columns]);
  return <Grid header={header} rows={rows} />;
}
```

## When not to use it

This rule only matters if you build with React Compiler.
