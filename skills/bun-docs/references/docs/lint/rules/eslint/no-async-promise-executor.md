# no-async-promise-executor
Source: https://bun.com/docs/lint/rules/eslint/no-async-promise-executor

Disallow an async function as a Promise executor


If the function you pass to `new Promise` is async and it throws, or something it awaits rejects, the new promise never hears about it. It stays pending forever, and a `.catch()` on it or a `try` around its `await` never sees the error.

An `await` in the executor also means that you already have a promise, so you rarely need `new Promise` at all.

This rule is on by default.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-async-promise-executor" = "off" # or "warn"
```


## Examples

Reported:

```js
const user = new Promise(async (resolve) => {
  const response = await fetch("/api/user");
  resolve(await response.json());
});
```

Not reported:

```js
async function loadUser() {
  const response = await fetch("/api/user");
  return response.json();
}

const user = loadUser();
```
