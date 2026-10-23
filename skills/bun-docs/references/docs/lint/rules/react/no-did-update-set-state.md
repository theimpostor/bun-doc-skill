# react/no-did-update-set-state
Source: https://bun.com/docs/lint/rules/react/no-did-update-set-state

Disallow `this.setState()` in `componentDidUpdate`


`componentDidUpdate` runs after every update, and `setState` causes an update. A call that isn't behind a condition loops forever. One that's behind a condition still renders the component twice for each change.

A `setState` in a callback inside `componentDidUpdate` is allowed by default, because it runs later, when a request finishes or an event fires.

The rule reports nothing if `settings.react.version` (`[lint.settings.react]` in `bunfig.toml`, or `settings` in an ESLint config) is 16.3 or later, or if it's `"detect"` and the installed version is 16.3 or later.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-did-update-set-state" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-did-update-set-state" = [
  "error",
  # "disallow-in-func",
]
```


## Examples

Reported:

```jsx
class Cart extends React.Component {
  componentDidUpdate(previous) {
    if (previous.items !== this.props.items) {
      this.setState({ total: sum(this.props.items) });
    }
  }
}
```

Not reported:

```jsx
class Cart extends React.Component {
  componentDidUpdate(previous) {
    if (previous.coupon !== this.props.coupon) {
      checkCoupon(this.props.coupon).then(discount => {
        this.setState({ discount });
      });
    }
  }

  render() {
    return <Total value={sum(this.props.items)} />;
  }
}
```

## Options

| Option | What it does |
| --- | --- |
| `"disallow-in-func"` | Also report `setState` in a function inside `componentDidUpdate`. |

```jsx
class Cart extends React.Component {
  componentDidUpdate() {
    checkCoupon(this.props.coupon).then(discount => {
      this.setState({ discount });
    });
  }
}
```
