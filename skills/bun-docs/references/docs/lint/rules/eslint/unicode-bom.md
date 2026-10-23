# unicode-bom
Source: https://bun.com/docs/lint/rules/eslint/unicode-bom

Require or disallow a Unicode byte order mark at the start of a file


A byte order mark (BOM) is the invisible character U+FEFF at the very start of a file. Some editors on Windows add it when they save as UTF-8. UTF-8 doesn't need it. It breaks a `#!` line, and it ends up in the middle of the output when files are joined.

By default the rule reports a file that starts with the mark.

`--fix` removes the mark, or adds it with `"always"`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicode-bom" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicode-bom" = ["error", "never"] # "always" or "never"
```


## Examples

The mark is invisible, so a file that has one looks the same here as a file that doesn't. None of these examples has one.

Not reported:

```js
const port = 3000;
```

Reported with `"always"`, because the mark is missing:

```js
const port = 3000;
```

## Options

| Option | What it does |
| --- | --- |
| `"never"` (default) | Report a file that starts with a byte order mark. |
| `"always"` | Report a file that doesn't start with one. |
