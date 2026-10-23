# unicorn/no-array-reverse
Source: https://bun.com/docs/lint/rules/unicorn/no-array-reverse

Require `toReversed()` instead of `reverse()`, which changes the array


`reverse()` reverses the array in place and returns that same array. After `const newestFirst = posts.reverse()`, `posts` is reversed too. `toReversed()` returns a new array and leaves the original alone.

`--fix-suggestions` replaces `reverse` with `toReversed`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-array-reverse" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-array-reverse" = ["error", {
  allowExpressionStatement = true,
}]
```


## Examples

Reported:

```js
const newestFirst = posts.reverse();
```

Copying the array first is reported too, because `toReversed()` already makes a copy:

```js
const newestFirst = [...posts].reverse();
```

Not reported:

```js
const newestFirst = posts.toReversed();
```

A call used as a standalone statement is allowed by default. Nothing uses the result, so changing the array is the point:

```js
posts.reverse();
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowExpressionStatement` | `true` | Allow `array.reverse();` as a standalone statement. |

```js
posts.reverse();
```

## When not to use it

`toReversed()` is part of ES2023. Turn the rule off if your code needs to run somewhere that doesn't have it.
