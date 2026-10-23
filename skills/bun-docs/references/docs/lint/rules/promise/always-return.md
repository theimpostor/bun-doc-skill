# promise/always-return
Source: https://bun.com/docs/lint/rules/promise/always-return

Require every `then()` callback to return a value or throw


A `then()` callback that returns nothing passes `undefined` to the next step in the chain. If the callback started more async work, the chain doesn't wait for it.

The rule checks the first argument of `then()` when it's a function with a `{ }` body. Every path through it must end with `return`, `throw`, `process.exit()` or `process.abort()`. A bare `return;` is enough.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/always-return" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/always-return" = ["error", {
  ignoreLastCallback = false,
  ignoreAssignmentVariable = ["globalThis"],
}]
```


## Examples

Reported:

```js
fetchUser(id)
  .then(user => {
    user.lastSeen = Date.now();
  })
  .then(user => render(user)); // user is undefined
```

Not reported:

```js
fetchUser(id)
  .then(user => {
    user.lastSeen = Date.now();
    return user;
  })
  .then(user => render(user));

migrate(database).then(() => {
  process.exit(0);
});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreLastCallback` | `false` | Allow the last `then()` of a chain to return nothing, if nothing uses the result. |
| `ignoreAssignmentVariable` | `["globalThis"]` | Allow the last `then()` of a chain to return nothing if it assigns to one of these variables or to a property of one. Your list replaces the default. |

The last `then()` can be followed by `catch()` or `finally()`, and the chain can be awaited:

```js
fetchUser(id)
  .then(user => user.profile)
  .then(profile => {
    render(profile);
  })
  .catch(showError);
```

If the result is stored or returned, other code can still chain on it, so it's reported:

```js
const rendered = fetchUser(id).then(user => {
  render(user);
});
```

With the default `ignoreAssignmentVariable`:

```js
fetchUser(id).then(user => {
  globalThis.currentUser = user;
});
```

```js
fetchUser(id).then(user => {
  window.currentUser = user;
});
```
