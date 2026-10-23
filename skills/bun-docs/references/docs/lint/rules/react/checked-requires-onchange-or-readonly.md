# react/checked-requires-onchange-or-readonly
Source: https://bun.com/docs/lint/rules/react/checked-requires-onchange-or-readonly

Require `onChange` or `readOnly` on an `input` that has `checked`


An `<input>` with `checked` is controlled by React. Without an `onChange` that updates the value, a click does nothing and the box looks broken. React also logs a warning for it.

The rule also reports an `<input>` with both `checked` and `defaultChecked`. The first says React controls the value, and the second says it doesn't. `React.createElement("input", ...)` is checked too.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/checked-requires-onchange-or-readonly" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/checked-requires-onchange-or-readonly" = ["error", {
  ignoreMissingProperties = false,
  ignoreExclusiveCheckedAttribute = false,
}]
```


## Examples

Reported:

```jsx
<input type="checkbox" checked={isSubscribed} />;
```

```jsx
<input type="checkbox" checked={isSubscribed} defaultChecked onChange={toggle} />;
```

Not reported:

```jsx
const controlled = <input type="checkbox" checked={isSubscribed} onChange={toggle} />;
const fixed = <input type="checkbox" checked={isSubscribed} readOnly />;
const uncontrolled = <input type="checkbox" defaultChecked />;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreMissingProperties` | `false` | Allow `checked` without `onChange` or `readOnly`. |
| `ignoreExclusiveCheckedAttribute` | `false` | Allow `checked` together with `defaultChecked`. |

```jsx
<input type="checkbox" checked={isSubscribed} />;
```

```jsx
<input type="checkbox" checked={isSubscribed} defaultChecked onChange={toggle} />;
```
