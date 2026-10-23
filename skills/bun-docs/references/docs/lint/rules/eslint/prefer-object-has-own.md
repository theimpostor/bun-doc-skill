# prefer-object-has-own
Source: https://bun.com/docs/lint/rules/eslint/prefer-object-has-own

Require `Object.hasOwn()` instead of `Object.prototype.hasOwnProperty.call()`


`Object.prototype.hasOwnProperty.call(user, key)` is the long way to ask if a property belongs to the object itself. It's written like that so it also works on objects without a prototype. `Object.hasOwn(user, key)` does the same thing and says what it means.

The shorter spellings `Object.hasOwnProperty.call()` and `{}.hasOwnProperty.call()` are reported too.

`--fix` replaces everything before the arguments with `Object.hasOwn`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"prefer-object-has-own" = "error" # or "warn"
```


## Examples

Reported:

```js
if (Object.prototype.hasOwnProperty.call(user, "email")) {
  send(user.email);
}

const isSet = {}.hasOwnProperty.call(settings, key);
const isCached = Object.hasOwnProperty.call(cache, id);
```

Not reported:

```js
if (Object.hasOwn(user, "email")) {
  send(user.email);
}

const isSet = Object.hasOwn(settings, key);
const isCached = Object.hasOwn(cache, id);
```

## When not to use it

`Object.hasOwn` is part of ES2022. Turn the rule off if your code runs on an older engine without a polyfill.
