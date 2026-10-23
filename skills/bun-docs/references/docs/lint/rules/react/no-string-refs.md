# react/no-string-refs
Source: https://bun.com/docs/lint/rules/react/no-string-refs

Disallow strings as the value of the `ref` attribute


`ref="input"` asks React to store the element in `this.refs.input`. String refs only work in class components, and React 19 removed them. Use `createRef`, `useRef`, or a callback.

If `settings.react.version` (`[lint.settings.react]` in `bunfig.toml`, or `settings` in an ESLint config) is lower than 18.3, the rule also reports reading `this.refs` in a class component.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-string-refs" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-string-refs" = ["error", {
  noTemplateLiterals = false,
}]
```


## Examples

Reported:

```jsx
class SearchBox extends React.Component {
  componentDidMount() {
    this.refs.input.focus();
  }

  render() {
    return <input ref="input" />;
  }
}
```

Not reported:

```jsx
class SearchBox extends React.Component {
  input = React.createRef();

  componentDidMount() {
    this.input.current.focus();
  }

  render() {
    return <input ref={this.input} />;
  }
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `noTemplateLiterals` | `false` | Also report a template literal as the value of `ref`. |

```jsx
const row = index => <li ref={`row${index}`} />;
```
