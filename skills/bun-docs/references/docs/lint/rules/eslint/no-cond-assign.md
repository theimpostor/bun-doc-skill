# no-cond-assign
Source: https://bun.com/docs/lint/rules/eslint/no-cond-assign

Disallow assignments in the test of `if`, loops and `? :`


`if (user.role = "admin")` is usually a typo for `===`. It overwrites `user.role`, and the branch always runs because `"admin"` is truthy.

The rule checks the test of `if`, `while`, `do...while`, `for` and `? :`. By default, an extra pair of parentheses around the assignment marks it as intentional.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-cond-assign" = "off" # or "error"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-cond-assign" = ["warn", "except-parens"] # "except-parens" or "always"
```


## Examples

Reported:

```js
if (user.role = "admin") {
  showSettings();
}
```

Not reported:

```js
if (user.role === "admin") {
  showSettings();
}

let node = list.head;
while ((node = node.next)) {
  visit(node);
}
```

## Options

| Option | What it does |
| --- | --- |
| `"except-parens"` (default) | Report a test that is an assignment, unless the assignment has its own parentheses. |
| `"always"` | Report every assignment inside a test, with or without parentheses. |

With `"always"`, an assignment that is only part of the test is reported too:

```js
let match;
while ((match = pattern.exec(text)) !== null) {
  results.push(match[0]);
}
```

The default allows it:

```js
let match;
while ((match = pattern.exec(text)) !== null) {
  results.push(match[0]);
}
```

With the default, the test of `? :` needs two pairs of parentheses. One pair is still reported:

```js
const label = (current = next()) ? current.name : "none";
```

```js
const label = ((current = next())) ? current.name : "none";
```
