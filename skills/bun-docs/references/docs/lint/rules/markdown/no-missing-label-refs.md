# markdown/no-missing-label-refs
Source: https://bun.com/docs/lint/rules/markdown/no-missing-label-refs

Disallow missing label references


`[guide]` and `[the guide][guide]` are links only if the document defines `guide`. If the definition is missing or misspelled, there is no error: the brackets show up in the text.


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
    rules: { "markdown/no-missing-label-refs": "error" },
  },
];
```

It also works with `markdown/gfm`.


## Examples

Reported:


```md
Read the [guide] and [the reference][ref].
```

Not reported:


```md
Read the [guide] and [the reference][ref]. \[Not a link\]

[guide]: https://example.com/guide
[ref]: https://example.com/reference
```

## Options

| Option        | Default | What it does                                          |
| ------------- | ------- | ----------------------------------------------------- |
| `allowLabels` | `[]`    | Labels that don't need a definition.                  |

Use it for text in brackets that was never meant to be a link, like GitHub's alerts:


```md
> [!NOTE]
> Restart the server afterwards.
```
