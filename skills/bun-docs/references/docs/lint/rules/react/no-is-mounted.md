# react/no-is-mounted
Source: https://bun.com/docs/lint/rules/react/no-is-mounted

Disallow `this.isMounted()`


`isMounted()` only exists on components made with `createReactClass`. In a class that extends `React.Component`, `this.isMounted` is `undefined` and the call throws.

It's mostly used to skip a `setState` after the component is gone. That hides the real problem: a request, timer or subscription that's still running and still holds on to the component. Cancel it in `componentWillUnmount`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-is-mounted" = "error" # or "warn"
```


## Examples

Reported:

```jsx
class Profile extends React.Component {
  componentDidMount() {
    loadUser(this.props.id).then(user => {
      if (this.isMounted()) {
        this.setState({ user });
      }
    });
  }
}
```

Not reported:

```jsx
class Profile extends React.Component {
  controller = new AbortController();

  componentDidMount() {
    loadUser(this.props.id, { signal: this.controller.signal }).then(user => {
      this.setState({ user });
    });
  }

  componentWillUnmount() {
    this.controller.abort();
  }
}
```
