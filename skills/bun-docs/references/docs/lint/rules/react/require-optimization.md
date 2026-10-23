# react/require-optimization
Source: https://bun.com/docs/lint/rules/react/require-optimization

Require class components to define `shouldComponentUpdate` or extend `PureComponent`


A class component renders again each time its parent renders, even if its props and state are the same. `shouldComponentUpdate` lets it skip those renders. `React.PureComponent` does the comparison for you.

The rule doesn't check function components. A `createReactClass` component also passes if `PureRenderMixin` is in its `mixins`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/require-optimization" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/require-optimization" = ["error", {
  allowDecorators = [], # list of strings
}]
```


## Examples

Reported:

```jsx
class Row extends React.Component {
  render() {
    return <li>{this.props.label}</li>;
  }
}
```

Not reported:

```jsx
class Row extends React.PureComponent {
  render() {
    return <li>{this.props.label}</li>;
  }
}

class Cell extends React.Component {
  shouldComponentUpdate(nextProps) {
    return nextProps.value !== this.props.value;
  }
  render() {
    return <td>{this.props.value}</td>;
  }
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowDecorators` | `[]` | Names of decorators that add `shouldComponentUpdate`. A class with one of them isn't reported. |

Not reported with `allowDecorators: ["pureRender"]`:

```tsx
@pureRender
class Row extends React.Component {
  render() {
    return <li>{this.props.label}</li>;
  }
}
```

## When not to use it

Comparing props has a cost too. For a component that nearly always gets new props, the check is wasted work on top of the render.
