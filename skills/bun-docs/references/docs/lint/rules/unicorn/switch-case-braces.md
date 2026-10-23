# unicorn/switch-case-braces
Source: https://bun.com/docs/lint/rules/unicorn/switch-case-braces

Enforce braces, or no braces, around the body of each `case`


All the `case` clauses in a `switch` share one scope. A `const` declared in one clause is in scope in the next, and declaring the same name in two clauses is a syntax error. Braces give each clause its own scope.

A `case` without a body, which falls through to the next one, is never reported. Empty braces, as in `case 1: {}`, are always reported.

`--fix` adds or removes the braces.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/switch-case-braces" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/switch-case-braces" = ["error", "always"] # "always" or "avoid"
```


## Examples

Reported:

```js
switch (event.type) {
  case "open":
    show(event.target);
    break;
  default:
    ignore(event);
}
```

Not reported:

```js
switch (event.type) {
  case "click":
  case "open": {
    show(event.target);
    break;
  }
  default: {
    ignore(event);
  }
}
```

## Options

| Option | What it does |
| --- | --- |
| `"always"` (default) | Require braces around the whole body of every `case`. |
| `"avoid"` | Report braces unless the block declares a variable or a function. |

```js
switch (event.type) {
  case "open": {
    show(event.target);
    break;
  }
}
```

```js
switch (event.type) {
  case "open":
    show(event.target);
    break;
  case "close": {
    const panel = find(event.target);
    hide(panel);
    break;
  }
}
```
