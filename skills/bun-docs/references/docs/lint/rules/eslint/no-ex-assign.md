# no-ex-assign
Source: https://bun.com/docs/lint/rules/eslint/no-ex-assign

Disallow assigning to the error parameter of a `catch` clause


Assigning to a `catch` clause's parameter overwrites the error that was caught. From that line on, nothing in the block can read the original message or stack.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-ex-assign" = "off" # or "error"
```


## Examples

Reported:

```js
try {
  upload(file);
} catch (error) {
  error = new Error("Upload failed");
  report(error);
}
```

Names that the parameter destructures count as well:

```js
try {
  upload(file);
} catch ({ message }) {
  message = "Upload failed";
  report(message);
}
```

Not reported:

```js
try {
  upload(file);
} catch (error) {
  const wrapped = new Error("Upload failed", { cause: error });
  report(wrapped);
}
```

Setting a property keeps the error, so it's allowed:

```js
try {
  upload(file);
} catch (error) {
  error.file = file;
  report(error);
}
```
