# @next/next/next-script-for-ga
Source: https://bun.com/docs/lint/rules/nextjs/next-script-for-ga

Require `next/script` instead of `<script>` to load Google Analytics


A plain `<script>` for Google Analytics or Google Tag Manager competes with your own code while the page loads. The `Script` component from `next/script` loads it after the page is interactive.

The rule reports a `<script>` if:

- its `src` contains `www.google-analytics.com/analytics.js` or `www.googletagmanager.com/gtag/js`
- the template literal in its `dangerouslySetInnerHTML` contains `www.google-analytics.com/analytics.js` or `www.googletagmanager.com/gtm.js`


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/next-script-for-ga" = "error" # or "warn"
```


## Examples

Reported:

```jsx
export default function Analytics() {
  return <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX" />;
}
```

```jsx
export default function Analytics() {
  return (
    <script
      dangerouslySetInnerHTML={{
        __html: `
          const tag = document.createElement("script");
          tag.src = "https://www.googletagmanager.com/gtm.js?id=GTM-XXXXXXX";
          document.head.append(tag);
        `,
      }}
    />
  );
}
```

Not reported:

```jsx
import Script from "next/script";

export default function Analytics() {
  return <Script src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX" />;
}
```
