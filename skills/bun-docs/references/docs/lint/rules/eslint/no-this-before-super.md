# no-this-before-super
Source: https://bun.com/docs/lint/rules/eslint/no-this-before-super

Disallow `this` and `super.x` before `super()` in a constructor


In the constructor of a class that extends another class, `this` doesn't exist until `super()` has returned. Using `this` or `super.method()` before that throws a `ReferenceError` when the object is created.

The rule follows the constructor's branches, so `super()` must be called on every path that leads to the `this`. Classes without `extends` aren't checked.

This rule is on by default in JavaScript files. It's off in TypeScript files, where TypeScript reports the same mistake.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-this-before-super" = "off" # or "warn"
```


## Examples

Reported:

```js
class Admin extends User {
  constructor(name) {
    this.role = "admin";
    super.validate(name);
    super(name);
  }
}
```

```js
class Admin extends User {
  constructor(name) {
    if (name) {
      super(name);
    }
    this.role = "admin";
  }
}
```

Not reported:

```js
class Admin extends User {
  constructor(name) {
    super(name);
    this.role = "admin";
  }
}
```

```js
class Admin extends User {
  constructor(name) {
    if (name) {
      super(name);
    } else {
      super("admin");
    }
    this.role = "admin";
  }
}
```
