# unicorn/no-new-array
Source: https://bun.com/docs/lint/rules/unicorn/no-new-array

Disallow `new Array()` with a single argument


`new Array(value)` does two different things. If `value` is a number, you get an array of that length with nothing in it. If it's anything else, you get an array with `value` as its only item. You can't tell which one is meant without knowing the type of `value`.

The rule suggests both readings: `Array.from({length: value})` and `[value]`. It can't know which one you meant, so `--fix` leaves the code alone. `--fix-dangerously` applies the first one.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-new-array" = "error" # or "warn"
```


## Examples

Reported:

```js
const slots = new Array(10);
const list = new Array(input);
```

Not reported:

```js
const slots = Array.from({ length: 10 });
const list = [input];
```

Only the form with exactly one argument is ambiguous:

```js
const empty = new Array();
const pair = new Array(1, 2);
```
