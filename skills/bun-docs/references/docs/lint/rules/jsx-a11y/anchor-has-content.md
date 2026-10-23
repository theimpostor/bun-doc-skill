# jsx-a11y/anchor-has-content
Source: https://bun.com/docs/lint/rules/jsx-a11y/anchor-has-content

Require links to have content that a screen reader can read


A link with nothing in it, or with only hidden content, is announced as "link" and nothing else. The person hearing it can't tell where it goes.

Text, an expression, a visible element, a `title` or an `aria-label` all count as content. A link that's hidden itself with `aria-hidden` isn't checked.

If the only child is a hidden element, `--fix` removes its `aria-hidden` and `hidden` attributes.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/anchor-has-content" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/anchor-has-content" = ["error", {
  components = [], # list of strings
}]
```


## Examples

Reported:

```jsx
const profile = <a href="/profile" />;
const settings = <a href="/settings"><span aria-hidden>Settings</span></a>;
```

Not reported:

```jsx
const profile = <a href="/profile">{user.name}</a>;
const settings = <a href="/settings"><span>Settings</span></a>;
const close = <a href="/" aria-label="Close"><Icon name="x" aria-hidden /></a>;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `components` | `[]` | Components to check like `a`. |

```jsx
const profile = <Link to="/profile" />;
```
