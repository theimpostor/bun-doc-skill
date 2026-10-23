# jsx-a11y/aria-activedescendant-has-tabindex
Source: https://bun.com/docs/lint/rules/jsx-a11y/aria-activedescendant-has-tabindex

Require elements with `aria-activedescendant` to be focusable


`aria-activedescendant` tells a screen reader which child of a widget is active while focus stays on the widget itself. That only works if the widget can take focus. A plain `div` can't, so the attribute does nothing there until you add a `tabIndex` of `0` or `-1`.

Elements that are focusable by default, such as `input`, `select` and `button`, don't need a `tabIndex`. Components aren't checked.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/aria-activedescendant-has-tabindex" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const list = (
  <div role="listbox" aria-activedescendant={activeId}>
    {options}
  </div>
);
```

Not reported:

```jsx
const list = (
  <div role="listbox" tabIndex={0} aria-activedescendant={activeId}>
    {options}
  </div>
);

const grid = <div role="grid" tabIndex={-1} aria-activedescendant={activeId} />;
const search = <input role="combobox" aria-activedescendant={activeId} />;
```
