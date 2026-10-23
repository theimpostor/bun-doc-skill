# no-useless-constructor
Source: https://bun.com/docs/lint/rules/eslint/no-useless-constructor

Disallow constructors that do what the default constructor does


A class without a constructor gets one for free. In a base class it's empty, and in a subclass it passes all arguments to `super()`. Writing that out by hand adds lines that do nothing.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-useless-constructor" = "error" # or "warn"
```


## Examples

Reported:

```js
class Store {
  constructor() {}
}

class UserStore extends Store {
  constructor(name, options) {
    super(name, options);
  }
}
```

Not reported:

```js
class Store {}

class UserStore extends Store {}

class CachedStore extends Store {
  constructor(name) {
    super(name, { cache: true });
  }
}
```

In TypeScript, a constructor is allowed if it's `private` or `protected`, or if its parameters declare fields:

```ts
class Config {
  private constructor() {}
}

class User {
  constructor(public name: string) {}
}
```
