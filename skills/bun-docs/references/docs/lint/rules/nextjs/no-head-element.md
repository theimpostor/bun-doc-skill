# @next/next/no-head-element
Source: https://bun.com/docs/lint/rules/nextjs/no-head-element

Disallow the `<head>` element in favor of `Head` from `next/head`


In the Pages Router, Next.js writes the document's `<head>` itself. A `<head>` element in a page or a component is rendered inside the `<body>`, where it isn't valid HTML. The `Head` component from `next/head` moves its children into the real `<head>`.

Files under an `app/` directory aren't checked. In the App Router, the root layout can have a `<head>`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-head-element" = "error" # or "warn"
```


## Examples

Reported:

```jsx
export default function About() {
  return (
    <div>
      <head>
        <title>About us</title>
      </head>
      <h1>About us</h1>
    </div>
  );
}
```

Not reported:

```jsx
import Head from "next/head";

export default function About() {
  return (
    <div>
      <Head>
        <title>About us</title>
      </Head>
      <h1>About us</h1>
    </div>
  );
}
```

```jsx
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body>{children}</body>
    </html>
  );
}
```
