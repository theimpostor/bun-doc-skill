# unicorn/no-await-in-promise-methods
Source: https://bun.com/docs/lint/rules/unicorn/no-await-in-promise-methods

Disallow `await` on the elements of the array passed to `Promise.all()` and similar methods


`Promise.all([await loadUser(), await loadPosts()])` waits for the user before it starts loading the posts. The requests run one after the other, and `Promise.all()` only gets finished values, so it has nothing left to do. With `Promise.race()` and `Promise.any()`, there's no race either.

The rule checks `Promise.all()`, `Promise.allSettled()`, `Promise.any()`, and `Promise.race()`.

`--fix-suggestions` removes the `await`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-await-in-promise-methods" = "error" # or "warn"
```


## Examples

Reported:

```js
async function loadPage(id) {
  const [user, posts] = await Promise.all([await loadUser(id), await loadPosts(id)]);
  render(user, posts);
}
```

Not reported:

```js
async function loadPage(id) {
  const [user, posts] = await Promise.all([loadUser(id), loadPosts(id)]);
  render(user, posts);
}
```
