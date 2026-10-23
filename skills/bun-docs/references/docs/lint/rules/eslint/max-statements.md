# max-statements
Source: https://bun.com/docs/lint/rules/eslint/max-statements

Enforce a maximum number of statements in a function


A function with a long list of statements usually does several jobs, and you have to read all of it to change any part. This rule reports any function with more statements than the maximum, which is 10 by default.

Statements in nested blocks count too. An inner function's statements only count for the inner function.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"max-statements" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"max-statements" = ["error", 10, {
  ignoreTopLevelFunctions = false,
}]
```


## Examples

With a maximum of 3, this function with 4 statements is reported:

```js
function register(form) {
  const user = parse(form);
  validate(user);
  save(user);
  sendWelcomeMail(user);
}
```

Not reported:

```js
function register(form) {
  const user = parse(form);
  validate(user);
  return saveAndWelcome(user);
}
```

This function has 3 statements, the `if` and the two in its block, so a maximum of 2 reports it:

```js
function log(message) {
  if (verbose) {
    console.log(message);
    count++;
  }
}
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
max-statements = ["error", 15, { ignoreTopLevelFunctions = true }]
```

The first option is the maximum, as a number or as `{ "max": number }`. `maximum` is an older name for `max`. The second option is an object:

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreTopLevelFunctions` | `false` | Don't report a file's only top-level function, such as a wrapper around a whole script. |

With it, this passes with a maximum of 2:

```js
(function () {
  const app = createApp();
  app.use(router);
  app.listen(3000);
})();
```

In a file with two or more top-level functions, the option has no effect:

```js
function start() {
  const app = createApp();
  app.use(router);
  app.listen(3000);
}

function stop() {}
```
