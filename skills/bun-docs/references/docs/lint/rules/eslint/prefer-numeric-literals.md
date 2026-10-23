# prefer-numeric-literals
Source: https://bun.com/docs/lint/rules/eslint/prefer-numeric-literals

Require binary, octal and hexadecimal literals instead of `parseInt()` on a fixed string


`parseInt("ff8800", 16)` parses a string every time it runs, to get a number you already knew when you wrote it. Write the number itself: `0xff8800`. Binary literals start with `0b` and octal ones with `0o`.

The rule only reports `parseInt` and `Number.parseInt` with a fixed string and a radix of `2`, `8` or `16`.

`--fix` replaces the call with the literal when the string only has digits that are valid in that radix.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"prefer-numeric-literals" = "error" # or "warn"
```


## Examples

Reported:

```js
const mask = parseInt("1010", 2);
const mode = Number.parseInt("644", 8);
const color = parseInt("ff8800", 16);
```

Not reported:

```js
const mask = 0b1010;
const mode = 0o644;
const color = 0xff8800;

const value = parseInt(input, 16);
const count = parseInt("42", 10);
```
