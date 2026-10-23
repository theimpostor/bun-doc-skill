# react/jsx-pascal-case
Source: https://bun.com/docs/lint/rules/react/jsx-pascal-case

Require component names in JSX to be in PascalCase


Components named `UserCard`, `User_Card` and `USERCARD` in one codebase are hard to search for and easy to mix up with constants. This rule wants one style: a capital first letter, no underscores, and at least one lowercase letter or digit.

Tags that start with a lowercase letter are HTML elements, so the rule skips them. One-character names, such as `<T />`, are allowed. In `<Menu.Item />`, the rule checks each part.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-pascal-case" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-pascal-case" = ["error", {
  allowAllCaps = false,
  allowLeadingUnderscore = false,
  allowNamespace = false,
  ignore = [],
}]
```


## Examples

Reported:

```jsx
const page = (
  <User_Card>
    <NAVBAR />
  </User_Card>
);
```

Not reported:

```jsx
const page = (
  <UserCard>
    <Navbar />
    <H1 />
  </UserCard>
);
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowAllCaps` | `false` | Also allow names in capitals, with underscores between words: `<NAV_BAR />`. |
| `allowLeadingUnderscore` | `false` | Allow one underscore before the name: `<_Button />`. |
| `allowNamespace` | `false` | In `<Form.input />`, only check `Form`. |
| `ignore` | `[]` | Names to skip. Globs such as `"*_DEPRECATED"` work. |

```jsx
const nav = <NAV_BAR />;
```

```jsx
const button = <_Button />;
```

```jsx
const button = <_Button />;
```

```jsx
const field = <Form.input />;
```

```jsx
const field = <Form.input />;
```

```jsx
const dialog = <Modal_DEPRECATED />;
```
