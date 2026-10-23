# no-delete-var
Source: https://bun.com/docs/lint/rules/eslint/no-delete-var

Disallow `delete` on variables


`delete` removes a property from an object. It doesn't remove a variable. On a variable declared with `var`, `let` or `const`, it does nothing and returns `false`.

In strict mode and in modules this is already a syntax error. The rule catches it in the scripts where it isn't, such as a `.cjs` file without `"use strict"`.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-delete-var" = "off" # or "error"
```


## Examples

Reported, in a `.cjs` file:

```js
var session = createSession();
delete session;
```

Not reported:

```js
var session = createSession();
session = undefined;

delete cache.session;
```
