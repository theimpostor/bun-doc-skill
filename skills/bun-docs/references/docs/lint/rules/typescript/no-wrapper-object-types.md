# @typescript-eslint/no-wrapper-object-types
Source: https://bun.com/docs/lint/rules/typescript/no-wrapper-object-types

Disallow `String`, `Number`, `Boolean`, `BigInt`, `Symbol`, and `Object` as types


The type `Number` isn't the type of `1`. It describes the wrapper object that `new Number(1)` creates. A `number` fits into a `Number`, but not the other way around, so you can't pass a value typed `Number` to a function that takes a `number`. The same goes for `String`, `Boolean`, `BigInt`, and `Symbol`.

`Object` accepts almost every value, including strings and numbers. If you mean "not a primitive", use `object`.

`--fix` replaces the type with the lower-case one, except for `Object`. `const port: Object = 3000` type checks and `const port: object = 3000` doesn't, so only `--fix-dangerously` replaces that one.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-wrapper-object-types" = "off" # or "error"
```


## Examples

Reported:

```ts
function repeat(text: String, times: Number): String {
  return text.repeat(times.valueOf());
}
```

```ts
function keysOf(record: Object) {
  return Object.keys(record);
}
```

Not reported:

```ts
function repeat(text: string, times: number): string {
  return text.repeat(times);
}

function keysOf(record: object) {
  return Object.keys(record);
}
```

Only types are checked. Calling the functions with the same names is fine:

```ts
const port = Number("3000");
const label = String(port);
```
