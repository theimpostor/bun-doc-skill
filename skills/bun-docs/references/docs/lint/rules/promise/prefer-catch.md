# promise/prefer-catch
Source: https://bun.com/docs/lint/rules/promise/prefer-catch

Require `catch()` instead of a second argument to `then()`


The second argument of `then(a, b)` only handles a rejection from before the `then()`. If `a` itself throws, `b` isn't called. A `catch()` after the `then()` handles both.

The rule only reports a `then()` call with two arguments when it's a statement by itself. One that's returned, awaited, assigned, or followed by more of the chain isn't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/prefer-catch" = "error" # or "warn"
```


## Examples

Reported:

```js
loadItems().then(render, showError); // an error in render is not handled
```

```js
loadItems().then(null, showError);
```

Not reported:

```js
loadItems().then(render).catch(showError);
loadItems().catch(showError);
```

```js
function refresh() {
  return loadItems().then(render, showError);
}
```
