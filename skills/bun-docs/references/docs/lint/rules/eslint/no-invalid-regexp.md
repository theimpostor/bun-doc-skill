# no-invalid-regexp
Source: https://bun.com/docs/lint/rules/eslint/no-invalid-regexp

Disallow invalid patterns and flags in `RegExp()` and `new RegExp()`


A mistake in a regular expression literal is a syntax error, so you see it right away. A pattern passed to `RegExp` as a string is only checked when that line runs, and then it throws a `SyntaxError`. This rule checks the string ahead of time.

Only string literals are checked. If the pattern or the flags come from a variable, that part is skipped.

This rule is on by default.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-invalid-regexp" = "off" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-invalid-regexp" = ["error", {
  allowConstructorFlags = [], # list of strings
}]
```


## Examples

Reported:

```js
const letters = new RegExp("[a-z");
const digits = RegExp("(\\d+");
const twice = new RegExp("\\d+", "gg");
const unknown = new RegExp("\\d+", "x");
```

Not reported:

```js
const letters = new RegExp("[a-z]");
const digits = RegExp("(\\d+)", "g");
const search = new RegExp(pattern, flags);
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowConstructorFlags` | `[]` | Extra flags to accept, one letter each, for a runtime that supports flags the standard doesn't have. Case matters. |

```js
const digits = new RegExp("\\d+", "x");
```

```js
const digits = new RegExp("\\d+", "X");
```
