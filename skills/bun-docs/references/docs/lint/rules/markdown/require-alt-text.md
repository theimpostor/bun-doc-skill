# markdown/require-alt-text
Source: https://bun.com/docs/lint/rules/markdown/require-alt-text

Require alternative text for images


The alternative text is what a screen reader reads out, and what everybody sees when the image doesn't load. Without it, those readers get nothing.

`<img>` elements in HTML are checked too. `alt=""` marks an image as decorative, so it's allowed, and so is `aria-hidden="true"`.


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
    rules: { "markdown/require-alt-text": "error" },
  },
];
```

It also works with `markdown/gfm`.


## Examples

Reported:


```md
![](./dashboard.png)

![][dashboard]

<img src="./dashboard.png">

[dashboard]: ./dashboard.png
```

Not reported:


```md
![The dashboard](./dashboard.png)

<img src="./dashboard.png" alt="The dashboard">

<img src="./divider.png" alt="">

<img src="./divider.png" aria-hidden="true">
```
