# no-unreachable
Source: https://bun.com/docs/lint/rules/eslint/no-unreachable

Disallow code after `return`, `throw`, `break`, and `continue` that can never run


Statements that follow a `return`, `throw`, `break`, or `continue` in the same block never run. Neither does code after a loop that never ends. It's either dead code you can delete, or code that was meant to run and is in the wrong place.

Function declarations and `var` declarations without a value are hoisted, so they aren't reported.

This rule is on by default in JavaScript files. It's off in TypeScript files, where TypeScript finds unreachable code itself.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-unreachable" = "off" # or "error"
```


## Examples

Reported:

```js
function price(item) {
  return item.price * item.quantity;
  console.log("computed", item.id);
}
```

```js
while (true) {
  poll();
}
cleanUp();
```

Not reported:

```js
function price(item) {
  console.log("computing", item.id);
  return item.price * item.quantity;
}
```

```js
function area(shape) {
  return width() * shape.height;

  function width() {
    return shape.width;
  }
}
```

`super()` creates a subclass's fields. If the constructor never calls it, the fields are reported:

```js
class Admin extends User {
  role = "admin";

  constructor() {
    return loadAdmin();
  }
}
```
