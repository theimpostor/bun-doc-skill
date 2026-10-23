# no-implied-eval
Source: https://bun.com/docs/lint/rules/eslint/no-implied-eval

Disallow passing a string of code to `setTimeout()`, `setInterval()` or `execScript()`


When the first argument of `setTimeout()` or `setInterval()` is a string, browsers compile and run it like `eval()` does. The code runs in the global scope, so it can't see your local variables, and anything a user typed that ends up in the string gets executed.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-implied-eval" = "error" # or "warn"
```


## Examples

Reported:

```js
setTimeout("refresh()", 1000);
setInterval("poll('" + url + "')", 5000);
window.setTimeout(`save(${id})`, 0);
```

The rule follows a constant that holds a string:

```js
const code = "refresh()";
setTimeout(code, 1000);
```

Not reported:

```js
setTimeout(refresh, 1000);
setInterval(() => poll(url), 5000);
window.setTimeout(() => save(id), 0);
```

Your own function with the same name isn't reported:

```js
import { setTimeout } from "./fake-timers.js";

setTimeout("tick", 1000);
```
