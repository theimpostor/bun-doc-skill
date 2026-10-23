# @typescript-eslint/no-duplicate-enum-values
Source: https://bun.com/docs/lint/rules/typescript/no-duplicate-enum-values

Disallow two enum members with the same value


You can't tell two enum members with the same value apart at runtime. `Status.Active === Status.Enabled` is `true`, a `switch` only ever reaches the first `case`, and for numbers the reverse lookup `Status[1]` gives only the last name.

The rule only compares values written as a number, a string or a template without `${}`, with or without a `+` or `-` sign. It skips members without a value and computed values.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-duplicate-enum-values" = "off" # or "error"
```


## Examples

Reported:

```ts
enum Status {
  Active = 1,
  Enabled = 1,
}

enum Color {
  Red = "red",
  Crimson = "red",
}
```

Not reported:

```ts
enum Status {
  Active = 1,
  Disabled = 2,
}

enum Color {
  Red = "red",
  Crimson = "crimson",
}
```

A value that TypeScript fills in isn't compared. Here `Third` is `1` as well:

```ts
enum Rank {
  First = 1,
  Second = 0,
  Third,
}
```
