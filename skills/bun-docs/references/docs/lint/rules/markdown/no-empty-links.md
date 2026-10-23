# markdown/no-empty-links
Source: https://bun.com/docs/lint/rules/markdown/no-empty-links

Disallow empty links


A link without a URL, or with just `#`, looks like a link and leads nowhere. It's usually a placeholder that was never filled in.


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
    rules: { "markdown/no-empty-links": "error" },
  },
];
```

It also works with `markdown/gfm`.


## Examples

Reported:


```md
Read the [guide]().

Read the [guide](#).

Read the [guide](<>).
```

Not reported:


```md
Read the [guide](https://example.com/guide) or jump to [usage](#usage).
```
