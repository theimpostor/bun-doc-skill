# jsx-a11y/html-has-lang
Source: https://bun.com/docs/lint/rules/jsx-a11y/html-has-lang

Require a `lang` attribute on the `html` element


A screen reader picks its voice and pronunciation from the page's `lang`. Without one, it falls back to the person's system language, so a French page is read aloud with English pronunciation.

An empty string, `null`, `undefined`, a number, `true` and `false` don't count as a language.

`jsx-a11y/lang` reports a missing or empty `lang` too, and also checks that the value is a real language tag. With both rules on, you get two reports.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/html-has-lang" = "error" # or "warn"
```


## Examples

Reported:

```jsx
function Layout({ children }) {
  return <html><body>{children}</body></html>;
}

function EmptyLang({ children }) {
  return <html lang=""><body>{children}</body></html>;
}
```

Not reported:

```jsx
function Layout({ children }) {
  return <html lang="en"><body>{children}</body></html>;
}

function Localized({ children, locale }) {
  return <html lang={locale}><body>{children}</body></html>;
}
```
