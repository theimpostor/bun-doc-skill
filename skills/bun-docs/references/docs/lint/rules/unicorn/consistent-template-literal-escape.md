# unicorn/consistent-template-literal-escape
Source: https://bun.com/docs/lint/rules/unicorn/consistent-template-literal-escape

Enforce one way to escape `${` in template literals


To write a literal `${` in a template literal you need to escape it, and three spellings work: a backslash before the `$`, before the `{`, or before both. All three give the same string. This rule keeps the first one, `${`, so an escaped placeholder looks the same everywhere.

Tagged templates aren't checked, because a tag can read the raw text.

`--fix` rewrites the escape.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/consistent-template-literal-escape" = "error" # or "warn"
```


## Examples

Reported:

```js
const usage = `Write $\{name} to insert the name`;
const help = `Write \$\{name} to insert the name`;
```

Not reported:

```js
const usage = `Write \${name} to insert the name`;
```

```js
const pattern = String.raw`$\{name}`;
```
