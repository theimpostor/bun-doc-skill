# no-div-regex
Source: https://bun.com/docs/lint/rules/eslint/no-div-regex

Disallow regular expressions that start with `=`


A regular expression literal that starts with `=` begins with `/=`, which is also the division assignment operator. You have to look twice to see which one it is.

`--fix` rewrites the `=` to `[=]`, which matches the same text.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-div-regex" = "error" # or "warn"
```


## Examples

Reported:

```js
const value = line.replace(/=\s*/, "");
```

Not reported:

```js
const value = line.replace(/[=]\s*/, "");
```
