# default-param-last
Source: https://bun.com/docs/lint/rules/eslint/default-param-last

Require parameters with a default value to come after the required ones


A default value is used when the caller leaves the argument out, but you can only leave out arguments at the end of a call. If a required parameter comes after it, the caller has to write `createUser(undefined, "Ada")` to get the default.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"default-param-last" = "error" # or "warn"
```


## Examples

Reported:

```js
function createUser(role = "member", name) {
  return { name, role };
}
```

Not reported:

```js
function createUser(name, role = "member") {
  return { name, role };
}

function log(level = "info", ...messages) {
  console[level](...messages);
}
```
