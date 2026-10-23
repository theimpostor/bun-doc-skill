# unicorn/throw-new-error
Source: https://bun.com/docs/lint/rules/unicorn/throw-new-error

Require `new` when creating an error


You can create the built-in errors without `new`, but not your own classes. `throw ValidationError("..")` throws a `TypeError` about the missing `new` instead of the error you meant to throw. Always writing `new` works for both.

The rule goes by the name. It reports a call to `Error`, or to any name that starts with a capital letter and ends with `Error`, whether or not the result is thrown.

`--fix` adds `new`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/throw-new-error" = "error" # or "warn"
```


## Examples

Reported:

```js
throw Error("Not found");
throw errors.ValidationError("Name is required");
const timeout = TypeError("Expected a number");
```

Not reported:

```js
throw new Error("Not found");
throw new errors.ValidationError("Name is required");
const timeout = new TypeError("Expected a number");

throw createError(404);
```
