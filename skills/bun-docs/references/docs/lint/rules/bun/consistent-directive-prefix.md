# bun/consistent-directive-prefix
Source: https://bun.com/docs/lint/rules/bun/consistent-directive-prefix

Require comments that turn rules off to start with the same word, `eslint` or `oxlint`


`eslint-disable` and `oxlint-disable` comments both turn a rule off. If a project mixes them, a search for one spelling misses the other, and ESLint ignores the `oxlint` ones.

The default is `eslint`, which ESLint, oxlint, and `bun lint` all read. The rule checks `-disable`, `-disable-line`, `-disable-next-line`, and `-enable` comments.

`--fix` rewrites the prefix.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/consistent-directive-prefix" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/consistent-directive-prefix" = ["error", {
  prefix = "eslint", # "eslint" or "oxlint"
}]
```


## Examples

Reported:

```js
// oxlint-disable-next-line no-console
console.log(version);
```

Not reported:

```js
// eslint-disable-next-line no-console
console.log(version);
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `prefix` | `"eslint"` | The word to start with: `"eslint"` or `"oxlint"`. |

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/consistent-directive-prefix" = ["error", { prefix = "oxlint" }]
```

```js
/* eslint-disable no-console */
console.log(version);
/* eslint-enable no-console */
```

```js
/* oxlint-disable no-console */
console.log(version);
/* oxlint-enable no-console */
```
