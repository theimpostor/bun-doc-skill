# no-await-in-loop
Source: https://bun.com/docs/lint/rules/eslint/no-await-in-loop

Disallow `await` inside of loops


An `await` in a loop makes every iteration wait for the one before it. Ten requests of 100 ms each take a second. If you start them together and await them with `Promise.all`, they take about 100 ms.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-await-in-loop" = "error" # or "warn"
```


## Examples

Reported:

```js
async function loadAll(urls) {
  const pages = [];
  for (const url of urls) {
    pages.push(await fetch(url));
  }
  return pages;
}
```

Not reported:

```js
async function loadAll(urls) {
  return Promise.all(urls.map((url) => fetch(url)));
}
```

A `for await` loop is meant to wait, so an `await` in its body isn't reported:

```js
async function copy(stream, file) {
  for await (const chunk of stream) {
    await file.write(chunk);
  }
}
```

The list a `for ... of` loop runs over is only evaluated once:

```js
async function printUsers() {
  for (const user of await loadUsers()) {
    console.log(user.name);
  }
}
```

## When not to use it

Some loops have to run one step at a time: each page of results gives you the cursor for the next one, a retry waits for the previous attempt, or you don't want to send a server 500 requests at once. Disable the rule for those loops with a comment.
