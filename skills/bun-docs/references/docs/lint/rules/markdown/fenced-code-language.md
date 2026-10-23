# markdown/fenced-code-language
Source: https://bun.com/docs/lint/rules/markdown/fenced-code-language

Require languages for fenced code blocks


A fenced code block without a language gets no syntax highlighting, and tools that extract code blocks by language skip it. Indented code blocks can't have a language, so they're ignored.


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
    rules: { "markdown/fenced-code-language": "error" },
  },
];
```

It also works with `markdown/gfm`.


## Examples

Reported:


````md
```
const port = 3000;
```
```

Not reported:


````md
```
const port = 3000;
```
```

## Options

| Option     | Default | What it does                                                                     |
| ---------- | ------- | -------------------------------------------------------------------------------- |
| `required` | `[]`    | The only languages that are allowed. An empty list allows any language.          |


````md
```
const port = 3000;
```
```


````md
```
const port = 3000;
```
```
