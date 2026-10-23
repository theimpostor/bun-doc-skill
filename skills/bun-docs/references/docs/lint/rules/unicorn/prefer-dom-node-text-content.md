# unicorn/prefer-dom-node-text-content
Source: https://bun.com/docs/lint/rules/unicorn/prefer-dom-node-text-content

Require `.textContent` instead of `.innerText`


`innerText` returns the text as it's rendered. The browser needs to compute styles and layout to answer, and it leaves out text hidden by CSS. `textContent` returns the text of every node under the element without any of that work.

The rule doesn't know types. It reports `.innerText` on any object, and `innerText` in destructuring.

`--fix` doesn't change the code, because the two give different text: `innerText` leaves out what CSS hides and turns `<br>` into a line break. `--fix-dangerously` renames the property access. You need to fix destructuring yourself.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-dom-node-text-content" = "error" # or "warn"
```


## Examples

Reported:

```js
const title = heading.innerText;
status.innerText = "Saved";
const { innerText } = heading;
```

Not reported:

```js
const title = heading.textContent;
status.textContent = "Saved";
const { textContent } = heading;
```

## When not to use it

If you want what the user sees, with hidden elements left out and line breaks where `<br>` and blocks are, `innerText` is the right property.
