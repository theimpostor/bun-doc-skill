# json/no-duplicate-keys
Source: https://bun.com/docs/lint/rules/json/no-duplicate-keys

Disallow duplicate keys in JSON objects


When an object has the same key twice, `JSON.parse` keeps the last value and silently drops the others. Someone reading the file may only notice the first one. It's usually left over from a merge or a copy and paste.

An escape sequence counts as the character it stands for. In JSON5, `a`, `'a'`, and `"a"` are the same key.


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
    rules: { "json/no-duplicate-keys": "error" },
  },
];
```

It also works with `json/jsonc` and `json/json5`.


## Examples

Reported:


```json
{
  "name": "app",
  "private": true,
  "name": "server"
}
```


```json5
{
  port: 3000,
  "port": 8080,
}
```

Not reported:


```json
{
  "name": "app",
  "author": { "name": "Ada" }
}
```
