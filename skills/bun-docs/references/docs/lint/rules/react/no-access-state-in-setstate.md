# react/no-access-state-in-setstate
Source: https://bun.com/docs/lint/rules/react/no-access-state-in-setstate

Disallow reading `this.state` in the argument of `this.setState()`


React batches `setState` calls, so `this.state` may still hold the old value when you build the next one from it. Two `this.setState({ count: this.state.count + 1 })` calls in the same event add 1, not 2.

Pass a function instead. React calls it with the state after all earlier updates.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-access-state-in-setstate" = "error" # or "warn"
```


## Examples

Reported:

```jsx
class Counter extends React.Component {
  increment() {
    this.setState({ count: this.state.count + 1 });
  }
}
```

Reading the value into a variable first doesn't help:

```jsx
class Counter extends React.Component {
  increment() {
    const count = this.state.count;
    this.setState({ count: count + 1 });
  }
}
```

Not reported:

```jsx
class Counter extends React.Component {
  increment() {
    this.setState(previous => ({ count: previous.count + 1 }));
  }
}
```
