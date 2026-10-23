# no-case-declarations
Source: https://bun.com/docs/lint/rules/eslint/no-case-declarations

Disallow `let`, `const`, `function` and `class` declarations directly in a `case` clause


All the `case` clauses in a `switch` share one scope. A `let`, `const` or `class` that you declare in one clause is visible in the others, but it only gets its value if its own clause runs. Reading it from another clause throws a `ReferenceError`, and declaring the same name in two clauses is a syntax error.

Put braces around the clause to give it its own scope. A `function` declaration in a clause is reported too. `var` isn't.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-case-declarations" = "off" # or "error"
```


## Examples

Reported:

```js
switch (action.type) {
  case "add":
    const item = action.item;
    list.push(item);
    break;
  default:
    list.length = 0;
}
```

Not reported:

```js
switch (action.type) {
  case "add": {
    const item = action.item;
    list.push(item);
    break;
  }
  default:
    list.length = 0;
}
```
