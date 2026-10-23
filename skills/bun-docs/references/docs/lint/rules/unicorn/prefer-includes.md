# unicorn/prefer-includes
Source: https://bun.com/docs/lint/rules/unicorn/prefer-includes

Require `.includes()` instead of comparing `.indexOf()` with `-1` or `0`


`tags.indexOf("draft") !== -1` asks for a position and then throws it away. `tags.includes("draft")` asks the question you mean, and there's no `-1`, `0`, `>` or `>=` to get wrong.

The rule reports `!== -1`, `!= -1`, `> -1`, `>= 0`, `=== -1`, `== -1` and `< 0` after a call to `indexOf()`. It doesn't know types, so it reports any object with an `indexOf` method.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-includes" = "error" # or "warn"
```


## Examples

Reported:

```js
if (tags.indexOf("draft") !== -1) {
  hide(post);
}

if (email.indexOf("@") < 0) {
  reject(email);
}
```

Not reported:

```js
if (tags.includes("draft")) {
  hide(post);
}

if (!email.includes("@")) {
  reject(email);
}
```

Code that uses the position is fine:

```js
const at = email.indexOf("@");
const hasName = email.indexOf("@") > 0;
```
