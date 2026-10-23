# react/no-unsafe
Source: https://bun.com/docs/lint/rules/react/no-unsafe

Disallow the `UNSAFE_` lifecycle methods of class components


`UNSAFE_componentWillMount`, `UNSAFE_componentWillReceiveProps`, and `UNSAFE_componentWillUpdate` run before React commits a render. React can start a render, drop it, and start again, so these methods can run several times for one update. If you start a request or a subscription there, it can start several times and may never be cleaned up.

| Instead of | Use |
| --- | --- |
| `UNSAFE_componentWillMount` | `componentDidMount` |
| `UNSAFE_componentWillReceiveProps` | `getDerivedStateFromProps` |
| `UNSAFE_componentWillUpdate` | `componentDidUpdate` |


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-unsafe" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-unsafe" = ["error", {
  checkAliases = false,
}]
```


## Examples

Reported:

```jsx
class Feed extends React.Component {
  UNSAFE_componentWillMount() {
    this.subscription = subscribe(this.props.channel);
  }
}
```

Not reported:

```jsx
class Feed extends React.Component {
  componentDidMount() {
    this.subscription = subscribe(this.props.channel);
  }
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `checkAliases` | `false` | Also report the old names without the prefix: `componentWillMount`, `componentWillReceiveProps`, and `componentWillUpdate`. |

```jsx
class Feed extends React.Component {
  componentWillMount() {
    this.subscription = subscribe(this.props.channel);
  }
}
```
