# react/forbid-foreign-prop-types
Source: https://bun.com/docs/lint/rules/react/forbid-foreign-prop-types

Disallow reading the `propTypes` of another component


Many production builds strip `propTypes` from components to save bytes. Code that reads `Button.propTypes` then gets `undefined`, so it works in development and breaks in production.

The rule reports every read of a `.propTypes` property, including destructuring it. Assigning to `propTypes` is fine. To share prop types between components, export them as a plain object.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/forbid-foreign-prop-types" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/forbid-foreign-prop-types" = ["error", {
  allowInPropTypes = false,
}]
```


## Examples

Reported:

```jsx
import Button from "./Button";

function IconButton(props) {
  return <Button {...props} />;
}
IconButton.propTypes = {
  ...Button.propTypes,
  icon: PropTypes.string,
};
```

```js
import Button from "./Button";

const { propTypes } = Button;
```

Not reported:

```jsx
import Button, { buttonPropTypes } from "./Button";

function IconButton(props) {
  return <Button {...props} />;
}
IconButton.propTypes = {
  ...buttonPropTypes,
  icon: PropTypes.string,
};
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowInPropTypes` | `false` | Allow the read inside an assignment to `propTypes` or a `propTypes` class field. That code is stripped from the build too. |

```jsx
import Button from "./Button";

function IconButton(props) {
  return <Button {...props} />;
}
IconButton.propTypes = {
  ...Button.propTypes,
  icon: PropTypes.string,
};
```

```js
import Button from "./Button";

const names = Object.keys(Button.propTypes);
```
