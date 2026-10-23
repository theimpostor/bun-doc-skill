# react-hooks/exhaustive-effect-dependencies
Source: https://bun.com/docs/lint/rules/react/exhaustive-effect-dependencies

Require the dependency array of an effect to match what the effect reads


An effect runs again only when something in its dependency array changes. If the effect reads a value that's missing from the array, it doesn't run when that value changes and keeps working with the old one. If the array lists a value the effect never reads, the effect runs more often than it needs to.

This check comes from the React Compiler, which works out what each effect in a component or hook depends on and compares that with your array.

In `.ts` and `.tsx` files, the report comes with a suggestion that rewrites the array, which your editor can apply.

With an ESLint config the rule reports nothing, because `eslint-plugin-react-hooks` leaves this compiler check switched off. Use `react-hooks/exhaustive-deps` there.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react-hooks/exhaustive-effect-dependencies" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import { useEffect } from "react";

function Room({ roomId }) {
  useEffect(() => {
    connect(roomId);
  }, []); // stays in the first room
}
```

```jsx
import { useEffect } from "react";

function Room({ roomId, theme }) {
  useEffect(() => {
    connect(roomId);
  }, [roomId, theme]); // reconnects when the theme changes
}
```

Not reported:

```jsx
import { useEffect } from "react";

function Room({ roomId }) {
  useEffect(() => {
    connect(roomId);
  }, [roomId]);
}
```
