# unicorn/prefer-export-from
Source: https://bun.com/docs/lint/rules/unicorn/prefer-export-from

Require `export ... from` to re-export instead of an import and a separate export


An `import` followed by an `export` of the same name takes two statements, often far apart, to say one thing. `export { parse } from "./parser.js"` says it in one place and doesn't add a name to the file's scope.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-export-from" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-export-from" = ["error", {
  checkUsedVariables = true,
}]
```


## Examples

Reported:

```js
import { parse } from "./parser.js";

export { parse };
```

```js
import Button from "./button.js";
import * as icons from "./icons.js";

export default Button;
export { icons };
```

Not reported:

```js
export { parse } from "./parser.js";
export { default } from "./button.js";
export * as icons from "./icons.js";
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `checkUsedVariables` | `true` | Also report an import that the file uses for something other than exporting it. |

By default, this is reported even though the file needs the import for `parse("")`:

```js
import { parse } from "./parser.js";

export { parse };
export const empty = parse("");
```

To fix it, keep the import and re-export from the module as well:

```js
import { parse } from "./parser.js";

export { parse } from "./parser.js";
export const empty = parse("");
```

With `false`, the rule skips an import statement as soon as the file uses one of its names:

```js
import { parse } from "./parser.js";

export { parse };
export const empty = parse("");
```
