# unicorn/prefer-code-point
Source: https://bun.com/docs/lint/rules/unicorn/prefer-code-point

Require `codePointAt()` and `String.fromCodePoint()` over `charCodeAt()` and `String.fromCharCode()`


`charCodeAt()` and `String.fromCharCode()` work in 16-bit units. Emoji and many other characters take two units. For those, `charCodeAt(0)` returns the number of half a character, and `String.fromCharCode(0x1F600)` drops the high bits and returns a different character. `codePointAt()` and `String.fromCodePoint()` handle the whole character.

`--fix-dangerously` renames the method. `--fix` doesn't, because the result changes for those characters.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-code-point" = "error" # or "warn"
```


## Examples

Reported:

```js
const code = text.charCodeAt(0);
const letter = String.fromCharCode(code);
```

Not reported:

```js
const code = text.codePointAt(0);
const letter = String.fromCodePoint(code);
```

## When not to use it

Code that works on UTF-16 units on purpose, such as an encoder or a hash that must match another implementation, needs `charCodeAt()`.
