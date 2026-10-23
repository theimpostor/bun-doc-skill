# import/no-dynamic-require
Source: https://bun.com/docs/lint/rules/import/no-dynamic-require

Disallow `require()` with an argument that is not a string literal


A bundler, a type checker and the other `import/*` rules find out what a file depends on by reading the string in `require("...")`. If the argument is a variable or is built at runtime, they can't know which file is loaded. The bundle misses it, and a wrong path only fails when the line runs.

A template literal without `${}` counts as a string.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-dynamic-require" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-dynamic-require" = ["error", {
  esmodule = false,
}]
```


## Examples

Reported:

```js
const plugin = require(name);
const locale = require(`./locales/${language}.json`);
```

Not reported:

```js
const plugin = require("./plugins/markdown");
const locale = require(`./locales/en.json`);
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `esmodule` | `false` | Also check `import()`. |

```js
const locale = await import(`./locales/${language}.js`);
```

```js
const locale = await import("./locales/en.js");
```

## When not to use it

A plugin loader has to load whatever its config names. Disable the rule on that line.
