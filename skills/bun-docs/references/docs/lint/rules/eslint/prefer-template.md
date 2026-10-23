# prefer-template
Source: https://bun.com/docs/lint/rules/eslint/prefer-template

Require template literals instead of string concatenation


In `"Hello, " + user.name + "!"`, quotes and plus signs cut the text into pieces, and a missing space at the edge of a piece is hard to see. A template literal keeps the text in one piece with the values in place.

A chain of `+` is reported if it mixes string literals with anything else. Joining only string literals is allowed, so you can still split a long string over two lines.

`--fix` rewrites the concatenation as a template literal.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"prefer-template" = "error" # or "warn"
```


## Examples

Reported:

```js
const greeting = "Hello, " + user.name + "!";
const url = base + "/users/" + id;
```

Not reported:

```js
const greeting = `Hello, ${user.name}!`;
const url = `${base}/users/${id}`;

const total = price + tax;
const notice = "This sentence is long, " +
  "so it is written as two strings.";
```
