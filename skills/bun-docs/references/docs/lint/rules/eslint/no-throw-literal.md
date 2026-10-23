# no-throw-literal
Source: https://bun.com/docs/lint/rules/eslint/no-throw-literal

Require `throw` to be given something that can be an `Error`


JavaScript lets you throw any value, but code that catches it expects an `Error`. A thrown string has no stack trace, so you can't see where it came from. `error.message` is `undefined` on it, and `error instanceof Error` is `false`.

The rule only looks at the syntax. It reports anything that can never be an `Error`: strings, numbers, `null`, `undefined`, object literals, template literals, and strings built with `+`. A variable, a property or a call's result could hold an `Error`, so those are allowed. `@typescript-eslint/only-throw-error` checks their types.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-throw-literal" = "error" # or "warn"
```


## Examples

Reported:

```js
function find(id) {
  if (!id) throw "id is required";
  if (id < 0) throw { code: 400 };
  if (id > max) throw "no such id: " + id;
  throw undefined;
}
```

Not reported:

```js
function find(id) {
  if (!id) throw new Error("id is required");
  if (id > max) throw new RangeError(`no such id: ${id}`);

  const error = new Error("bad request");
  error.code = 400;
  throw error;
}
```
