# no-unsafe-negation
Source: https://bun.com/docs/lint/rules/eslint/no-unsafe-negation

Disallow negating the left operand of `in` and `instanceof`


`!` binds tighter than `in` and `instanceof`. So `!key in cache` means `(!key) in cache`, which asks if `cache` has a property called `"true"` or `"false"`. And `!error instanceof TypeError` is always `false`, because a boolean isn't an instance of anything.

The rule can't tell which meaning you want, so it suggests both: negate the whole expression, or put the negation in parentheses.

This rule is on by default in JavaScript files. It's off in TypeScript files, where the type checker reports the same thing.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-unsafe-negation" = "off" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-unsafe-negation" = ["error", {
  enforceForOrderingRelations = false,
}]
```


## Examples

Reported:

```js
if (!key in cache) {
  cache[key] = load(key);
}

if (!error instanceof TypeError) {
  throw error;
}
```

Not reported:

```js
if (!(key in cache)) {
  cache[key] = load(key);
}

if (!(error instanceof TypeError)) {
  throw error;
}
```

If you do want to negate the left operand, say so with parentheses:

```js
const hasFlag = (!enabled) in counts;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `enforceForOrderingRelations` | `false` | Also check `<`, `>`, `<=` and `>=`. |

`!count < limit` compares `true` or `false` with `limit`:

```js
if (!count < limit) {
  stop();
}
```

```js
if (!(count < limit)) {
  stop();
}
```
