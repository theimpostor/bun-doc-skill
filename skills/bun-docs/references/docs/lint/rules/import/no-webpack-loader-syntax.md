# import/no-webpack-loader-syntax
Source: https://bun.com/docs/lint/rules/import/no-webpack-loader-syntax

Disallow webpack loader syntax such as `style-loader!./app.css` in imports


webpack lets you put loader names in front of a path, separated by `!`. Bun, Node.js and most other bundlers can't resolve a path like that, so the file only works with webpack. It also scatters your build setup across your source files.

The rule reports any `import`, `export .. from`, `import()` or `require()` with a `!` in its path.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-webpack-loader-syntax" = "error" # or "warn"
```


## Examples

Reported:

```js
import styles from "style-loader!css-loader!./app.css";
const notes = require("raw-loader!./notes.txt");
```

Not reported:

```js
import styles from "./app.css";
const notes = require("./notes.txt");
```

Configure the loaders in `webpack.config.js` instead.
