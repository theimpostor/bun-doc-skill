# unicorn/no-lonely-if
Source: https://bun.com/docs/lint/rules/unicorn/no-lonely-if

Disallow an `if` as the only statement in another `if` when neither has an `else`


Two nested `if` statements with nothing else between them test one combined condition. Join them with `&&` and you lose a level of indentation and get the whole condition in one place.

`no-lonely-if` without the `unicorn/` prefix is a different rule. It reports an `if` that's the only thing in an `else` block.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-lonely-if" = "error" # or "warn"
```


## Examples

Reported:

```js
if (user) {
  if (user.isAdmin) {
    showSettings();
  }
}
```

Not reported:

```js
if (user && user.isAdmin) {
  showSettings();
}
```

You can't merge the two when either one has an `else`, or when the outer block does something else as well:

```js
if (user) {
  if (user.isAdmin) {
    showSettings();
  }
} else {
  showLogin();
}

if (user) {
  greet(user);
  if (user.isAdmin) {
    showSettings();
  }
}
```
