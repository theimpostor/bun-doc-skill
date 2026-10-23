# unicorn/prefer-set-has
Source: https://bun.com/docs/lint/rules/unicorn/prefer-set-has

Require `Set#has()` instead of `Array#includes()` for an array that is only searched


`includes()` walks the array from the start on every call. `has()` on a `Set` is a hash lookup, so it stays fast no matter how long the list gets.

The rule reports a `const` or `let` when all of this is true:

- Its value is a new array: an array literal, `Array.from()`, or the result of a method such as `map()` or `filter()`.
- You only ever call `.includes(value)` on it.
- The lookup can run more than once, because there are two or more calls or the only call is inside a loop or a function.
- It isn't exported.

`--fix` wraps the array in `new Set()` and renames the calls to `.has()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-set-has" = "error" # or "warn"
```


## Examples

Reported:

```js
const blocked = ["admin", "root", "system"];

function isAllowed(name) {
  return !blocked.includes(name);
}
```

Not reported:

```js
const blocked = new Set(["admin", "root", "system"]);

function isAllowed(name) {
  return !blocked.has(name);
}
```

An array that you search once, or that you also use as an array somewhere, can stay an array:

```js
const formats = ["png", "jpeg"];
const isImage = formats.includes(extension);

const sizes = [16, 32, 64];
for (const icon of icons) {
  if (sizes.includes(icon.size)) draw(icon);
}
console.log(sizes.length);
```
