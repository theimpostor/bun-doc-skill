# no-useless-concat
Source: https://bun.com/docs/lint/rules/eslint/no-useless-concat

Disallow joining two string literals with `+` on the same line


`"a" + "b"` is a longer way to write `"ab"`. Two literals next to each other are usually left over after someone removed a variable between them.

Both plain strings and template literals count. Strings on different lines are allowed, because that's a common way to break a long string.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-useless-concat" = "error" # or "warn"
```


## Examples

Reported:

```js
const greeting = "Hello, " + "world";
const path = base + "/api" + `/users`;
```

Not reported:

```js
const greeting = "Hello, world";
const path = base + "/api/users";
const label = "user " + id;

const message = "This sentence is too long for one line, " +
  "so it goes on here.";
```
