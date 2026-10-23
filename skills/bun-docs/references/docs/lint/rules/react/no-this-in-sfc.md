# react/no-this-in-sfc
Source: https://bun.com/docs/lint/rules/react/no-this-in-sfc

Disallow `this` in function components


A function component gets its props as an argument. React calls it without a `this`, so `this.props` throws a `TypeError`. This often happens when a class component is rewritten as a function and one `this.` is left behind.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-this-in-sfc" = "error" # or "warn"
```


## Examples

Reported:

```jsx
function Greeting(props) {
  return <h1>Hello, {this.props.name}</h1>;
}
```

Not reported:

```jsx
function Greeting(props) {
  return <h1>Hello, {props.name}</h1>;
}

class Welcome extends React.Component {
  render() {
    return <h1>Welcome, {this.props.name}</h1>;
  }
}
```
