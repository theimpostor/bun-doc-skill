# jsx-a11y/no-aria-hidden-on-focusable
Source: https://bun.com/docs/lint/rules/jsx-a11y/no-aria-hidden-on-focusable

Disallow `aria-hidden="true"` on elements that can receive focus


`aria-hidden="true"` hides an element from screen readers, but the Tab key still stops on it. The user lands on something that isn't announced and can't tell where focus went.

An element with a `tabIndex` is focusable if the value is 0 or more. Without a `tabIndex`, these are focusable: `<a>` and `<area>` with an `href`, and `<button>`, `<input>`, `<select>` and `<textarea>` that aren't `disabled`.

`--fix` removes the `aria-hidden` attribute.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/no-aria-hidden-on-focusable" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const close = <button aria-hidden="true" onClick={closeDialog} />;
const panel = <div aria-hidden="true" tabIndex={0} />;
```

Not reported:

```jsx
const close = <button aria-label="Close" onClick={closeDialog} />;
const icon = <svg aria-hidden="true" />;
const skipped = <button aria-hidden="true" tabIndex={-1} />;
```

Only `aria-hidden` and `aria-hidden="true"` are recognized. A value in braces isn't checked:

```jsx
const close = <button aria-hidden={true} onClick={closeDialog} />;
```
