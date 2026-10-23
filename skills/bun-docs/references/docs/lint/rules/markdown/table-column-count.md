# markdown/table-column-count
Source: https://bun.com/docs/lint/rules/markdown/table-column-count

Disallow data rows in a table from having more cells than the header row


The header row decides how many columns a table has. Extra cells are dropped when the table is rendered, so their content is silently lost.

Tables are part of GitHub Flavored Markdown, so the rule reports nothing in `markdown/commonmark`.


## Configure

Off by default. It needs an ESLint config that says which files are in the language:


**File:** `eslint.config.js`
```js
import markdown from "@eslint/markdown";

export default [
  {
    files: ["**/*.md"],
    plugins: { markdown },
    language: "markdown/gfm",
    rules: { "markdown/table-column-count": "error" },
  },
];
```

It also works with `markdown/commonmark`.


## Examples

Reported:


```md
| Name | Port |
| ---- | ---- |
| api  | 3000 | internal |
```

Not reported:


```md
| Name | Port |
| ---- | ---- |
| api  | 3000 |
| web  |
```

## Options

| Option              | Default | What it does                                               |
| ------------------- | ------- | ---------------------------------------------------------- |
| `checkMissingCells` | `false` | Also report a row with fewer cells than the header row.    |


```md
| Name | Port |
| ---- | ---- |
| web  |
```
