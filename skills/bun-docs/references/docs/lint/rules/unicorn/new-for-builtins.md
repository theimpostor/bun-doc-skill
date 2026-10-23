# unicorn/new-for-builtins
Source: https://bun.com/docs/lint/rules/unicorn/new-for-builtins

Require `new` for built-in classes and disallow it for `String`, `Number`, `Boolean`, `Symbol`, `BigInt`


Some built-ins work with and without `new`, some throw without it, and some do something else. `Array(3)` is the same as `new Array(3)`, `Map()` throws a `TypeError`, and `Date()` returns a string, not a `Date`. This rule requires `new` for built-in classes such as `Array`, `Object`, `Date`, `Error`, `RegExp`, `Promise`, `Map`, `Set` and the typed arrays.

The primitive wrappers are the other way around. `new Boolean(false)` is an object, so it's truthy, and `typeof new String("a")` is `"object"`. `new Symbol()` and `new BigInt(1)` throw. Call these without `new`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/new-for-builtins" = "error" # or "warn"
```


## Examples

Reported:

```js
const slots = Array(3);
const seen = Map();
const failure = Error("Not found");
const now = Date();
```

```js
const enabled = new Boolean(false);
const total = new Number(input.value);
```

Not reported:

```js
const slots = new Array(3);
const seen = new Map();
const failure = new Error("Not found");
const now = String(new Date());
```

```js
const enabled = Boolean(input.checked);
const total = Number(input.value);
```

`Object(value) === value` is a common test for "is this an object", so it's allowed:

```js
const isObject = value => Object(value) === value;
```

A name that your file declares or imports isn't the built-in, so it isn't checked:

```js
import { Map } from "immutable";

const seen = Map();
```
