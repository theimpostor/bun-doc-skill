# no-prototype-builtins
Source: https://bun.com/docs/lint/rules/eslint/no-prototype-builtins

Disallow calling `hasOwnProperty` and other `Object.prototype` methods on the object itself


`data.hasOwnProperty("id")` only works if `data` inherits the method and doesn't define a property with that name itself. An object made with `Object.create(null)` doesn't inherit it, so the call throws. An object parsed from JSON can have its own `hasOwnProperty` key, so anyone who sends the input can make the call throw too.

The rule reports calls to `hasOwnProperty`, `isPrototypeOf` and `propertyIsEnumerable`. Use `Object.hasOwn()`, or call the method from `Object.prototype`.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-prototype-builtins" = "off" # or "error"
```


## Examples

Reported:

```js
const data = JSON.parse(body);

if (data.hasOwnProperty("id")) {
  update(data.id);
}

const isChild = base.isPrototypeOf(data);
```

Not reported:

```js
const data = JSON.parse(body);

if (Object.hasOwn(data, "id")) {
  update(data.id);
}

const isChild = Object.prototype.isPrototypeOf.call(base, data);
```
