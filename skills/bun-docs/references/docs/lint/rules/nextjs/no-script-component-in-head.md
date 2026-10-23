# @next/next/no-script-component-in-head
Source: https://bun.com/docs/lint/rules/nextjs/no-script-component-in-head

Disallow `<Script>` as a child of `Head` from `next/head`


`Head` from `next/head` is for plain tags such as `<title>`, `<meta>` and `<link>`. The `Script` component from `next/script` doesn't work inside it. `Script` decides where its tag goes, so put it anywhere else in the page.

The rule reports a `<Script>` that's a direct child of the default import of `next/head`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-script-component-in-head" = "error" # or "warn"
```


## Examples

Reported:

```jsx
import Head from "next/head";
import Script from "next/script";

export default function Home() {
  return (
    <Head>
      <title>Home</title>
      <Script src="https://example.com/widget.js" />
    </Head>
  );
}
```

Not reported:

```jsx
import Head from "next/head";
import Script from "next/script";

export default function Home() {
  return (
    <>
      <Head>
        <title>Home</title>
      </Head>
      <Script src="https://example.com/widget.js" />
    </>
  );
}
```
