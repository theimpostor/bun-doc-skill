# no-proto
Source: https://bun.com/docs/lint/rules/eslint/no-proto

Disallow the `__proto__` property


`object.__proto__` is a getter and setter that objects inherit from `Object.prototype`. An object made with `Object.create(null)` doesn't have it, so on that object `__proto__` is an ordinary property and reading it returns `undefined`. `Object.getPrototypeOf()` and `Object.setPrototypeOf()` work on every object.

Using `__proto__` as a key in an object literal sets the new object's prototype, and that isn't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-proto" = "error" # or "warn"
```


## Examples

Reported:

```js
const parent = user.__proto__;
user["__proto__"] = admin;
```

Not reported:

```js
const parent = Object.getPrototypeOf(user);
Object.setPrototypeOf(user, admin);

const guest = { __proto__: user, name: "guest" };
```
