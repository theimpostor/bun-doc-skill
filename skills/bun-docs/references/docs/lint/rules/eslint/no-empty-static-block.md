# no-empty-static-block
Source: https://bun.com/docs/lint/rules/eslint/no-empty-static-block

Disallow empty `static {}` blocks in classes


A `static` block runs once, when the class is defined. An empty one does nothing. It's usually something a refactor left behind, or setup code that was never written.

A block with a comment in it isn't reported.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-empty-static-block" = "off" # or "error"
```


## Examples

Reported:

```js
class Config {
  static values = new Map();

  static {}
}
```

Not reported:

```js
class Config {
  static values = new Map();

  static {
    Config.values.set("mode", process.env.NODE_ENV);
  }
}
```

```js
class Config {
  static {
    // Values are loaded on first use.
  }
}
```
