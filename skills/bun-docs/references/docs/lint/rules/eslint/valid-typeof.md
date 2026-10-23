# valid-typeof
Source: https://bun.com/docs/lint/rules/eslint/valid-typeof

Require `typeof` to be compared with a valid type name


`typeof` returns one of eight strings: `"undefined"`, `"object"`, `"boolean"`, `"number"`, `"string"`, `"function"`, `"symbol"` or `"bigint"`. A comparison with anything else, usually a typo such as `"strnig"`, is never true, and nothing tells you.

The rule checks `==`, `===`, `!=` and `!==` where one side is a `typeof` expression. It reports a string that isn't one of the eight, any other literal such as `null` or a number, and the bare identifier `undefined`. For `undefined`, the report comes with a suggestion that writes `"undefined"`.

This rule is on by default.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"valid-typeof" = "off" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"valid-typeof" = ["error", {
  requireStringLiterals = false,
}]
```


## Examples

Reported:

```js
if (typeof name === "strnig") {
  trim(name);
}

if (typeof callback === undefined) {
  callback = noop;
}

if (typeof user === null) {
  signIn();
}
```

Not reported:

```js
if (typeof name === "string") {
  trim(name);
}

if (typeof callback === "undefined") {
  callback = noop;
}

if (typeof left === typeof right) {
  compare(left, right);
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `requireStringLiterals` | `false` | Also report a comparison with anything that isn't a string literal or another `typeof`, such as a variable. |

By default a variable is allowed, because the rule can't know what it holds:

```js
if (typeof value === expectedType) {
  accept(value);
}
```

With `requireStringLiterals` it's reported:

```js
if (typeof value === expectedType) {
  accept(value);
}
```
