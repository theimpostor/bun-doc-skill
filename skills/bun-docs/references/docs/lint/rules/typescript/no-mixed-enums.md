# @typescript-eslint/no-mixed-enums
Source: https://bun.com/docs/lint/rules/typescript/no-mixed-enums

Disallow enums that have both number and string members


An enum's number members and string members behave differently. A number member gets a reverse mapping, so `Status[0]` is `"Active"`, and `Object.values(Status)` holds the names along with the numbers. A string member gets neither. In an enum with both, code that loops over the members or looks one up by value has to handle two shapes.

The first member decides the kind. The first member of the other kind is reported. An enum that's declared in several parts counts as one.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-mixed-enums" = "error" # or "warn"
```


## Examples

Reported:

```ts
enum Status {
  Active,
  Archived = "archived",
}
```

Not reported:

```ts
enum Status {
  Active = "active",
  Archived = "archived",
}

enum Priority {
  Low,
  High,
}
```

The second part of this enum doesn't match the first:

```ts
enum Color {
  Red = "red",
}

enum Color {
  Green = 1,
}
```
