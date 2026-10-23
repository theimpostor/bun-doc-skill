# no-new-wrappers
Source: https://bun.com/docs/lint/rules/eslint/no-new-wrappers

Disallow `new String()`, `new Number()` and `new Boolean()`


With `new`, `String`, `Number` and `Boolean` return an object that wraps the value, not the value itself. `typeof new String("a")` is `"object"`, `new Number(1) === 1` is `false`, and `new Boolean(false)` is truthy, so the `if` below always runs.

Without `new`, the same functions convert a value and return a plain string, number or boolean.

With an oxlint config, `--fix` rewrites `new String("Ada")` to `"Ada"` and `new Number(input)` to `Number(input)`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-new-wrappers" = "error" # or "warn"
```


## Examples

Reported:

```js
const enabled = new Boolean(false);

if (enabled) {
  start();
}
```

```js
const name = new String("Ada");
const port = new Number(input);
```

Not reported:

```js
const enabled = false;
const name = "Ada";
const port = Number(input);
```
