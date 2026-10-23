# no-eq-null
Source: https://bun.com/docs/lint/rules/eslint/no-eq-null

Disallow comparing with `null` using `==` or `!=`


`value == null` is `true` for `null` and also for `undefined`. If you meant only `null`, the check lets `undefined` through. If you meant both, the next reader can't tell that from the code.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-eq-null" = "error" # or "warn"
```


## Examples

Reported:

```js
if (user == null) {
  redirect("/login");
}

while (node != null) {
  node = node.next;
}
```

Not reported:

```js
if (user === null) {
  redirect("/login");
}

if (session === null || session === undefined) {
  redirect("/login");
}
```

## When not to use it

`== null` is a common shorthand for testing for `null` and `undefined` at once. If your code does that on purpose, leave this rule off. `eqeqeq` with the `"smart"` option allows `== null` and still reports `value == other`.
