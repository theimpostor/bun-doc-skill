# markdown/no-invalid-label-refs
Source: https://bun.com/docs/lint/rules/markdown/no-invalid-label-refs

Disallow invalid label references


`[guide][]` is short for `[guide][guide]`. With whitespace between the last two brackets, it's no longer a reference, and the brackets show up in the text.


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
    rules: { "markdown/no-invalid-label-refs": "error" },
  },
];
```

It also works with `markdown/gfm`.


## Examples

Reported:


```md
Read the [guide][ ].

[guide]: https://example.com/guide
```

Not reported:


```md
Read the [guide][], the [guide], or [this][guide].

[guide]: https://example.com/guide
```
