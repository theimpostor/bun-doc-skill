# json/no-unnormalized-keys
Source: https://bun.com/docs/lint/rules/json/no-unnormalized-keys

Disallow JSON keys that are not normalized


Unicode has more than one way to write some characters. `é` is one character, U+00E9, or an `e` followed by the combining accent U+0301. The two look the same but are different keys, so a lookup with one doesn't find the other.

This rule reports keys that aren't in the chosen Unicode normalization form, which is NFC by default. `--fix` rewrites the key, unless it's written with escape sequences.


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
    rules: { "json/no-unnormalized-keys": "error" },
  },
];
```

It also works with `json/jsonc` and `json/json5`.


## Examples

The `é` in this key is an `e` and a combining accent. Reported:


```json
{
  "café": 1
}
```

Here it's the single character. Not reported:


```json
{
  "café": 1
}
```

## Options


**File:** `eslint.config.js`
```js
export default [
  {
    rules: { "json/no-unnormalized-keys": ["error", { form: "NFD" }] },
  },
];
```

| Option | Default | What it does                                                        |
| ------ | ------- | ------------------------------------------------------------------- |
| `form` | `"NFC"` | The form that keys have to be in: `"NFC"`, `"NFD"`, `"NFKC"`, or `"NFKD"`. |

With `NFD`, it's the single character that's reported:


```json
{
  "café": 1
}
```
