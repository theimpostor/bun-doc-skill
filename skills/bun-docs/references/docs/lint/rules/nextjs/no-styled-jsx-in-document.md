# @next/next/no-styled-jsx-in-document
Source: https://bun.com/docs/lint/rules/nextjs/no-styled-jsx-in-document

Disallow `<style jsx>` in `pages/_document.js`


Next.js doesn't support `styled-jsx` in `pages/_document.js`. Put the styles in `pages/_app.js`, in a component, or in a CSS file.

The rule checks files named `_document.*`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-styled-jsx-in-document" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import { Head, Html, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html>
      <Head />
      <body>
        <Main />
        <NextScript />
        <style jsx>{`
          body {
            margin: 0;
          }
        `}</style>
      </body>
    </Html>
  );
}
```

Not reported, in `pages/_app.jsx`:

```jsx
export default function App({ Component, pageProps }) {
  return (
    <>
      <Component {...pageProps} />
      <style jsx global>{`
        body {
          margin: 0;
        }
      `}</style>
    </>
  );
}
```
