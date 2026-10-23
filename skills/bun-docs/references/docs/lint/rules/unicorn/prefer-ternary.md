# unicorn/prefer-ternary
Source: https://bun.com/docs/lint/rules/unicorn/prefer-ternary

Require a ternary instead of an `if`/`else` where both branches do the same kind of thing


When both branches of an `if`/`else` only return, throw, `await`, `yield`, or assign to the same variable, the statement repeats itself and the only difference is the value. A ternary writes the common part once.

The rule skips an `if` when it's an `else if`, when a branch has more than one statement, or when the condition or one of the values is already a ternary.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-ternary" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
# "always" or "only-single-line"
"unicorn/prefer-ternary" = ["error", "always"]
```


## Examples

Reported:

```js
function label(user) {
  if (user.isAdmin) {
    return "admin";
  } else {
    return "member";
  }
}

let timeout;
if (retrying) {
  timeout = 5000;
} else {
  timeout = 1000;
}
```

Not reported:

```js
function label(user) {
  return user.isAdmin ? "admin" : "member";
}

const timeout = retrying ? 5000 : 1000;

if (retrying) {
  attempts = 0;
} else {
  failures = 0;
}
```

## Options

| Option | What it does |
| --- | --- |
| `"always"` (default) | Report every `if`/`else` that can be a ternary. |
| `"only-single-line"` | Only report when the condition and the statement in each branch fit on one line each. |

```js
if (cached) {
  result = cache.get(key);
} else {
  result = load({
    key,
    retries: 3,
  });
}
```

```js
if (cached) {
  result = cache.get(key);
} else {
  result = load(key);
}
```
