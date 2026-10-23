# oxc/double-comparisons
Source: https://bun.com/docs/lint/rules/oxc/double-comparisons

Disallow two comparisons of the same values that one operator can express


`a === b || a < b` is a long way to write `a <= b`. Readers have to check that both halves compare the same two values before they can see what the condition means.

| Written | Means |
| --- | --- |
| `a == b || a < b`, `a === b || a < b` | `a <= b` |
| `a == b || a > b`, `a === b || a > b` | `a >= b` |
| `a < b || a > b` | `a != b` |
| `a <= b && a >= b` | `a == b` |

The halves can be in either order, and one of them can be flipped, so `a < b || b < a` is reported too.

`--fix-suggestions` rewrites the condition with the single operator.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/double-comparisons" = "error" # or "warn"
```


## Examples

Reported:

```js
if (stock === minimum || stock < minimum) {
  reorder();
}

const changed = before < after || before > after;
```

Not reported:

```js
if (stock <= minimum) {
  reorder();
}

const changed = before !== after;
```

## When not to use it

The short form doesn't always mean the same thing. `a < b || a > b` is `false` when one side is `NaN`, but `a != b` is `true`. For two `Date` objects, `a <= b && a >= b` compares the times, but `a == b` only tests whether they're the same object.
