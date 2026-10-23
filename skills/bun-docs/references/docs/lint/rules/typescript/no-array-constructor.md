# @typescript-eslint/no-array-constructor
Source: https://bun.com/docs/lint/rules/typescript/no-array-constructor

Disallow `Array()` and `new Array()` in favor of array literals


`new Array(1, 2)` makes `[1, 2]`, but `new Array(2)` makes an empty array of length 2. An array literal always holds what you write in it.

A call with exactly one argument is allowed, because that's how you make an array of a given length. A call with a type argument, such as `new Array<string>()`, is allowed too.

It's the TypeScript version of `no-array-constructor`.

`--fix` rewrites the call as an array literal.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-array-constructor" = "off" # or "error"
```


## Examples

Reported:

```ts
const sizes = new Array(10, 20, 30);
const names = Array();
```

Not reported:

```ts
const sizes = [10, 20, 30];
const names: string[] = [];

const slots = new Array(5);
const labels = new Array<string>();
```
