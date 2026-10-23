# unicorn/custom-error-definition
Source: https://bun.com/docs/lint/rules/unicorn/custom-error-definition

Enforce that subclasses of `Error` set `name` and pass the message to `super()`


A class that extends `Error` inherits `name`, so without more work `String(new ValidationError("Bad email"))` is `"Error: Bad email"`, and a check such as `error.name === "ValidationError"` never matches.

The rule looks at every named class that extends `Error` or a class with a name like `TypeError` or `HttpError`. It reports:

- a `name` that's missing, or is anything other than the class name written as a string
- a constructor that doesn't call `super()`
- `this.message = message` instead of `super(message)`
- a class name that doesn't end in `Error` or doesn't start with a capital letter
- `exports.A = class B extends Error`, where the two names differ


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/custom-error-definition" = "error" # or "warn"
```


## Examples

Reported:

```js
class ValidationError extends Error {}
```

```js
class ValidationError extends Error {
  constructor(message) {
    super();
    this.message = message;
    this.name = this.constructor.name;
  }
}
```

```js
class Validation extends Error {
  name = "Validation";
}
```

Not reported:

```js
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}
```

A class field works too:

```js
class ValidationError extends Error {
  name = "ValidationError";
}
```
