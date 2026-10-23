# unicorn/no-nested-ternary
Source: https://bun.com/docs/lint/rules/unicorn/no-nested-ternary

Disallow deeply nested ternaries, and require parentheses around a ternary in a ternary


In `a ? b : c ? d : e`, it's hard to see which `:` belongs to which `?`. This rule allows one ternary inside another if the inner one is in parentheses. A third level is always reported.

`--fix` adds the parentheses. It doesn't rewrite a third level.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-nested-ternary" = "error" # or "warn"
```


## Examples

Reported:

```js
const size = width > 1200 ? "large" : width > 600 ? "medium" : "small";
```

```js
const size = width > 1200 ? "large" : (width > 600 ? "medium" : (width > 300 ? "small" : "tiny"));
```

Not reported:

```js
const size = width > 1200 ? "large" : (width > 600 ? "medium" : "small");
```

For more than two levels, use `if` statements:

```js
function sizeOf(width) {
  if (width > 1200) return "large";
  if (width > 600) return "medium";
  return width > 300 ? "small" : "tiny";
}
```
