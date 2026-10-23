# oxc/bad-replace-all-arg
Source: https://bun.com/docs/lint/rules/oxc/bad-replace-all-arg

Require the `g` flag on a regular expression passed to `replaceAll()`


`replaceAll()` throws a `TypeError` when its regular expression doesn't have the `g` flag. The code parses and only fails when that line runs.

The rule checks a regular expression literal, `new RegExp()` and `RegExp()`, written in the call or kept in a variable. If the flags aren't a plain string, it can't tell and reports nothing. A string argument is fine, because `replaceAll()` replaces every occurrence of it.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/bad-replace-all-arg" = "error" # or "warn"
```


## Examples

Reported:

```js
const slug = title.replaceAll(/\s+/, "-");

const digits = new RegExp("\\d");
const masked = cardNumber.replaceAll(digits, "*");
```

Not reported:

```js
const slug = title.replaceAll(/\s+/g, "-");

const digits = new RegExp("\\d", "g");
const masked = cardNumber.replaceAll(digits, "*");

const unixPath = path.replaceAll("\\", "/");
```
