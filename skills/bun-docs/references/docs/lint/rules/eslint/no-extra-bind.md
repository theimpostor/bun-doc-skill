# no-extra-bind
Source: https://bun.com/docs/lint/rules/eslint/no-extra-bind

Disallow `.bind()` on functions that do not use `this`


`.bind(user)` sets `this` inside a function. If the function never reads `this`, that changes nothing. On an arrow function it has no effect either, because an arrow function takes `this` from where it's written. The call is usually left over from when the function did use `this`.

The rule only checks a function written right before the `.bind()`, and only a call with one argument.

`--fix` removes the `.bind()` call if its argument is a name, a literal or `this`. It leaves `.bind(getUser())` alone, because removing it would also remove the call to `getUser()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-extra-bind" = "error" # or "warn"
```


## Examples

Reported:

```js
const greet = function () {
  return "Hello";
}.bind(user);

const log = (() => {
  console.log(this.name);
}).bind(user);
```

A `this` inside a nested `function` belongs to that function, not to the outer one:

```js
const setup = function () {
  button.onclick = function () {
    this.disabled = true;
  };
}.bind(form);
```

Not reported:

```js
const greet = function () {
  return `Hello ${this.name}`;
}.bind(user);

const save = user.save.bind(user);
```

Extra arguments fill in parameters, which is useful even without `this`:

```js
const addFive = function (a, b) {
  return a + b;
}.bind(null, 5);
```
