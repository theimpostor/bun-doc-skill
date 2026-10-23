# react/state-in-constructor
Source: https://bun.com/docs/lint/rules/react/state-in-constructor

Enforce where a class component sets its initial state: in the constructor or in a class field


A class component can set its initial state in two places: with `this.state = ...` in the constructor, or with a `state = ...` class field. Both work. In a codebase that mixes them, you have to look in two places to find a component's initial state.

By default the rule asks for the constructor.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/state-in-constructor" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/state-in-constructor" = ["error", "always"] # "always" or "never"
```


## Examples

Reported:

```jsx
class Counter extends React.Component {
  state = { count: 0 };

  render() {
    return <span>{this.state.count}</span>;
  }
}
```

Not reported:

```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  render() {
    return <span>{this.state.count}</span>;
  }
}
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/state-in-constructor" = ["error", "never"]
```

| Option | What it does |
| --- | --- |
| `"always"` (default) | Report a `state` class field. Set the state in the constructor. |
| `"never"` | Report `this.state = ...` in the constructor. Set the state in a class field. |

With `"never"`, this is reported:

```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }
}
```

And this isn't:

```jsx
class Counter extends React.Component {
  state = { count: 0 };
}
```
