# react-hooks/refs
Source: https://bun.com/docs/lint/rules/react/refs

Disallow reading or writing `ref.current` while a component renders


React doesn't track refs. Changing `ref.current` doesn't cause a render, so output that depends on it goes stale. And because React can render a component more than once or throw a render away, a write during render can happen too often or for a render that never reaches the screen.

Read and write `ref.current` in event handlers and effects. For a value that the output depends on, use state.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react-hooks/refs" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import { useRef } from "react";

function Counter() {
  const renders = useRef(0);
  renders.current = renders.current + 1;
  return <p>Rendered {renders.current} times</p>;
}
```

Not reported:

```jsx
import { useEffect, useRef } from "react";

function SearchBox() {
  const input = useRef(null);
  useEffect(() => {
    input.current.focus();
  }, []);
  return <input ref={input} onBlur={() => console.log(input.current.value)} />;
}
```

Setting a ref once, behind a check for `null`, is allowed:

```jsx
import { useRef } from "react";

function Player() {
  const audio = useRef(null);
  if (audio.current == null) {
    audio.current = new Audio();
  }
  return <button onClick={() => audio.current.play()}>Play</button>;
}
```
