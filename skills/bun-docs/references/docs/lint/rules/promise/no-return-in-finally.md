# promise/no-return-in-finally
Source: https://bun.com/docs/lint/rules/promise/no-return-in-finally

Disallow `return` in a `finally()` callback


The chain ignores the value a `finally()` callback returns. The next step gets the result from before the `finally()`, so the returned value is lost.

The rule reports a `return` statement at the top level of the callback's body. An arrow function without braces isn't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/no-return-in-finally" = "error" # or "warn"
```


## Examples

Reported:

```js
loadItems()
  .finally(() => {
    hideSpinner();
    return "done";
  })
  .then(result => console.log(result)); // the items, not "done"
```

Not reported:

```js
loadItems()
  .finally(() => {
    hideSpinner();
  })
  .then(items => console.log(items));

loadItems().finally(() => hideSpinner());
```

Returning a promise does have an effect, because the chain waits for it. The rule reports that `return` too.

```js
query(sql).finally(() => {
  return connection.close();
});
```

Use `await` instead:

```js
query(sql).finally(async () => {
  await connection.close();
});
```
