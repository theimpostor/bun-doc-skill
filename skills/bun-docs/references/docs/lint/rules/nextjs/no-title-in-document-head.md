# @next/next/no-title-in-document-head
Source: https://bun.com/docs/lint/rules/nextjs/no-title-in-document-head

Disallow `<title>` in the `Head` of `next/document`


Every page shares `pages/_document.js`, so a `<title>` in it gives every page the same title, and it can clash with the title a page sets for itself. Set the title in each page, with `Head` from `next/head`.

The rule reports a `<title>` that's a direct child of the `Head` you import from `next/document`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-title-in-document-head" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import { Head, Html, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html>
      <Head>
        <title>My shop</title>
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
```

Not reported, in a page:

```jsx
import Head from "next/head";

export default function Home() {
  return (
    <Head>
      <title>My shop</title>
    </Head>
  );
}
```

The rule only follows the first name in the import's braces. If `Head` isn't first, nothing is reported:

```jsx
import { Html, Head } from "next/document";

export default function Document() {
  return (
    <Html>
      <Head>
        <title>My shop</title>
      </Head>
    </Html>
  );
}
```
