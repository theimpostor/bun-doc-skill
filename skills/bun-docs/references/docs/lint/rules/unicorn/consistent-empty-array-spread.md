# unicorn/consistent-empty-array-spread
Source: https://bun.com/docs/lint/rules/unicorn/consistent-empty-array-spread

Require both branches of a spread ternary in an array to have the same type


Spreading `[]` and spreading `""` both add nothing to an array, so either works as the "nothing" branch of `...(condition ? items : fallback)`. But when one branch is an array and the other is a string, the reader needs to stop and work out that the mismatch is harmless.

The rule reports an array followed by `""`, and a string followed by `[]`. It only looks at the fallback after the `:`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/consistent-empty-array-spread" = "error" # or "warn"
```


## Examples

Reported:

```js
const args = ["build", ...(watch ? ["--watch", "--hot"] : "")];
```

```js
const letters = ["a", ...(more ? "bc" : [])];
```

Not reported:

```js
const args = ["build", ...(watch ? ["--watch", "--hot"] : [])];

const letters = ["a", ...(more ? "bc" : "")];
```
