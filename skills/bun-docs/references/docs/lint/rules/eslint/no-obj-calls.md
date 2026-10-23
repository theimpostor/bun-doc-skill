# no-obj-calls
Source: https://bun.com/docs/lint/rules/eslint/no-obj-calls

Disallow calling `Math`, `JSON`, `Reflect`, `Atomics`, `Intl` and `Temporal` as functions


`Math`, `JSON`, `Reflect`, `Atomics`, `Intl` and `Temporal` start with a capital letter, but they're plain objects that hold functions. `Math()` and `new JSON()` throw a `TypeError` when they run.

The rule follows the object through variables and through `globalThis`.

This rule is on by default in JavaScript files. It's off in TypeScript files, where TypeScript reports the same mistake.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-obj-calls" = "off" # or "warn"
```


## Examples

Reported:

```js
const random = Math();
```

```js
const parser = new JSON();
```

```js
const format = Intl;
const text = format("en-US");

const now = globalThis.Reflect();
```

Not reported:

```js
const random = Math.random();
const data = JSON.parse(body);
const text = new Intl.NumberFormat("en-US").format(total);
```
