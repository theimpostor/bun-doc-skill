# sort-vars
Source: https://bun.com/docs/lint/rules/eslint/sort-vars

Require the variables of one declaration to be sorted


When one `let`, `const` or `var` declares several variables, alphabetical order makes a name quick to find in the list.

Only names in the same declaration are compared. Destructuring patterns are skipped. Capital letters sort before lowercase letters unless you set `ignoreCase`.

`--fix` sorts the names if every initializer is a literal such as `0` or `"px"`. Other initializers can depend on the order they run in, so the declaration is left as is.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"sort-vars" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"sort-vars" = ["error", {
  ignoreCase = false,
}]
```


## Examples

Reported:

```js
let width, height, depth;
```

Not reported:

```js
let depth, height, width;

let total = 0;
let count = 0;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreCase` | `false` | Ignore case when comparing names. |

By default `Button` sorts before `app`, so this is reported:

```js
let app, Button, config;
```

With `ignoreCase` it isn't:

```js
let app, Button, config;
```
