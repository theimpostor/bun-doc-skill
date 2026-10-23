# jsx-a11y/mouse-events-have-key-events
Source: https://bun.com/docs/lint/rules/jsx-a11y/mouse-events-have-key-events

Require `onFocus` with `onMouseOver` and `onBlur` with `onMouseOut`


Keyboard users never hover, so a tooltip or a preview that only shows on hover doesn't exist for them. Focus is the keyboard's version of hover, so pair `onMouseOver` with `onFocus`, and `onMouseOut` with `onBlur`.

The rule only checks HTML elements, not components.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/mouse-events-have-key-events" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/mouse-events-have-key-events" = ["error", {
  hoverInHandlers = ["onMouseOver"],
  hoverOutHandlers = ["onMouseOut"],
}]
```


## Examples

Reported:

```jsx
const help = (
  <button onMouseOver={showTooltip} onMouseOut={hideTooltip}>
    Help
  </button>
);
```

Not reported:

```jsx
const help = (
  <button
    onMouseOver={showTooltip}
    onFocus={showTooltip}
    onMouseOut={hideTooltip}
    onBlur={hideTooltip}
  >
    Help
  </button>
);
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `hoverInHandlers` | `["onMouseOver"]` | Handlers that need an `onFocus` next to them. |
| `hoverOutHandlers` | `["onMouseOut"]` | Handlers that need an `onBlur` next to them. |

Your list replaces the default. `onMouseEnter` isn't checked unless you add it:

```jsx
const card = <div onMouseEnter={showPreview} />;
```

```jsx
const card = <div onMouseEnter={showPreview} />;
```
