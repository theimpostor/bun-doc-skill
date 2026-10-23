# no-empty
Source: https://bun.com/docs/lint/rules/eslint/no-empty

Disallow empty block statements


An empty block is usually code that was never finished, or something a refactor left behind. An empty `catch` is worse, because the error disappears and nothing tells you that the call failed.

A block with a comment in it isn't reported, so you can say why it's empty. Empty function bodies aren't reported either. Use `no-empty-function` for those.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-empty" = "off" # or "error"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-empty" = ["warn", {
  allowEmptyCatch = false,
}]
```


## Examples

Reported:

```js
try {
  cache.clear();
} catch (error) {}
```

```js
if (user.active) {
}

switch (user.role) {
}
```

Not reported:

```js
try {
  cache.clear();
} catch (error) {
  // The cache is optional. A failure here changes nothing.
}

function noop() {}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowEmptyCatch` | `false` | Allow an empty `catch` block. |

```js
try {
  cache.clear();
} catch (error) {}
```

Other empty blocks are still reported, including the `finally` of the same statement:

```js
try {
  cache.clear();
} catch (error) {
} finally {
}
```
