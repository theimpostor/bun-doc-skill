# no-return-assign
Source: https://bun.com/docs/lint/rules/eslint/no-return-assign

Disallow assignments in `return` statements


`return total = price + tax;` can be a typo for `return total === price + tax;`, and a reader can't tell which one you meant. Even when you do want the assignment, it hides a side effect in a line that looks like it only returns a value.

The rule also covers an arrow function whose body is an assignment.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-return-assign" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-return-assign" = ["error", "except-parens"] # "except-parens" or "always"
```


## Examples

Reported:

```js
function setName(user, name) {
  return user.name = name;
}

const select = (item) => selected = item;
```

Not reported:

```js
function setName(user, name) {
  user.name = name;
  return name;
}

const select = (item) => {
  selected = item;
};
```

## Options

| Option | What it does |
| --- | --- |
| `"except-parens"` (default) | Allow an assignment that's wrapped in parentheses. |
| `"always"` | Report every assignment in a `return`. |

The parentheses show that the assignment is on purpose:

```js
function next() {
  return (current = current.next);
}
```

```js
function next() {
  return (current = current.next);
}
```
