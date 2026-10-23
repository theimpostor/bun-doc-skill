# unicorn/consistent-existence-index-check
Source: https://bun.com/docs/lint/rules/unicorn/consistent-existence-index-check

Require `=== -1` and `!== -1` to test the result of `indexOf()` and `findIndex()`


`indexOf()`, `lastIndexOf()`, `findIndex()` and `findLastIndex()` return `-1` when they find nothing. `index < 0`, `index >= 0` and `index > -1` all test for that, but they read like range checks. Comparing with `-1` says what you mean: found, or not found.

`--fix` rewrites the comparison.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/consistent-existence-index-check" = "error" # or "warn"
```


## Examples

Reported:

```js
const index = users.findIndex(user => user.id === id);

if (index < 0) {
  throw new Error("No such user");
}

if (index >= 0) {
  users.splice(index, 1);
}
```

Not reported:

```js
const index = users.findIndex(user => user.id === id);

if (index === -1) {
  throw new Error("No such user");
}

if (index !== -1) {
  users.splice(index, 1);
}
```

The rule only follows a `const` that holds the result of one of these methods. It doesn't check a `let`, or a call that's compared in place:

```js
let index = users.indexOf(name);

if (index < 0) {
  index = users.push(name) - 1;
}

if (admins.indexOf(name) < 0) {
  admins.push(name);
}
```
