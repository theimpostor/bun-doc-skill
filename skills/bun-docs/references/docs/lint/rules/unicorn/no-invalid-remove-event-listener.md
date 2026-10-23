# unicorn/no-invalid-remove-event-listener
Source: https://bun.com/docs/lint/rules/unicorn/no-invalid-remove-event-listener

Disallow passing a new function to `removeEventListener()`


`removeEventListener()` only removes the exact function you passed to `addEventListener()`. An inline function or the result of `.bind()` is a new function every time, so the call removes nothing and the old listener keeps running.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-invalid-remove-event-listener" = "error" # or "warn"
```


## Examples

Reported:

```js
button.addEventListener("click", () => save());
button.removeEventListener("click", () => save());

window.addEventListener("resize", this.layout.bind(this));
window.removeEventListener("resize", this.layout.bind(this));
```

Not reported:

```js
const onClick = () => save();
button.addEventListener("click", onClick);
button.removeEventListener("click", onClick);

const onResize = this.layout.bind(this);
window.addEventListener("resize", onResize);
window.removeEventListener("resize", onResize);
```
