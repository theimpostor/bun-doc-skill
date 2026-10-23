# no-useless-return
Source: https://bun.com/docs/lint/rules/eslint/no-useless-return

Disallow a `return` without a value where the function ends anyway


A bare `return;` is for leaving a function early. If nothing would run after it anyway, it doesn't change anything and you can delete it.

`--fix` removes the statement.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-useless-return" = "error" # or "warn"
```


## Examples

Reported:

```js
function reset(form) {
  form.clear();
  return;
}

function notify(user) {
  if (user.muted) {
    return;
  } else {
    send(user);
  }
}
```

Not reported:

```js
function reset(form) {
  form.clear();
}

function notify(user) {
  if (user.muted) {
    return;
  }
  send(user);
}

function find(id) {
  return undefined;
}
```
