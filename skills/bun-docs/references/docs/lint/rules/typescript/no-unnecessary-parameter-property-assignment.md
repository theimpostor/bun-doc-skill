# @typescript-eslint/no-unnecessary-parameter-property-assignment
Source: https://bun.com/docs/lint/rules/typescript/no-unnecessary-parameter-property-assignment

Disallow assigning a constructor parameter property to itself


A constructor parameter with `public`, `private`, `protected` or `readonly` in front of it declares a property and assigns the argument to it. Writing `this.name = name` in the body does the same work a second time.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unnecessary-parameter-property-assignment" = "error"
```


## Examples

Reported:

```ts
class User {
  constructor(public name: string) {
    this.name = name;
  }
}
```

Not reported:

```ts
class User {
  constructor(public name: string) {}
}
```

An assignment that stores a different value is fine, and so is a copy made after the parameter was changed:

```ts
class User {
  constructor(
    public name: string,
    private email: string,
  ) {
    this.name = name.trim();

    email = email.toLowerCase();
    this.email = email;
  }
}
```
