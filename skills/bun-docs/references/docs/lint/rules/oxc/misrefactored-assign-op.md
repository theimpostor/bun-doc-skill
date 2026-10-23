# oxc/misrefactored-assign-op
Source: https://bun.com/docs/lint/rules/oxc/misrefactored-assign-op

Disallow `a += a + b`, where the target is repeated on the right


If you change `total = total + price` to use `+=` and forget to remove `total` from the right side, you get `total += total + price`. That adds `total` twice.

The rule reports a compound assignment when the right side uses the same operator and the target is its left operand. For `+`, `*`, `&`, `|` and `^`, where the order doesn't matter, it's also reported when the target is the right operand. The target can be a variable or a property such as `cart.total`.

`--fix-suggestions` removes the repeated target, so `total += total + price` becomes `total += price`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/misrefactored-assign-op" = "error" # or "warn"
```


## Examples

Reported:

```js
total += total + price;
scale *= 2 * scale;
cart.remaining -= cart.remaining - used;
```

Not reported:

```js
total += price;
scale *= 2;
cart.remaining -= used;

// A different operator, or an order that matters
total += total * rate;
remaining -= limit - remaining;
```
