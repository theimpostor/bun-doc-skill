# markdown/no-reference-like-urls
Source: https://bun.com/docs/lint/rules/markdown/no-reference-like-urls

Disallow URLs that match defined reference identifiers


`[the guide](guide)` links to a file called `guide`. If the document also defines `[guide]: ..`, the author almost certainly meant `[the guide][guide]`, with square brackets.

`--fix` changes the parentheses to brackets, unless the link has a title, which a reference can't have.


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
    rules: { "markdown/no-reference-like-urls": "error" },
  },
];
```

It also works with `markdown/gfm`.


## Examples

Reported:


```md
Read [the guide](guide).

![The logo](logo)

[guide]: https://example.com/guide
[logo]: ./logo.png
```

Not reported:


```md
Read [the guide][guide] or [the other guide](./guide.md).

[guide]: https://example.com/guide
```
