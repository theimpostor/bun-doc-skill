# @typescript-eslint/prefer-literal-enum-member
Source: https://bun.com/docs/lint/rules/typescript/prefer-literal-enum-member

Require enum values to be literals, not computed expressions


An enum value can be any expression, but then you need to evaluate it in your head to know what the member is. Names can also surprise you. Inside an enum, a name refers to another member before it refers to a variable outside, so `Max = limit` reads the member `limit` if there is one, not the `const limit` above the enum.

Strings, numbers, a `-` or `+` in front of a number, and template strings without `${}` are allowed. A member without a value isn't checked.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-literal-enum-member" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-literal-enum-member" = ["error", {
  allowBitwiseExpressions = false,
}]
```


## Examples

Reported:

```ts
const prefix = "app";

enum Key {
  Session = `${prefix}:session`,
  Length = "session".length,
  Total = 1 + 2,
}
```

Not reported:

```ts
enum Key {
  Session = "app:session",
  Length = 7,
  Offset = -1,
  Next,
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowBitwiseExpressions` | `false` | Allow `|`, `&`, `^`, `~`, `<<`, `>>`, and `>>>` on literals and on other members of the same enum. |

Flags are often written with shifts. Without the option, each of these is reported:

```ts
enum Permission {
  Read = 1 << 0,
  Write = 1 << 1,
  All = Read | Write,
}
```

With `allowBitwiseExpressions: true`, none of them are reported:

```ts
enum Permission {
  Read = 1 << 0,
  Write = 1 << 1,
  All = Read | Write,
}
```

A variable from outside the enum is still reported:

```ts
const base = 8;

enum Permission {
  Admin = base | 1,
}
```
