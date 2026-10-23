# handle-callback-err
Source: https://bun.com/docs/lint/rules/eslint/handle-callback-err

Require callbacks to use their error parameter


A Node.js-style callback gets the error as its first argument. If the function never looks at it, a failure goes unnoticed and the code carries on with an `undefined` result.

The rule reports a function if its first parameter is named `err` and is never used. Any use counts as handling it.

ESLint has deprecated this rule. Use `n/handle-callback-err` instead.

## Examples

Reported:

```js
fs.readFile(path, "utf8", function (err, text) {
  render(text);
});
```

Not reported:

```js
fs.readFile(path, "utf8", function (err, text) {
  if (err) {
    showError(err);
    return;
  }
  render(text);
});
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
handle-callback-err = ["error", "^(err|error)$"]
```

The only option is a string with the name of the error parameter. The default is `"err"`. A string that starts with `^` is a regular expression that the name must match.

```js
fs.readFile(path, "utf8", (error, text) => {
  render(text);
});
```

```js
fs.readFile(path, "utf8", (error, text) => {
  render(text);
});

fs.unlink(path, (err) => {
  done();
});
```

With the default, a parameter named `error` isn't checked:

```js
fs.readFile(path, "utf8", (error, text) => {
  render(text);
});
```
