# promise/no-nesting
Source: https://bun.com/docs/lint/rules/promise/no-nesting

Disallow `then()` and `catch()` nested inside another `then()` or `catch()`


A `then()` inside a `then()` adds a level of indentation for every step, and a `catch()` on the inner chain doesn't see errors from the outer one. Return the inner promise and continue the chain one level up.

A nested callback that uses a variable from the outer callback can't move up, so it isn't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/no-nesting" = "error" # or "warn"
```


## Examples

Reported:

```js
getUser(id).then(user => {
  return getOrders(user).then(orders => render(orders));
});
```

Not reported:

```js
getUser(id)
  .then(user => getOrders(user))
  .then(orders => render(orders));
```

Here the inner callback needs `user`:

```js
getUser(id).then(user => {
  return getOrders(user).then(orders => render(user, orders));
});
```
