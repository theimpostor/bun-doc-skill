# markdown/no-empty-images
Source: https://bun.com/docs/lint/rules/markdown/no-empty-images

Disallow empty images


An image without a URL, or with just `#`, shows up as a broken image. It's usually a placeholder that was never filled in.


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
    rules: { "markdown/no-empty-images": "error" },
  },
];
```

It also works with `markdown/gfm`.


## Examples

Reported:


```md
![The dashboard]()

![The dashboard](#)

![The dashboard](<>)
```

Not reported:


```md
![The dashboard](./dashboard.png)
```
