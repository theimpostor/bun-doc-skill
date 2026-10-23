# react/prefer-exact-props
Source: https://bun.com/docs/lint/rules/react/prefer-exact-props

Require `propTypes` to be wrapped in a function that rejects unknown props


`propTypes` check the props they name and say nothing about the rest. A misspelled prop such as `onclick` is passed, ignored, and never noticed. A wrapper such as `exact()` from the `prop-types-exact` package adds a warning for every prop that isn't declared.

The rule does nothing until you name your wrapper. List it under `propWrapperFunctions` in your settings, with `exact` set to `true`:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/prefer-exact-props" = "error"

[lint.settings]
propWrapperFunctions = [{ property = "exact", exact = true }]
```

In an ESLint config, the same list goes under `settings`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/prefer-exact-props" = "error" # or "warn"
```


## Examples

Reported, with `exact` listed as a wrapper:

```jsx
function Button({ label }) {
  return <button>{label}</button>;
}

Button.propTypes = {
  label: PropTypes.string,
};
```

```jsx
class Button extends React.Component {
  static propTypes = {
    label: PropTypes.string,
  };
  render() {
    return <button>{this.props.label}</button>;
  }
}
```

Not reported:

```jsx
function Button({ label }) {
  return <button>{label}</button>;
}

Button.propTypes = exact({
  label: PropTypes.string,
});
```
