# jsx-a11y/aria-unsupported-elements
Source: https://bun.com/docs/lint/rules/jsx-a11y/aria-unsupported-elements

Disallow `role` and `aria-*` attributes on elements that do not support them


Elements such as `meta`, `script` and `style` aren't part of what the page shows, so a screen reader never gets to them. A `role` or an `aria-*` attribute on them does nothing.

The elements are `base`, `col`, `colgroup`, `head`, `html`, `link`, `meta`, `noembed`, `noscript`, `param`, `picture`, `script`, `source`, `style`, `title` and `track`.

`--fix` removes the attribute.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/aria-unsupported-elements" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const head = (
  <head>
    <meta charSet="utf-8" aria-hidden="true" />
    <title role="heading">Dashboard</title>
  </head>
);
```

Not reported:

```jsx
const head = (
  <head>
    <meta charSet="utf-8" />
    <title>Dashboard</title>
  </head>
);
```
