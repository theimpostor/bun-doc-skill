# react/require-render-return
Source: https://bun.com/docs/lint/rules/react/require-render-return

Require the `render` method of a class component to return something


A `render` method without `return` gives React `undefined`. React 18 and later show nothing for it, and older versions throw. The usual cause is JSX written as a statement with the `return` forgotten.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/require-render-return" = "error" # or "warn"
```


## Examples

Reported:

```jsx
class Greeting extends React.Component {
  render() {
    <h1>Hello {this.props.name}</h1>;
  }
}
```

Not reported:

```jsx
class Greeting extends React.Component {
  render() {
    return <h1>Hello {this.props.name}</h1>;
  }
}

class Footer extends React.Component {
  render = () => <footer>{this.props.text}</footer>;
}
```
