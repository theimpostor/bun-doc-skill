# markdown/no-multiple-h1
Source: https://bun.com/docs/lint/rules/markdown/no-multiple-h1

Disallow multiple H1 headings in the same document


The level 1 heading is the title of the document. Search engines, screen readers and documentation tools expect one. A second one is usually a section that should be level 2.

`<h1>` elements in HTML count, and so does a title in the front matter.


## Configure

Off by default. It needs an ESLint config that says which files are in the language:


**File:** `eslint.config.js`
```js
import markdown from "@eslint/markdown";

export default [
  {
    files: ["**/*.md"],
    plugins: { markdown },
    language: "markdown/commonmark",
    rules: { "markdown/no-multiple-h1": "error" },
  },
];
```

It also works with `markdown/gfm`.


## Examples

Reported:


```md
# Bun

# Install
```


```md
# Bun

<h1>Install</h1>
```

Not reported:


```md
# Bun

## Install
```

## Options

| Option             | Default                                                | What it does                                                                                                                         |
| ------------------ | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `frontmatterTitle` | a pattern that matches `title:`, `title =`, `"title":` | A regular expression. If a line of the front matter matches it, the front matter counts as a level 1 heading. `""` turns that off. |

Front matter is only parsed if `languageOptions.frontmatter` is set to the format that the files use.


```md
---
title: Bun
---

# Install
```


```md
---
title: Bun
---

# Install
```
