# @next/next/google-font-display
Source: https://bun.com/docs/lint/rules/nextjs/google-font-display

Require a `display` parameter other than `auto`, `block` or `fallback` on Google Fonts URLs


The `display` parameter in a Google Fonts URL decides what the browser shows while the font downloads. Without it, or with `auto` or `block`, the text can stay invisible until the font arrives. With `fallback`, the browser only waits a few seconds for the font and then keeps the fallback font for that page view.

The rule checks `<link>` elements with an `href` that starts with `https://fonts.googleapis.com/css`. It reports a missing `display` and the values `auto`, `block` and `fallback`. Any other value is accepted, such as `optional` or `swap`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/google-font-display" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const font = <link href="https://fonts.googleapis.com/css2?family=Inter" rel="stylesheet" />;
```

```jsx
const font = <link href="https://fonts.googleapis.com/css2?family=Inter&display=block" rel="stylesheet" />;
```

Not reported:

```jsx
const font = <link href="https://fonts.googleapis.com/css2?family=Inter&display=optional" rel="stylesheet" />;
```

An `href` in braces isn't checked:

```jsx
const font = <link href={fontUrl} rel="stylesheet" />;
```
