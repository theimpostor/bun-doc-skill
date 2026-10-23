# no-new-native-nonconstructor
Source: https://bun.com/docs/lint/rules/eslint/no-new-native-nonconstructor

Disallow `new Symbol()` and `new BigInt()`


`Symbol` and `BigInt` start with a capital letter but aren't constructors. `new Symbol("id")` and `new BigInt(10)` throw a `TypeError` when they run. Call them without `new`.

This rule is on by default in JavaScript files. It's off in TypeScript files, where TypeScript reports the same mistake.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-new-native-nonconstructor" = "off" # or "warn"
```


## Examples

Reported:

```js
const id = new Symbol("id");
```

```js
const total = new BigInt(9007199254740991);
```

Not reported:

```js
const id = Symbol("id");
const total = BigInt(9007199254740991);
```
