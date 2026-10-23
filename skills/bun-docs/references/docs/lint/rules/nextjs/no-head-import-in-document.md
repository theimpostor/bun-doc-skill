# @next/next/no-head-import-in-document
Source: https://bun.com/docs/lint/rules/nextjs/no-head-import-in-document

Disallow importing `next/head` in `pages/_document.js`


There are two `Head` components. The one from `next/head` is for pages. It updates the `<head>` as the user moves from page to page. `pages/_document.js` is only rendered on the server and needs the `Head` from `next/document`.

The rule reports every `import` of `next/head` in a file named `_document.*`, or named `index.*` in a `_document` directory.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-head-import-in-document" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import { Html, Main, NextScript } from "next/document";
import Head from "next/head";

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

Not reported:

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
