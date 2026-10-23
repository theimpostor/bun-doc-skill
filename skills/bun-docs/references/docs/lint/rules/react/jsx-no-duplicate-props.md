# react/jsx-no-duplicate-props
Source: https://bun.com/docs/lint/rules/react/jsx-no-duplicate-props

Disallow the same prop twice on one JSX element


When a prop is written twice, the last one wins and the first is silently dropped. That's nearly always a leftover from an edit or a merge.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-no-duplicate-props" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-no-duplicate-props" = ["error", {
  ignoreCase = false,
}]
```


## Examples

Reported:

```jsx
const field = <Input name="email" type="text" name="username" />;
```

Not reported:

```jsx
const field = <Input name="email" type="text" />;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreCase` | `false` | Treat names that differ only in case, such as `onClick` and `onclick`, as the same prop. |

```jsx
const button = <Button onClick={save} onclick={save} />;
```
