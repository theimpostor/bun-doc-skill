# unicorn/no-accessor-recursion
Source: https://bun.com/docs/lint/rules/unicorn/no-accessor-recursion

Disallow a getter or setter that uses its own property on `this`


A getter that reads `this.name` inside `get name()` calls itself. So does a setter that assigns to `this.name` inside `set name()`. The call never ends, and the program throws `RangeError: Maximum call stack size exceeded` the first time the property is used.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-accessor-recursion" = "error" # or "warn"
```


## Examples

Reported:

```js
class User {
  get name() {
    return this.name;
  }

  set name(value) {
    this.name = value.trim();
  }
}
```

Destructuring the property from `this` reads it too:

```js
const settings = {
  get theme() {
    const { theme } = this;
    return theme ?? "light";
  },
};
```

Not reported:

```js
class User {
  #name = "";

  get name() {
    return this.#name;
  }

  set name(value) {
    // Reading this.name in the setter is fine: it calls the getter.
    if (this.name !== value) {
      this.#name = value.trim();
    }
  }
}
```
