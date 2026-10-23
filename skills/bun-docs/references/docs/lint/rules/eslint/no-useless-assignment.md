# no-useless-assignment
Source: https://bun.com/docs/lint/rules/eslint/no-useless-assignment

Disallow assigning a value to a variable that is never read afterwards


A value that's overwritten or thrown away before anything reads it does nothing. Often it's left over from an edit, or the wrong variable was assigned.

The rule follows every path through the function. An assignment is reported only if no path reads the value.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-useless-assignment" = "off" # or "error"
```


## Examples

Reported:

```js
function label(user) {
  let name = "guest";
  name = user.name;
  return name;
}
```

```js
function finish(job) {
  let status = job.status;
  log(status);
  status = "done";
}
```

Not reported:

```js
function label(user) {
  let name = "guest";
  if (user) {
    name = user.name;
  }
  return name;
}
```

A variable that an inner function reads is skipped, because that function can run at any time:

```js
function finish(job) {
  let status = job.status;
  job.onClose(() => log(status));
  status = "done";
}
```

`no-unused-vars` handles a variable that's never read at all:

```js
function finish(job) {
  let status = job.status;
  status = "done";
}
```
