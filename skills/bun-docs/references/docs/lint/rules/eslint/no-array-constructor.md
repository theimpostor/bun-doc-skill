# no-array-constructor
Source: https://bun.com/docs/lint/rules/eslint/no-array-constructor

Disallow `Array` constructors in favor of array literals


`Array()` behaves differently depending on how many arguments it gets. `Array(10, 20)` is an array with two items, but `Array(10)` is an array with 10 empty slots. An array literal always holds what you wrote.

The rule reports `Array()` and `new Array()` with no argument or with more than one. A call with one argument is allowed, because that's how you make an array of a given length.

`--fix` rewrites the call to an array literal.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-array-constructor" = "error" # or "warn"
```


## Examples

Reported:

```js
const empty = new Array();
const sizes = Array(10, 20, 30);
```

Not reported:

```js
const empty = [];
const sizes = [10, 20, 30];
const slots = new Array(5);
```

In TypeScript, a call with a type argument isn't reported either:

```ts
const names = new Array<string>();
```
