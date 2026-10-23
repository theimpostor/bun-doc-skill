# for-direction
Source: https://bun.com/docs/lint/rules/eslint/for-direction

Require the update clause of a `for` loop to move the counter toward the end of the loop


A loop that tests `i < 10` and then runs `i--` moves away from 10, so the test stays true and the loop never ends. It's almost always a typo, like `--` for `++` or `<` for `>`.

The rule looks at `++`, `--`, `+=` and `-=` on the counter. If it can't tell whether the step is positive or negative, it reports nothing.

This rule is on by default.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"for-direction" = "off" # or "warn"
```


## Examples

Reported:

```js
for (let i = 0; i < items.length; i--) {
  render(items[i]);
}
```

```js
for (let i = items.length - 1; i >= 0; i += 1) {
  render(items[i]);
}
```

Not reported:

```js
for (let i = 0; i < items.length; i++) {
  render(items[i]);
}

for (let i = items.length - 1; i >= 0; i -= 1) {
  render(items[i]);
}
```

The rule can't know the sign of `step` here, so it leaves the loop alone:

```js
function walk(items, step) {
  for (let i = 0; i < items.length; i += step) {
    render(items[i]);
  }
}
```
