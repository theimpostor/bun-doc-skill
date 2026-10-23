# no-process-exit
Source: https://bun.com/docs/lint/rules/eslint/no-process-exit

Disallow calls to `process.exit()`


`process.exit()` stops the process immediately. Code further up the call stack never gets a chance to handle the problem, `finally` blocks don't run, and output that's still being written can get cut off. If a function deep in a library calls it, the whole application goes down.

Throw an error instead, and let the caller decide. To end with a failure code without stopping early, set `process.exitCode`.

ESLint has deprecated this rule. Use `n/no-process-exit` instead.

## Examples

Reported:

```js
function loadConfig(path) {
  if (!exists(path)) {
    console.error("No config file");
    process.exit(1);
  }
  return read(path);
}
```

Not reported:

```js
function loadConfig(path) {
  if (!exists(path)) {
    throw new Error(`No config file at ${path}`);
  }
  return read(path);
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
```

## When not to use it

A command line tool's entry file is often the right place for `process.exit()`. Turn the rule off for that file.
