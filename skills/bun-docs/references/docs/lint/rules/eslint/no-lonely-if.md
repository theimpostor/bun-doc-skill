# no-lonely-if
Source: https://bun.com/docs/lint/rules/eslint/no-lonely-if

Require `else if` instead of an `if` alone in an `else` block


An `else` block that holds nothing but an `if` is an `else if` with one more level of indentation. Each extra condition pushes the code further to the right.

`--fix` rewrites it to `else if`. It leaves the code alone if the `else` block also has a comment, which would be lost.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-lonely-if" = "error" # or "warn"
```


## Examples

Reported:

```js
if (user.isAdmin) {
  showAdminPage();
} else {
  if (user.isMember) {
    showMemberPage();
  } else {
    showLogin();
  }
}
```

Not reported:

```js
if (user.isAdmin) {
  showAdminPage();
} else if (user.isMember) {
  showMemberPage();
} else {
  showLogin();
}
```

Not reported, because the `else` block does something else as well:

```js
if (user.isAdmin) {
  showAdminPage();
} else {
  if (user.isMember) {
    showMemberPage();
  }
  trackVisit(user);
}
```
