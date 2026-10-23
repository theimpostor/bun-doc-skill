# json/top-level-interop
Source: https://bun.com/docs/lint/rules/json/top-level-interop

Require the JSON top-level value to be an array or object


The first JSON specification, RFC 4627, only allowed an object or an array at the top of a document. Later ones allow any value, but some older parsers still reject a file that's just a string, a number, `true`, `false`, or `null`. Turn this rule on for files that such tools have to read.


## Configure

Off by default. It needs an ESLint config that says which files are in the language:


**File:** `eslint.config.js`
```js
import json from "@eslint/json";

export default [
  {
    files: ["**/*.json"],
    plugins: { json },
    language: "json/json",
    rules: { "json/top-level-interop": "error" },
  },
];
```

It also works with `json/jsonc` and `json/json5`.


## Examples

Reported:


```json
"app"
```


```json
42
```

Not reported:


```json
{ "name": "app" }
```


```json
[1, 2, 3]
```
