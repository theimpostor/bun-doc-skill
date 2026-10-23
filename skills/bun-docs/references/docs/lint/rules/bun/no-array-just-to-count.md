# bun/no-array-just-to-count
Source: https://bun.com/docs/lint/rules/bun/no-array-just-to-count

Disallow `.split(separator).length` with a one-character separator


`text.split("\n").length` copies every line of `text` into a new array, reads the length, and throws the array away. For a large string, that's a lot of memory for one number. A loop that counts the separator allocates nothing.

Only a literal one-character separator is reported, not a variable or a regular expression.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-array-just-to-count" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-array-just-to-count" = ["error", {
  # countFunction = <string>,
}]
```


## Examples

Reported:

```js
const lineCount = source.split("\n").length;
```

Not reported:

```js
function count(text, separator) {
  let found = 0;
  for (let at = text.indexOf(separator); at !== -1; at = text.indexOf(separator, at + 1)) {
    found++;
  }
  return found;
}

const lineCount = count(source, "\n") + 1;
```

An array that's used for more than its length is fine, and so is a longer separator:

```js
const lines = source.split("\n");
console.log(lines.length, lines[0]);

const paragraphCount = source.split("\n\n").length;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `countFunction` | none | The name of a function that's called as `countFunction(string, separator)` and returns how often the separator occurs. |

Without `countFunction`, the rule only reports. With it, `--fix` rewrites `source.split("\n").length` to `count(source, "\n") + 1`, and `source.split("\n").length - 1` to `count(source, "\n")`. The fix only applies where a function with that name is in scope.

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-array-just-to-count" = ["error", { countFunction = "count" }]
```

```js
import { count } from "./strings.js";

const commas = row.split(",").length - 1;
```
