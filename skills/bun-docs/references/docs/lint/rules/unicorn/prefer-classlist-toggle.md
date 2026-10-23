# unicorn/prefer-classlist-toggle
Source: https://bun.com/docs/lint/rules/unicorn/prefer-classlist-toggle

Require `classList.toggle()` instead of choosing between `add()` and `remove()`


`classList.toggle(name, force)` adds the class if `force` is true and removes it if `force` is false. That's one call instead of an `if` and an `else` that repeat the element and the class name.

`--fix` rewrites the code to `toggle()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-classlist-toggle" = "error" # or "warn"
```


## Examples

Reported:

```js
if (isOpen) {
  menu.classList.add("open");
} else {
  menu.classList.remove("open");
}

isOpen ? menu.classList.add("open") : menu.classList.remove("open");

menu.classList[isOpen ? "add" : "remove"]("open");
```

Not reported:

```js
menu.classList.toggle("open", isOpen);
```

`toggle(name, undefined)` flips the class instead of removing it. If the condition can be `undefined`, pass `Boolean(isOpen)`.

The two calls must use the same element and the same class:

```js
if (isOpen) {
  menu.classList.add("open");
} else {
  menu.classList.remove("closing");
}
```
