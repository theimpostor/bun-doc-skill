# @typescript-eslint/require-array-sort-compare
Source: https://bun.com/docs/lint/rules/typescript/require-array-sort-compare

Require a compare function in calls to `sort` and `toSorted` on arrays


Without a compare function, `sort()` and `toSorted()` turn every element into a string and compare the strings. `[1, 2, 10].sort()` gives `[1, 10, 2]`.

Arrays of strings are allowed by default, because sorting them as strings is usually what you want.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/require-array-sort-compare" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/require-array-sort-compare" = ["error", {
  ignoreStringArrays = true,
}]
```


## Examples

Reported:

```ts
const prices = [5, 100, 20];

prices.sort(); // [100, 20, 5]
const sorted = prices.toSorted();
```

Not reported:

```ts
const prices = [5, 100, 20];
prices.sort((a, b) => a - b); // [5, 20, 100]

const names = ["Zoe", "Adam"];
names.sort();
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreStringArrays` | `true` | Allow `sort()` with no argument on an array where every element is a string. |

```ts
const names = ["Zoe", "Adam"];
names.sort();
```
