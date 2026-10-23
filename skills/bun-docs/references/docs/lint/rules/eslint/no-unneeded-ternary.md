# no-unneeded-ternary
Source: https://bun.com/docs/lint/rules/eslint/no-unneeded-ternary

Disallow `? :` where the condition alone says the same


`age >= 18 ? true : false` is a long way to write `age >= 18`.

`--fix` rewrites the expression: `a === b ? true : false` becomes `a === b`, `user ? true : false` becomes `!!user`, and `user ? false : true` becomes `!user`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-unneeded-ternary" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-unneeded-ternary" = ["error", {
  defaultAssignment = true,
}]
```


## Examples

Reported:

```js
const isAdult = age >= 18 ? true : false;
const isGuest = user ? false : true;
```

Not reported:

```js
const isAdult = age >= 18;
const isGuest = !user;
const label = isAdult ? "adult" : "minor";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `defaultAssignment` | `true` | Allow `x ? x : fallback`. Set it to `false` to report that too. |

```js
const title = name ? name : "Untitled";
```

```js
const title = name ? name : "Untitled";
```

With `false`, `--fix` rewrites it with `||`:

```js
const title = name || "Untitled";
```
