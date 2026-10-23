# no-debugger
Source: https://bun.com/docs/lint/rules/eslint/no-debugger

Disallow `debugger` statements


`debugger` pauses the program when a debugger is attached, for example when the browser's developer tools are open. It's useful while you track down a bug. If you commit one by accident, the page freezes for anyone who has dev tools open.

This rule is on by default.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-debugger" = "off" # or "warn"
```


## Examples

Reported:

```js
function total(items) {
  debugger;
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

Not reported:

```js
function total(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}
```
