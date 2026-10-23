# unicorn/no-object-as-default-parameter
Source: https://bun.com/docs/lint/rules/unicorn/no-object-as-default-parameter

Disallow an object literal with properties as the default value of a parameter


A default value is only used when the whole argument is missing. As soon as the caller passes an object with even one property, the default object is dropped and its other properties are `undefined`. Destructure the parameter and give each property its own default.

An empty object, `options = {}`, is allowed.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-object-as-default-parameter" = "error" # or "warn"
```


## Examples

Reported:

```js
function connect(options = { retries: 3, secure: true }) {
  return open(options.retries, options.secure);
}

connect({ retries: 5 }); // options.secure is undefined
```

Not reported:

```js
function connect({ retries = 3, secure = true } = {}) {
  return open(retries, secure);
}

connect({ retries: 5 }); // secure is true
```
