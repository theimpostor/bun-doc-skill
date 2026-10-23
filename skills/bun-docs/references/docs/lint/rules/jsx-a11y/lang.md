# jsx-a11y/lang
Source: https://bun.com/docs/lint/rules/jsx-a11y/lang

Require the `lang` attribute of `<html>` to be a valid language tag


A screen reader picks its voice and pronunciation from the page's `lang`. If the value isn't a language, such as a typo or a country name, it falls back to the user's default and might mispronounce the text.

The value must be a registered BCP 47 tag such as `en`, `en-US` or `zh-Hans`. An `<html>` without `lang` is reported too, so with `jsx-a11y/html-has-lang` on as well, a missing or empty `lang` gets two reports. A value that's only known at runtime, such as `lang={locale}`, isn't checked.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/lang" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const wrong = <html lang="english" />;
const empty = <html lang="" />;
const missing = <html />;
```

Not reported:

```jsx
const page = <html lang="en" />;
const brazilian = <html lang="pt-BR" />;
const dynamic = <html lang={locale} />;
```
