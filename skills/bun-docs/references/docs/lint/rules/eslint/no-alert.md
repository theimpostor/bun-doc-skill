# no-alert
Source: https://bun.com/docs/lint/rules/eslint/no-alert

Disallow `alert`, `confirm`, and `prompt`


`alert`, `confirm` and `prompt` stop all JavaScript on the page until the user answers, and you can't style the box they show. They're often left over from debugging.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-alert" = "error" # or "warn"
```


## Examples

Reported:

```js
alert("Saved");

if (window.confirm("Delete this file?")) {
  remove(file);
}
```

Not reported:

```js
showToast("Saved");

if (await dialog.confirm("Delete this file?")) {
  remove(file);
}
```

Your own function with one of these names is fine:

```js
import { alert } from "./ui/dialogs.js";

alert("Saved");
```

## When not to use it

In Bun, `alert`, `confirm` and `prompt` work in the terminal, which makes them a quick way to ask a question in a command-line script. Turn the rule off for those scripts.
