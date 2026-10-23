# n/handle-callback-err
Source: https://bun.com/docs/lint/rules/node/handle-callback-err

Require callbacks to use their error parameter


A Node.js callback gets the error as its first argument. If the function never looks at it, a failure goes unnoticed, and the code carries on with a result that's `undefined`.

The rule reports a function with a first parameter named `err` that's never used in its body. Any use counts. The rule doesn't check what you do with the error.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/handle-callback-err" = "error" # or "warn"
```


## Examples

Reported:

```js
fs.readFile("config.json", (err, data) => {
  start(JSON.parse(data));
});
```

Not reported:

```js
fs.readFile("config.json", (err, data) => {
  if (err) {
    throw err;
  }
  start(JSON.parse(data));
});
```

## Options

The option is the name of the error parameter. The default is `"err"`. If it starts with `^`, it's treated as a regular expression.

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/handle-callback-err" = ["error", "^(err|error)$"]
```

```js
server.close(function (error) {
  console.log("closed");
});

socket.end(function (err) {
  console.log("ended");
});
```

A plain name replaces `err`, so `err` is no longer checked:

```js
socket.end(function (err) {
  console.log("ended");
});
```
