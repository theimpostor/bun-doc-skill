# @next/next/google-font-preconnect
Source: https://bun.com/docs/lint/rules/nextjs/google-font-preconnect

Require `rel="preconnect"` on `<link>` elements that point to `fonts.gstatic.com`


Google Fonts serves its font files from `fonts.gstatic.com`. A `<link>` to that host is there to open the connection early, so the font download doesn't wait for DNS and TLS. Without `rel="preconnect"`, the browser doesn't do that.

The rule looks at `<link>` elements with an `href` that starts with `https://fonts.gstatic.com`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/google-font-preconnect" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const hint = <link href="https://fonts.gstatic.com" />;
```

```jsx
const hint = <link rel="preload" href="https://fonts.gstatic.com" />;
```

Not reported:

```jsx
const hint = <link rel="preconnect" href="https://fonts.gstatic.com" />;
```
