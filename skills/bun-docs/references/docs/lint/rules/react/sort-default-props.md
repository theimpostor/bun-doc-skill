# react/sort-default-props
Source: https://bun.com/docs/lint/rules/react/sort-default-props

Require the keys of `defaultProps` to be sorted alphabetically


In a long `defaultProps` object, a fixed order makes props quick to find and duplicates easy to spot.

Capital letters sort before lowercase ones. After a spread, sorting starts over.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/sort-default-props" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/sort-default-props" = ["error", {
  ignoreCase = false,
}]
```


## Examples

Reported:

```jsx
function Button({ label, size }) {
  return <button className={size}>{label}</button>;
}

Button.defaultProps = {
  size: "medium",
  label: "OK",
};
```

Not reported:

```jsx
function Button({ label, size }) {
  return <button className={size}>{label}</button>;
}

Button.defaultProps = {
  label: "OK",
  size: "medium",
};
```

`label` comes after a spread here, so it isn't compared with `size`:

```jsx
class Button extends React.Component {
  static defaultProps = {
    size: "medium",
    ...shared,
    label: "OK",
  };
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreCase` | `false` | Ignore case when comparing the keys. |

By default this is reported, because `I` sorts before `a`:

```jsx
Button.defaultProps = {
  ariaLabel: "",
  Icon: null,
};
```

With `ignoreCase: true` it isn't:

```jsx
Button.defaultProps = {
  ariaLabel: "",
  Icon: null,
};
```
