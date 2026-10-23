# react/forbid-component-props
Source: https://bun.com/docs/lint/rules/react/forbid-component-props

Disallow chosen props, by default `className` and `style`, on components


A component that accepts `className` or `style` lets every caller restyle it, and soon no two uses look the same. This rule reports those props on components, so callers change the look through props the component defines, such as `variant` or `size`.

The rule only checks components, which means elements with a capitalized name. It skips DOM elements such as `<div>`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/forbid-component-props" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/forbid-component-props" = ["error", {
  # forbid = <list of strings or objects>,
}]
```


## Examples

Reported:

```jsx
<Button className="wide" style={{ color: "red" }}>
  Delete
</Button>;
```

Not reported:

```jsx
<Button size="wide" variant="danger">
  Delete
</Button>;

<div className="toolbar" />;
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/forbid-component-props" = ["error", {
  forbid = ["style", { propName = "className", allowedFor = ["Icon"] }],
}]
```

`forbid` is the only option. It's a list of prop names or objects, and it replaces the default `["className", "style"]`:

| Key | What it does |
| --- | --- |
| `propName` | The name of the prop. |
| `propNamePattern` | Use this instead of `propName` to match names with a glob, such as `"data-*"`. |
| `allowedFor` | Components that can have the prop. It's forbidden on all others. |
| `allowedForPatterns` | The same, as globs that match the component's name. |
| `disallowedFor` | The prop is forbidden on these components only. |
| `disallowedForPatterns` | The same, as globs. |
| `message` | Replaces the report's text. |

An entry can have the `allowed..` keys or the `disallowed..` keys, but not both.

```jsx
<Icon className="spin" />;
```

```jsx
<Button className="wide" />;
```

```jsx
<IconButton style={{ margin: 4 }} />;
```

```jsx
<Card style={{ margin: 4 }} />;
```

```jsx
<Button data-testid="save" />;
```
