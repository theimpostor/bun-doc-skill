# unicorn/no-negation-in-equality-check
Source: https://bun.com/docs/lint/rules/unicorn/no-negation-in-equality-check

Disallow `!` on the left side of `===`, `!==`, `==`, and `!=`


`!` binds tighter than `===`, so `!a === b` means `(!a) === b`. It turns `a` into `true` or `false` and compares that with `b`. You almost always meant `a !== b`.

`--fix-suggestions` removes the `!` and flips the operator.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-negation-in-equality-check" = "error" # or "warn"
```


## Examples

Reported:

```js
if (!user.role === "admin") {
  deny();
}
```

Not reported:

```js
if (user.role !== "admin") {
  deny();
}
```

If you do want to compare the negated value, wrap it in parentheses to say so. `!!value`, which converts to a boolean, is also allowed:

```js
if ((!isOpen) === wasOpen) {
  toggle();
}

if (!!selected === expected) {
  confirm();
}
```
