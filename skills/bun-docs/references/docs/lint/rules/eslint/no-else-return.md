# no-else-return
Source: https://bun.com/docs/lint/rules/eslint/no-else-return

Disallow `else` after an `if` branch that always returns


When the `if` branch ends with `return`, the code after the `if` only runs if the condition was false. An `else` around that code adds a level of indentation and says nothing new.

`--fix` removes the `else` and moves its content out of the block, unless a name declared in the block would clash with one outside it.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-else-return" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-else-return" = ["error", {
  allowElseIf = true,
}]
```


## Examples

Reported:

```js
function label(user) {
  if (user.admin) {
    return "Admin";
  } else {
    return "Member";
  }
}
```

Not reported:

```js
function label(user) {
  if (user.admin) {
    return "Admin";
  }
  return "Member";
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowElseIf` | `true` | Allow `else if` after a branch that returns. |

By default an `else if` is fine:

```js
function label(user) {
  if (user.admin) {
    return "Admin";
  } else if (user.guest) {
    return "Guest";
  }
  return "Member";
}
```

The last `else` of a chain is still reported if every branch before it returns:

```js
function label(user) {
  if (user.admin) {
    return "Admin";
  } else if (user.guest) {
    return "Guest";
  } else {
    return "Member";
  }
}
```

With `allowElseIf: false`, the `else if` is reported too:

```js
function label(user) {
  if (user.admin) {
    return "Admin";
  } else if (user.guest) {
    return "Guest";
  }
  return "Member";
}
```
