# @typescript-eslint/no-unnecessary-qualifier
Source: https://bun.com/docs/lint/rules/typescript/no-unnecessary-qualifier

Disallow naming the enclosing namespace or enum where the short name works


Inside a `namespace` or an `enum`, its own members are in scope. Writing `Shapes.Circle` inside `Shapes` means the same as `Circle`.

`--fix` removes the qualifier.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unnecessary-qualifier" = "error" # or "warn"
```


## Examples

Reported:

```ts
namespace Shapes {
  export interface Circle {
    radius: number;
  }
  export const unit: Shapes.Circle = { radius: 1 };
}

enum Level {
  Low = 1,
  Default = Level.Low,
}
```

Not reported:

```ts
namespace Shapes {
  export interface Circle {
    radius: number;
  }
  export const unit: Circle = { radius: 1 };
}

enum Level {
  Low = 1,
  Default = Low,
}

const circle: Shapes.Circle = Shapes.unit;
```

Here `limit` alone would be the local constant, so `Config.limit` stays:

```ts
namespace Config {
  export const limit = 10;

  export function clamp(value: number) {
    const limit = value * 2;
    return Math.min(limit, Config.limit);
  }
}
```
