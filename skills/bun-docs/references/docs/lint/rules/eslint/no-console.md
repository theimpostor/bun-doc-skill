# no-console
Source: https://bun.com/docs/lint/rules/eslint/no-console

Disallow the use of `console`


`console.log()` calls added while debugging are easy to forget. In a web page they show up in every visitor's console, and in a library they write to the output of someone else's program.

Any property of the global `console` is reported, whether it's called or not. A local variable named `console` isn't.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-console" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-console" = ["error", {
  # allow = <list of strings>,
}]
```


## Examples

Reported:

```js
console.log("loaded", items.length);

items.forEach(console.warn);
```

Not reported:

```js
import { logger } from "./logger.js";

logger.info("loaded", items.length);
```

```js
function report(console) {
  console.log("done");
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allow` | none | The `console` methods to allow. |

**File:** `bunfig.toml`
```toml
[lint.rules]
no-console = ["error", { allow = ["warn", "error"] }]
```

```js
console.error("could not save", reason);
```

```js
console.log("saved");
```

## When not to use it

In a CLI tool or a script, `console` is how the program talks to its user. Turn the rule off there.
