# oxc/bad-char-at-comparison
Source: https://bun.com/docs/lint/rules/oxc/bad-char-at-comparison

Disallow comparing a single character with a longer string


`text.charAt(0)` is at most one character. Comparing it with a string of two or more characters is always `false` with `===` and always `true` with `!==`, so the branch never does what it looks like it does.

Every `.charAt(index)` is checked. `.at(index)` and an index written as a number, such as `[0]`, are only checked when the value is clearly a string: a string literal, a `const` set to one, or a variable declared with the type `string`. A parameter of type `string` doesn't count.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/bad-char-at-comparison" = "error" # or "warn"
```


## Examples

Reported:

```js
if (path.charAt(0) === "./") {
  resolveRelative(path);
}

const prefix = "https://example.com";
if (prefix[0] === "ht") {
  useTls();
}
```

Not reported:

```js
if (path.startsWith("./")) {
  resolveRelative(path);
}

if (path.charAt(0) === "/") {
  resolveAbsolute(path);
}
```
