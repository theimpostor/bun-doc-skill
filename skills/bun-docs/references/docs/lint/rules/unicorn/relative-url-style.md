# unicorn/relative-url-style
Source: https://bun.com/docs/lint/rules/unicorn/relative-url-style

Enforce one style for relative URLs in `new URL()`: with or without `./`


`new URL("./logo.png", base)` and `new URL("logo.png", base)` give the same URL. Pick one style so you write and search for the same file the same way everywhere.

The rule only checks `new URL()` with two arguments, and only when adding or removing `./` doesn't change the result. `"../logo.png"` and `"/logo.png"` are never reported.

`--fix` removes or adds the `./` in a string. For a template literal, the editor offers the change as a suggestion.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/relative-url-style" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/relative-url-style" = ["error", "never"] # "never" or "always"
```


## Examples

Reported:

```js
const logo = new URL("./logo.png", import.meta.url);
const icon = new URL(`./${name}.svg`, import.meta.url);
```

Not reported:

```js
const logo = new URL("logo.png", import.meta.url);
const icon = new URL(`${name}.svg`, import.meta.url);
const shared = new URL("../shared/logo.png", import.meta.url);
```

## Options

| Option | What it does |
| --- | --- |
| `"never"` (default) | Report a string or a template literal that starts with `./`. |
| `"always"` | Report a string that doesn't start with `./`. Template literals aren't checked. |

```js
const logo = new URL("logo.png", import.meta.url);
```

```js
const logo = new URL("./logo.png", import.meta.url);
const icon = new URL(`${name}.svg`, import.meta.url);
const shared = new URL("../shared/logo.png", import.meta.url);
```
