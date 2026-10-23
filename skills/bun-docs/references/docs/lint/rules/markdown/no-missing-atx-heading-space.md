# markdown/no-missing-atx-heading-space
Source: https://bun.com/docs/lint/rules/markdown/no-missing-atx-heading-space

Disallow headings without a space after the hash characters


`#Install` is not a heading. Without a space after the `#`, Markdown reads the line as a paragraph that starts with a hash.

`--fix` adds the space.


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
    rules: { "markdown/no-missing-atx-heading-space": "error" },
  },
];
```

It also works with `markdown/gfm`.


## Examples

Reported:


```md
#Install

##With Homebrew
```

Not reported:


```md
# Install

## With Homebrew

Issue \#12 and #12 in the middle of a line are fine.
```

## Options

| Option                | Default | What it does                                                        |
| --------------------- | ------- | ------------------------------------------------------------------- |
| `checkClosedHeadings` | `false` | Also require a space before the `#` characters that close a heading. |

Without that space the closing `#` characters are part of the heading's text:


```md
# Install#
```


```md
# Install #
```
