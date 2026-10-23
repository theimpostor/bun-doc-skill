# react/jsx-indent-props
Source: https://bun.com/docs/lint/rules/react/jsx-indent-props

Enforce consistent indentation of JSX props


When props are on their own lines, uneven indentation makes them hard to tell apart from the tag and its children. The rule checks each prop that starts a line. The default is 4 spaces more than the line where the tag starts.

`--fix` corrects the indentation.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-indent-props" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-indent-props" = ["error", {
  indentMode = 4, # "tab", "first" or number
  ignoreTernaryOperator = false,
}]
```


## Examples

Reported:

```jsx
const field = (
    <Input
      name="email"
            value={email}
    />
);
```

Not reported:

```jsx
const field = (
    <Input
        name="email"
        value={email}
    />
);
```

## Options

The option is a number of spaces, `"tab"`, `"first"`, or an object:

| Option | Default | What it does |
| --- | --- | --- |
| `indentMode` | `4` | A number of spaces, `"tab"` for one tab, or `"first"` to line up every prop with the first one. |
| `ignoreTernaryOperator` | `false` | By default, props of a tag on a line that starts with `?` or `:` get one more level. With `true` they don't. |

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-indent-props" = ["error", 2]
```

```jsx
const field = (
  <Input
    name="email"
    value={email}
  />
);
```

With `"first"`:

```jsx
const field = <Input name="email"
  value={email}
/>;
```

```jsx
const field = <Input name="email"
                     value={email}
/>;
```

With `2`, the props of a tag on a line that starts with `?` or `:` are indented by 4:

```jsx
const field = editable
  ? <Input
      name="email"
    />
  : null;
```

```jsx
const field = editable
  ? <Input
    name="email"
  />
  : null;
```

With `ignoreTernaryOperator`, they're indented by 2 like any other props:

```jsx
const field = editable
  ? <Input
    name="email"
  />
  : null;
```

## When not to use it

If `bun fmt` or another formatter lays out your code, it already decides the indentation.
