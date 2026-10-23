# import/no-named-as-default
Source: https://bun.com/docs/lint/rules/import/no-named-as-default

Disallow naming a default import after a named export of the same module


`import Button from "./button"` gets the default export, whatever you call it. If `./button` also has a named export `Button`, you probably forgot the braces, and the code is using a different value than the name suggests.

The rule reads the imported module. It only reports if that module has both a default export and a named export with the name you chose.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-named-as-default" = "error" # or "warn"
```


## Examples

Reported:

**File:** `button.js`
```js
export const Button = props => render("button", props);

export default withTheme(Button);
```

```js
import Button from "./button";
```

Not reported:

**File:** `button.js`
```js
export const Button = props => render("button", props);

export default withTheme(Button);
```

```js
import ThemedButton, { Button } from "./button";
```

## When not to use it

Some modules export the same value both ways on purpose, so that `import Button` and `import { Button }` both work. The rule still reports the first form there.
