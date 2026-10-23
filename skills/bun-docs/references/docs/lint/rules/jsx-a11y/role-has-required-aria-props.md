# jsx-a11y/role-has-required-aria-props
Source: https://bun.com/docs/lint/rules/jsx-a11y/role-has-required-aria-props

Require the `aria-*` attributes that an element's `role` needs


Some roles only make sense together with a state. A screen reader announces `role="checkbox"` as "checked" or "not checked", and it reads that from `aria-checked`. Without the attribute, the user hears a checkbox but can't tell which state it's in.

| Role | Needs |
| --- | --- |
| `checkbox`, `radio`, `switch`, `menuitemcheckbox`, `menuitemradio` | `aria-checked` |
| `combobox` | `aria-controls`, `aria-expanded` |
| `heading` | `aria-level` |
| `meter`, `slider` | `aria-valuenow` |
| `option` | `aria-selected` |
| `scrollbar` | `aria-controls`, `aria-valuenow` |

Only a `role` written as a string is checked.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/role-has-required-aria-props" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const dark = <span role="switch" tabIndex={0} onClick={toggleTheme} />;
const title = <div role="heading">Settings</div>;
```

Not reported:

```jsx
const dark = (
  <span role="switch" aria-checked={isDark} tabIndex={0} onClick={toggleTheme} />
);

const title = <div role="heading" aria-level={2}>Settings</div>;
```

The rule only looks at the attributes written on the element. It doesn't know that a native checkbox already has a checked state, or what a spread adds:

```jsx
const dark = <input type="checkbox" role="switch" checked={isDark} />;
const wifi = <span role="switch" {...switchProps} />;
```
