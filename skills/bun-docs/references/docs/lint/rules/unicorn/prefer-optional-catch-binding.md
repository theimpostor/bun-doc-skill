# unicorn/prefer-optional-catch-binding
Source: https://bun.com/docs/lint/rules/unicorn/prefer-optional-catch-binding

Require `catch {}` without a parameter when the error is not used


`catch` doesn't need a parameter. A name that's never read sends the reader looking for where the error is handled.

`--fix` removes the parameter and its parentheses.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-optional-catch-binding" = "error" # or "warn"
```


## Examples

Reported:

```js
function parse(text) {
  try {
    return JSON.parse(text);
  } catch (error) {
    return undefined;
  }
}

try {
  await upload(file);
} catch ({ message }) {
  retry(file);
}
```

Not reported:

```js
function parse(text) {
  try {
    return JSON.parse(text);
  } catch {
    return undefined;
  }
}

try {
  await upload(file);
} catch ({ message }) {
  console.error(message);
}
```
