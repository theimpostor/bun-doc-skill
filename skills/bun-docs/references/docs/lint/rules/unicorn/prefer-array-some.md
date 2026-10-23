# unicorn/prefer-array-some
Source: https://bun.com/docs/lint/rules/unicorn/prefer-array-some

Require `.some()` to test whether an array has a matching element


`.some()` answers "is there a match?" with `true` or `false`, and stops at the first one. The other ways to ask are longer, and some are wrong or slow:

- `if (items.find(fn))` is false when the element it finds is `0` or `""`.
- `.filter(fn).length > 0` tests every element and builds an array only to count it.

`--fix-suggestions` rewrites the `.find()`, `.findLast()` and `.filter()` forms to `.some()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-array-some" = "error" # or "warn"
```


## Examples

Reported:

```js
if (users.find(user => user.isAdmin)) {
  showAdminPanel();
}

const hasAdmin = users.find(user => user.isAdmin) !== undefined;
const hasGuest = users.findIndex(user => user.isGuest) !== -1;
const hasActive = users.filter(user => user.isActive).length > 0;
```

Not reported:

```js
if (users.some(user => user.isAdmin)) {
  showAdminPanel();
}

const hasAdmin = users.some(user => user.isAdmin);
const hasGuest = users.some(user => user.isGuest);
const hasActive = users.some(user => user.isActive);
```

Code that uses the element, the index or the count isn't reported:

```js
const admin = users.find(user => user.isAdmin);
const position = users.findIndex(user => user.isGuest);
const enough = users.filter(user => user.isActive).length > 2;
```
