# @typescript-eslint/no-useless-constructor
Source: https://bun.com/docs/lint/rules/typescript/no-useless-constructor

Disallow constructors that do what the default constructor does


A class without a constructor gets one for free. In a base class it's empty, and in a subclass it passes all arguments to `super()`. Writing that out by hand adds lines that do nothing.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-useless-constructor" = "error" # or "warn"
```


## Examples

Reported:

```ts
class Store {
  constructor() {}
}

class HttpError extends Error {
  constructor(message: string) {
    super(message);
  }
}
```

Not reported:

```ts
class Store {}

class HttpError extends Error {}

class NotFoundError extends Error {
  constructor(path: string) {
    super(`${path} was not found`);
  }
}
```

An empty constructor is allowed if TypeScript gives it a job. A `private` or `protected` constructor limits who can create the class, a parameter property declares a field, and a decorator on a parameter runs code:

```ts
class Config {
  private constructor() {}
}

class User {
  constructor(public name: string) {}
}
```

A `public` constructor in a subclass is allowed too, because it can open up a `protected` one:

```ts
class Shape {
  protected constructor() {}
}

class Circle extends Shape {
  public constructor() {
    super();
  }
}
```
