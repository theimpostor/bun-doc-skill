# unicorn/no-await-expression-member
Source: https://bun.com/docs/lint/rules/unicorn/no-await-expression-member

Disallow reading a property directly from an `await` expression


`(await getUser(id)).name` needs parentheses, and they're easy to forget. Without them, `await getUser(id).name` reads `name` from the promise and gives you `undefined`. If you destructure, or put the awaited value in a variable, you don't need parentheses and the code reads from left to right.

`--fix-dangerously` rewrites `const name = (await getUser(id)).name` and `const first = (await getPosts(id))[0]` to destructuring. You need to rewrite other forms by hand.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-await-expression-member" = "error" # or "warn"
```


## Examples

Reported:

```js
async function show(id) {
  const name = (await getUser(id)).name;
  const first = (await getPosts(id))[0];
  render(name, first);
}
```

```js
async function load(url) {
  return (await fetch(url)).json();
}
```

Not reported:

```js
async function show(id) {
  const { name } = await getUser(id);
  const [first] = await getPosts(id);
  render(name, first);
}
```

```js
async function load(url) {
  const response = await fetch(url);
  return response.json();
}
```
