# no-new
Source: https://bun.com/docs/lint/rules/eslint/no-new

Disallow `new` when the created object is thrown away


`new Thing()` as a standalone statement creates an object and throws it away. Either a variable is missing, or the constructor is only called for its side effects. In that case a plain function says so more clearly.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-new" = "error" # or "warn"
```


## Examples

Reported:

```js
new Router(routes);
```

Not reported:

```js
const router = new Router(routes);

startRouter(routes);
```

## When not to use it

Some libraries start working from the constructor, for example `new Vue({ el: "#app" })`. If you use one, disable the rule on that line or turn it off.
