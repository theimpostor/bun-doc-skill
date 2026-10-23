# no-setter-return
Source: https://bun.com/docs/lint/rules/eslint/no-setter-return

Disallow returning a value from a setter


The value a setter returns goes nowhere. `user.name = "Ada"` evaluates to `"Ada"` no matter what the setter does. A `return value` in a setter is dead code, or a sign that the function was meant to be a getter or a method.

The rule checks `set` in classes and object literals, and the `set` function of a descriptor passed to `Object.defineProperty`, `Object.defineProperties`, `Object.create` or `Reflect.defineProperty`. A bare `return;` to leave early is fine.

This rule is on by default in JavaScript files. It's off in TypeScript files, where TypeScript reports the same mistake.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-setter-return" = "off" # or "error"
```


## Examples

Reported:

```js
class User {
  set name(value) {
    this._name = value;
    return this;
  }
}

Object.defineProperty(config, "port", {
  set(value) {
    return Number(value);
  },
});
```

Not reported:

```js
class User {
  set name(value) {
    if (!value) {
      return;
    }
    this._name = value;
  }
}
```
