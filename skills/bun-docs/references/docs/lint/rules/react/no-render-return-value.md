# react/no-render-return-value
Source: https://bun.com/docs/lint/rules/react/no-render-return-value

Disallow using the return value of `ReactDOM.render`


`ReactDOM.render` returns the root component's instance, but only if React has rendered it by the time the call returns. React doesn't promise that. To get the instance, give the root element a `ref` callback. React calls it when the instance exists.

The rule reports the call when its result is stored in a variable or a property, assigned, or returned.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-render-return-value" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const app = ReactDOM.render(<App />, document.body);
```

```jsx
function mount(root) {
  return ReactDOM.render(<App />, root);
}
```

Not reported:

```jsx
let app;

ReactDOM.render(<App ref={instance => (app = instance)} />, document.body);
```
