# @next/next/no-page-custom-font
Source: https://bun.com/docs/lint/rules/nextjs/no-page-custom-font

Disallow Google Fonts `<link>` elements outside `pages/_document.js`


A font `<link>` in one page only loads for that page. Other pages that use the font show a fallback instead. In `pages/_document.js`, the same `<link>` is part of every page.

The rule looks at `<link>` elements with an `href` that starts with `https://fonts.googleapis.com/css`. It reports them in every file that isn't named `_document.*`. In `_document.*`, it reports them if they aren't inside the default export.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-page-custom-font" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import Head from "next/head";

export default function Home() {
  return (
    <Head>
      <link href="https://fonts.googleapis.com/css2?family=Inter&display=optional" rel="stylesheet" />
    </Head>
  );
}
```

Here the file is `pages/_document.jsx`, but the element is in a helper, not in the exported document:

```jsx
import { Head, Html, Main, NextScript } from "next/document";

function Fonts() {
  return <link href="https://fonts.googleapis.com/css2?family=Inter&display=optional" rel="stylesheet" />;
}

export default function Document() {
  return (
    <Html>
      <Head>
        <Fonts />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
```

Not reported:

```jsx
import { Head, Html, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html>
      <Head>
        <link href="https://fonts.googleapis.com/css2?family=Inter&display=optional" rel="stylesheet" />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
```

## When not to use it

The App Router has no `_document.js`, so a font `<link>` in `app/layout.js` is reported too. Load the font with `next/font`, or turn the rule off.

```jsx
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Inter&display=optional" rel="stylesheet" />
      </head>
      <body>{children}</body>
    </html>
  );
}
```
