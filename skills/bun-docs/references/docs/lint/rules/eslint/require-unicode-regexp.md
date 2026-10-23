# require-unicode-regexp
Source: https://bun.com/docs/lint/rules/eslint/require-unicode-regexp

Require the `u` or `v` flag on regular expressions


Without the `u` or `v` flag, a regular expression works on 16-bit units, not on characters. `/^.$/` doesn't match a single emoji such as `"\u{1F600}"`, because it takes two units. The flags also make the pattern strict, so a useless escape such as `\a` is a syntax error instead of being silently read as `a`.

The rule checks regular expression literals and calls to `RegExp`, with or without `new`. If the flags aren't a constant string, the call isn't reported.

The report comes with a suggestion that adds the flag, if the pattern is still valid with it.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"require-unicode-regexp" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"require-unicode-regexp" = ["error", {
  # requireFlag = <"u" or "v">,
}]
```


## Examples

Reported:

```js
const oneCharacter = /^.$/;
const word = new RegExp("\\w+", "g");
```

Not reported:

```js
const oneCharacter = /^.$/u;
const word = new RegExp("\\w+", "gu");
const emoji = /^\p{RGI_Emoji}$/v;

function search(pattern, flags) {
  return new RegExp(pattern, flags);
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `requireFlag` | not set | Set it to `"u"` or `"v"` to accept only that flag. When it isn't set, either flag is accepted. |

With `requireFlag` set to `"v"`, the `u` flag is reported:

```js
const oneCharacter = /^.$/u;
```
