# oxc/missing-throw
Source: https://bun.com/docs/lint/rules/oxc/missing-throw

Require `throw` before a `new Error()` that is not used


A statement that's only `new Error("...")` creates an error and throws it away. Nothing is thrown, and the code carries on as if the check passed.

An error that's assigned, returned or passed to a function isn't reported. Only `Error` itself is checked, not other classes such as `TypeError`.

`--fix-suggestions` adds the `throw`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/missing-throw" = "error" # or "warn"
```


## Examples

Reported:

```js
function setAge(age) {
  if (age < 0) {
    new Error("age must not be negative");
  }
  user.age = age;
}
```

Not reported:

```js
function setAge(age) {
  if (age < 0) {
    throw new Error("age must not be negative");
  }
  user.age = age;
}

const timeout = new Error("timed out");
reject(new Error("canceled"));
```
