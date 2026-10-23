# bun/jsx-no-forbidden-nesting
Source: https://bun.com/docs/lint/rules/bun/jsx-no-forbidden-nesting

Disallow a JSX element inside another element that cannot contain it


HTML doesn't allow a link or a button inside another link or button. Browsers disagree about what a click on the inner element does. In server-rendered HTML, the parser ends an `a` or a `button` where the next one starts and ignores a `form` inside a `form`, so the DOM doesn't match your JSX.

The inner element is reported at any depth, not only as a direct child. By default the rule knows these pairs:

| Outer | Cannot contain |
| --- | --- |
| `a` | `a`, `button` |
| `button` | `a`, `button` |
| `form` | `form` |
| `label` | `label` |

Only the tag names are compared, so a `Link` component that renders an `a` doesn't count as an `a`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/jsx-no-forbidden-nesting" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/jsx-no-forbidden-nesting" = ["error", {
  # pairs = <list of objects>,
}]
```


## Examples

Reported:

```jsx
const card = (
  <a href={post.url}>
    <h2>{post.title}</h2>
    <button onClick={save}>Save</button>
  </a>
);
```

Not reported:

```jsx
const card = (
  <article>
    <a href={post.url}>
      <h2>{post.title}</h2>
    </a>
    <button onClick={save}>Save</button>
  </article>
);
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `pairs` | The table above | A list of `{ outer, inner }` names. It replaces the default list. |

Use it for your own components:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/jsx-no-forbidden-nesting" = ["error", {
  pairs = [{ outer = "Link", inner = "Button" }],
}]
```

```jsx
const row = (
  <Link to="/settings">
    <Button>Settings</Button>
  </Link>
);
```

Then the default pairs no longer apply. Add them to the list if you want to keep them:

```jsx
const row = (
  <a href="/settings">
    <button>Settings</button>
  </a>
);
```
