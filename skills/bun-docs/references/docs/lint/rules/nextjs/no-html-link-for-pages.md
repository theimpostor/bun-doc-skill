# @next/next/no-html-link-for-pages
Source: https://bun.com/docs/lint/rules/nextjs/no-html-link-for-pages

Disallow `<a>` elements that link to another page of the app


Clicking a plain `<a>` makes the browser load the whole next page. That means new HTML, new scripts, and all client state is gone. `Link` from `next/link` changes the page in the browser and fetches the next page's code ahead of time.

The rule reports an `<a>` with an `href` that's a plain string and points inside the site, such as `/about` or `about`. It doesn't look at which pages exist, so a link to an API route or to a file in `public/` is reported too.

These are allowed: an `href` with a scheme (`https:`, `mailto:`, `tel:`), one that starts with `//` or `#`, an element with `target="_blank"`, and an element with `download`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-html-link-for-pages" = "error" # or "warn"
```


## Examples

Reported:

```jsx
export default function Nav() {
  return <a href="/about">About</a>;
}
```

```jsx
export default function LogOut() {
  return <a href="/api/logout">Log out</a>;
}
```

Not reported:

```jsx
import Link from "next/link";

export default function Nav() {
  return <Link href="/about">About</Link>;
}
```

```jsx
export default function Footer() {
  return (
    <footer>
      <a href="https://example.com">Partner site</a>
      <a href="mailto:hello@example.com">Write to us</a>
      <a href="#top">Back to top</a>
      <a href="/terms" target="_blank">Terms</a>
      <a href="/price-list.pdf" download>Price list</a>
    </footer>
  );
}
```
