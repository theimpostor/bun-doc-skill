# @next/next/no-duplicate-head
Source: https://bun.com/docs/lint/rules/nextjs/no-duplicate-head

Disallow more than one `<Head>` element in a file


Each `<Head>` from `next/document` renders a whole `<head>`, with the styles and scripts Next.js adds for the page. A second one repeats all of that. Put your tags in one `<Head>`.

The rule reports any file with two or more `<Head>` elements, if `Head` is an imported name.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-duplicate-head" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import { Head, Html, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html>
      <Head>
        <meta name="theme-color" content="#111111" />
      </Head>
      <Head>
        <link rel="icon" href="/favicon.ico" />
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
        <meta name="theme-color" content="#111111" />
        <link rel="icon" href="/favicon.ico" />
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

The rule doesn't check where `Head` comes from. Next.js merges several `<Head>` elements from `next/head`, but two of them in one file are still reported:

```jsx
import Head from "next/head";

export default function Post({ post }) {
  return (
    <article>
      <Head>
        <title>{post.title}</title>
      </Head>
      {post.draft && (
        <Head>
          <meta name="robots" content="noindex" />
        </Head>
      )}
    </article>
  );
}
```
