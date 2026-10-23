# @next/next/no-sync-scripts
Source: https://bun.com/docs/lint/rules/nextjs/no-sync-scripts

Disallow `<script src>` without `async` or `defer`


When the browser hits a `<script>` with a `src`, it stops reading the HTML until it has downloaded and run the file. Nothing below the tag shows up in the meantime, so a slow third-party server holds up your whole page.

With `async` or `defer`, the browser keeps reading the HTML while the file downloads. `Script` from `next/script` doesn't block either, and it lets you pick when the script loads.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-sync-scripts" = "error" # or "warn"
```


## Examples

Reported:

```jsx
export default function Checkout() {
  return <script src="https://example.com/payments.js" />;
}
```

Not reported:

```jsx
export default function Checkout() {
  return <script src="https://example.com/payments.js" defer />;
}
```

```jsx
import Script from "next/script";

export default function Checkout() {
  return <Script src="https://example.com/payments.js" />;
}
```
