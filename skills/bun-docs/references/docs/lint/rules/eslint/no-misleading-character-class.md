# no-misleading-character-class
Source: https://bun.com/docs/lint/rules/eslint/no-misleading-character-class

Disallow characters made of several code points inside a regular expression character class


A character class such as `[ab]` matches one code point from the list. Many things that look like one character are several: a letter followed by a combining accent, an emoji with a skin tone, a flag, a family joined with zero-width joiners. Without the `u` flag, most emoji count as two. Inside `[...]` each part becomes its own alternative, so `/^[👍]$/.test("👍")` is `false`.

The rule checks regular expression literals and the patterns given to `RegExp(...)` and `new RegExp(...)`.

`--fix-suggestions` adds the `u` flag when that's all that's missing and the pattern stays valid with it.

This rule is on by default.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-misleading-character-class" = "off" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-misleading-character-class" = ["error", {
  allowEscape = false,
}]
```


## Examples

Reported:

```js
const isThumbsUp = /^[👍]$/;
```

```js
const isFlag = /^[🇯🇵🇩🇪]$/u;
```

```js
const isFamily = new RegExp("[👨‍👩‍👦]", "u");
```

Not reported:

```js
const isThumbsUp = /^[👍]$/u;
```

```js
const isFlag = /^(?:🇯🇵|🇩🇪)$/u;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowEscape` | `false` | Don't report code points that are written as escapes, such as `\u0301`. The escape shows that you meant a separate code point. |

```js
const accents = /[A\u0301]/;
```

```js
const accents = /[A\u0301]/;
```
