# no-octal
Source: https://bun.com/docs/lint/rules/eslint/no-octal

Disallow number literals that start with `0` followed by a digit


A number that starts with `0` followed by more digits is read in base 8, so `071` is 57. If one of the digits is an `8` or a `9`, it's read in base 10 after all, so `081` is 81. Write `0o71` if you mean octal, and drop the zero if you don't.

These numbers are a syntax error in modules and in strict mode. `.js` files are linted as modules, so the rule only has something to report in `.cjs` files, or where your config sets `sourceType` to `"commonjs"` or `"script"`.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-octal" = "off" # or "error"
```


## Examples

Reported:

**File:** `permissions.cjs`
```js
const mode = 0755;
const month = 09;
```

Not reported:

**File:** `permissions.cjs`
```js
const mode = 0o755;
const month = 9;
const ratio = 0.5;
```
