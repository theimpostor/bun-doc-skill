# no-empty-character-class
Source: https://bun.com/docs/lint/rules/eslint/no-empty-character-class

Disallow empty character classes `[]` in regular expressions


`[]` in a regular expression is a character class with no characters in it. It matches nothing, so `/^#[]{6}$/` never matches any string. Most often someone forgot to fill in the class, or meant the text `[]`, which is written `[]`.

`[^]`, which matches any character, is allowed. Only regular expression literals are checked, not strings passed to `new RegExp()`.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-empty-character-class" = "off" # or "error"
```


## Examples

Reported:

```js
const isHexColor = /^#[]{6}$/.test(color);
```

Not reported:

```js
const isHexColor = /^#[0-9a-f]{6}$/i.test(color);
```

```js
const anyCharacter = /[^]/;
const emptyArrayText = /\[]/;
const notChecked = new RegExp("[]");
```
