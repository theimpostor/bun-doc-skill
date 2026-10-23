# unicorn/prefer-bigint-literals
Source: https://bun.com/docs/lint/rules/unicorn/prefer-bigint-literals

Require `BigInt` literals such as `123n` instead of `BigInt(123)`


`BigInt(123)` and `BigInt("123")` call a function to make a value you can write as `123n`. With a large number, the call is also wrong. `BigInt(9007199254740993)` rounds the number before `BigInt` sees it, so you get `9007199254740992n`.

`--fix` replaces the call with the literal.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-bigint-literals" = "error" # or "warn"
```


## Examples

Reported:

```js
const zero = BigInt(0);
const limit = BigInt("9007199254740993");
const mask = BigInt(0xFF);
```

Not reported:

```js
const zero = 0n;
const limit = 9007199254740993n;
const mask = 0xFFn;
```

A value that's only known at runtime still needs the call:

```js
const id = BigInt(row.id);
const size = BigInt(`${count}000`);
```
