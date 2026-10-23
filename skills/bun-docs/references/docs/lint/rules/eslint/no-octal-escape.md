# no-octal-escape
Source: https://bun.com/docs/lint/rules/eslint/no-octal-escape

Disallow octal escape sequences such as `\251` in strings


In a string, a backslash followed by digits from `0` to `7` is a character code in base 8. For example, `"\251"` is the copyright sign. Few readers know this form, and a digit typed right after it can change which character you get. Use `\xA9` or `\u{A9}` instead.

`\0` on its own (the null character) isn't reported.

Octal escapes are a syntax error in modules and in strict mode. `.js` files are linted as modules, so the rule only has something to report in `.cjs` files, or where your config sets `sourceType` to `"commonjs"` or `"script"`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-octal-escape" = "error" # or "warn"
```


## Examples

Reported:

**File:** `notice.cjs`
```js
const notice = "Copyright \251 2026";
```

Not reported:

**File:** `notice.cjs`
```js
const notice = "Copyright \xA9 2026";
const long = "Copyright \u{A9} 2026";
const terminator = "\0";
```
