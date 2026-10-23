# n/no-process-exit
Source: https://bun.com/docs/lint/rules/node/no-process-exit

Disallow `process.exit()`


`process.exit()` stops the process immediately. Output that hasn't been written yet is lost, `finally` blocks don't run, and the code that called yours doesn't get a chance to handle the problem or clean up.

Throw an error instead. If nothing catches it, the process ends with a stack trace and a failing exit code. To end with a specific exit code, set `process.exitCode` and let the process finish by itself.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/no-process-exit" = "error" # or "warn"
```


## Examples

Reported:

```js
if (!config.valid) {
  console.error("invalid config");
  process.exit(1);
}
```

Not reported:

```js
if (!config.valid) {
  throw new Error("invalid config");
}
```

```js
if (!config.valid) {
  console.error("invalid config");
  process.exitCode = 1;
}
```

## When not to use it

A command line tool's entry file is a reasonable place for `process.exit()`, for example to stop while timers or sockets are still open.
