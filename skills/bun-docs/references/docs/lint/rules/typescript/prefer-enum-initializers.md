# @typescript-eslint/prefer-enum-initializers
Source: https://bun.com/docs/lint/rules/typescript/prefer-enum-initializers

Require every enum member to have an explicit value


An enum member without a value gets a number from its position. The first is `0`, and each one after that is one more than the member before it. If you add a member in the middle or sort the list, every member after it gets a new number. Values that were saved in a database or sent to another service now mean something else.

Each member without a value is reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-enum-initializers" = "error" # or "warn"
```


## Examples

Reported:

```ts
enum Status {
  Draft,
  Published,
  Archived,
}
```

Not reported:

```ts
enum Status {
  Draft = 0,
  Published = 1,
  Archived = 2,
}

enum Role {
  Admin = "admin",
  Member = "member",
}
```

## When not to use it

If the values never leave the program and you only compare members with each other, the numbers don't matter.
