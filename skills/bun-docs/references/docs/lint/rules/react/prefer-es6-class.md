# react/prefer-es6-class
Source: https://bun.com/docs/lint/rules/react/prefer-es6-class

Enforce one way to write class components: `class` or `createReactClass`


You can write a class component with `class` or with `createReactClass()`. The two differ in how methods are bound and how the initial state and the default props are set, so a codebase that mixes them is harder to read. By default, the rule requires `class`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/prefer-es6-class" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/prefer-es6-class" = ["error", "always"] # "always" or "never"
```


## Examples

Reported:

```jsx
const Greeting = createReactClass({
  render() {
    return <h1>Hello {this.props.name}</h1>;
  },
});
```

Not reported:

```jsx
class Greeting extends React.Component {
  render() {
    return <h1>Hello {this.props.name}</h1>;
  }
}
```

## Options

| Option | What it does |
| --- | --- |
| `"always"` (default) | Report components made with `createReactClass()`. |
| `"never"` | Report components written as a `class` declaration. |

Reported with `"never"`:

```jsx
class Greeting extends React.Component {
  render() {
    return <h1>Hello {this.props.name}</h1>;
  }
}
```
