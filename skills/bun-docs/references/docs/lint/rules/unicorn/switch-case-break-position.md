# unicorn/switch-case-break-position
Source: https://bun.com/docs/lint/rules/unicorn/switch-case-break-position

Require `break`, `return`, `continue` and `throw` inside the braces of a `case`


When the body of a `case` is in braces and the `break` comes after the closing brace, the `break` is easy to overlook, and easy to leave behind when you move the block.

The rule reports a `case` that's a block followed by only a `break`, `return`, `continue` or `throw`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/switch-case-break-position" = "error" # or "warn"
```


## Examples

Reported:

```js
switch (event.type) {
  case "open": {
    show(event.target);
  }
  break;
}
```

Not reported:

```js
switch (event.type) {
  case "open": {
    show(event.target);
    break;
  }
  case "close":
    hide(event.target);
    break;
}
```
