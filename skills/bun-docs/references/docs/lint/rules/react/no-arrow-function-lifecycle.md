# react/no-arrow-function-lifecycle
Source: https://bun.com/docs/lint/rules/react/no-arrow-function-lifecycle

Disallow arrow functions in class fields as React lifecycle methods


An arrow function in a class field is created again for every instance, and it isn't on the prototype. A subclass can't call it with `super.componentDidMount()`, and a test can't replace it on `Component.prototype`. React always calls lifecycle methods on the instance, so binding `this` with an arrow function gains nothing.

The rule covers `render`, every `component*` and `UNSAFE_component*` method, `shouldComponentUpdate`, `getSnapshotBeforeUpdate`, `getChildContext`, `getDefaultProps`, `getInitialState` and the static `getDerivedStateFromProps`, in classes and in `createReactClass`.

`--fix` rewrites the arrow function as a method.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-arrow-function-lifecycle" = "error" # or "warn"
```


## Examples

Reported:

```jsx
class Clock extends React.Component {
  componentDidMount = () => {
    this.timer = setInterval(this.tick, 1000);
  };

  render = () => <time>{this.state.now}</time>;
}
```

Not reported:

```jsx
class Clock extends React.Component {
  componentDidMount() {
    this.timer = setInterval(this.tick, 1000);
  }

  // Not a lifecycle method: an arrow function keeps `this` when it is passed around.
  tick = () => {
    this.setState({ now: Date.now() });
  };

  render() {
    return <time>{this.state.now}</time>;
  }
}
```
