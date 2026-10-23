# markdown/no-reversed-media-syntax
Source: https://bun.com/docs/lint/rules/markdown/no-reversed-media-syntax

Disallow reversed link and image syntax


The syntax is `[text](url)`. The other way around, `(text)[url]`, isn't a link, and all of it shows up as text.

`--fix` swaps the brackets.


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
    rules: { "markdown/no-reversed-media-syntax": "error" },
  },
];
```

It also works with `markdown/gfm`.


## Examples

Reported:


```md
Read (the guide)[https://example.com/guide].

!(The logo)[./logo.png]
```

Not reported:


```md
Read [the guide](https://example.com/guide).

![The logo](./logo.png)

Call `f(a)[0]`.
```
