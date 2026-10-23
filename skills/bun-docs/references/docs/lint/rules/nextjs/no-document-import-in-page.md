# @next/next/no-document-import-in-page
Source: https://bun.com/docs/lint/rules/nextjs/no-document-import-in-page

Disallow importing `next/document` outside `pages/_document.js`


`Html`, `Head`, `Main` and `NextScript` from `next/document` only work while the server renders `pages/_document.js`. If you use them in a page or a component, they fail when the page renders.

The rule reports every `import` of `next/document` in a file that isn't `pages/_document.*` or inside `pages/_document/`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-document-import-in-page" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import { Head } from "next/document";

export default function Home() {
  return (
    <Head>
      <meta name="theme-color" content="#111111" />
    </Head>
  );
}
```

Not reported:

```jsx
import Head from "next/head";

export default function Home() {
  return (
    <Head>
      <meta name="theme-color" content="#111111" />
    </Head>
  );
}
```

```jsx
import { Head, Html, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html>
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
```
