# react/forward-ref-uses-ref
Source: https://bun.com/docs/lint/rules/react/forward-ref-uses-ref

Require a component wrapped in `forwardRef` to take a `ref` parameter


`forwardRef` passes the parent's `ref` to your component as a second parameter. A component that only takes `props` drops it, so the parent's `ref.current` is never set. Either the `ref` parameter is missing or you don't need the wrapper.

The rule reports a function with exactly one parameter. Your editor offers two suggestions: add a `ref` parameter, or remove the `forwardRef` wrapper.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/forward-ref-uses-ref" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import { forwardRef } from "react";

const TextInput = forwardRef(props => {
  return <input type="text" value={props.value} />;
});
```

Not reported:

```jsx
import { forwardRef } from "react";

const TextInput = forwardRef((props, ref) => {
  return <input type="text" value={props.value} ref={ref} />;
});

const Label = props => <label>{props.text}</label>;
```
