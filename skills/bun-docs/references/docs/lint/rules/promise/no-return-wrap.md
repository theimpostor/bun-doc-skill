# promise/no-return-wrap
Source: https://bun.com/docs/lint/rules/promise/no-return-wrap

Disallow returning `Promise.resolve()` or `Promise.reject()` from a promise callback


`then()` and `catch()` already wrap whatever their callback returns in a promise, and an error thrown in the callback already rejects the chain. So `return Promise.resolve(value)` does the same as `return value`, and `return Promise.reject(error)` does the same as `throw error`.

The rule checks the return values of `then()`, `catch()` and `finally()` callbacks.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/no-return-wrap" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/no-return-wrap" = ["error", {
  allowReject = false,
}]
```


## Examples

Reported:

```js
fetchUser(id).then(user => {
  if (!user.active) {
    return Promise.reject(new Error("inactive user"));
  }
  return Promise.resolve(user.profile);
});
```

Not reported:

```js
fetchUser(id).then(user => {
  if (!user.active) {
    throw new Error("inactive user");
  }
  return user.profile;
});
```

Outside a promise callback, both are fine:

```js
function cachedUser(id) {
  return Promise.resolve(cache.get(id));
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowReject` | `false` | Allow `return Promise.reject(error)`. `Promise.resolve()` is still reported. |

```js
fetchUser(id).catch(err => Promise.reject(new Error("no user", { cause: err })));
```

```js
fetchUser(id).then(user => Promise.resolve(user.profile));
```
