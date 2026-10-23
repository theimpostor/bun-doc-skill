# no-negated-condition
Source: https://bun.com/docs/lint/rules/eslint/no-negated-condition

Disallow negated conditions in `if`/`else` and in ternaries


When both branches are there, a negated condition makes the `else` a double negative: "if not logged in .. otherwise ..". Swapping the branches removes the negation and says the same thing.

The rule looks at conditions of the form `!x`, `a != b` and `a !== b`. An `if` without `else` is fine, and so is one followed by `else if`.

With an oxlint config, `--fix` removes the negation and swaps the branches.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-negated-condition" = "error" # or "warn"
```


## Examples

Reported:

```js
if (!user) {
  redirect("/login");
} else {
  render(user);
}
```

```js
const label = count !== 1 ? "items" : "item";
```

Not reported:

```js
if (user) {
  render(user);
} else {
  redirect("/login");
}

const label = count === 1 ? "item" : "items";
```

```js
if (!user) {
  redirect("/login");
}

if (!user) {
  redirect("/login");
} else if (user.isAdmin) {
  renderAdmin(user);
}
```
