# unicorn/no-array-reduce
Source: https://bun.com/docs/lint/rules/unicorn/no-array-reduce

Disallow `reduce()` and `reduceRight()` in favor of a loop


To read a `reduce()`, you have to follow the accumulator through every return in the callback, and its starting value comes last, after the callback. Written as a `for...of` loop, the same code names the result first and updates it in plain statements.

A callback that only combines two values with an operator, such as a sum, is allowed by default.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-array-reduce" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-array-reduce" = ["error", {
  allowSimpleOperations = true,
}]
```


## Examples

Reported:

```js
const byId = users.reduce((result, user) => {
  result[user.id] = user;
  return result;
}, {});
```

Not reported:

```js
const byId = {};
for (const user of users) {
  byId[user.id] = user;
}
```

```js
const total = prices.reduce((sum, price) => sum + price, 0);
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowSimpleOperations` | `true` | Allow a callback that only returns a binary expression, such as `a + b` or `a * b`. |

```js
const total = prices.reduce((sum, price) => sum + price, 0);
```
