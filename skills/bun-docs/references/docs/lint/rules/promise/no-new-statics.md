# promise/no-new-statics
Source: https://bun.com/docs/lint/rules/promise/no-new-statics

Disallow `new` on static `Promise` methods such as `Promise.all`


`Promise.all`, `Promise.resolve` and the other static methods are plain functions, not constructors. Calling one with `new` throws a `TypeError` at run time.

The rule covers `all`, `allSettled`, `any`, `race`, `reject`, `resolve`, `try` and `withResolvers`.

`--fix` removes the `new`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/no-new-statics" = "error" # or "warn"
```


## Examples

Reported:

```js
async function loadPage() {
  return await new Promise.all([loadUser(), loadOrders()]);
}
```

Not reported:

```js
async function loadPage() {
  return await Promise.all([loadUser(), loadOrders()]);
}
```
