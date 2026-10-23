# @typescript-eslint/parameter-properties
Source: https://bun.com/docs/lint/rules/typescript/parameter-properties

Require or disallow parameter properties in class constructors


`constructor(private name: string) {}` declares a field and assigns it in one step. That's short, but the field isn't listed with the class's other fields, so it's easy to miss. It also isn't plain type syntax, so tools that only strip types, such as Node.js, reject it.

By default, every parameter property is reported. The `prefer` option flips the rule.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/parameter-properties" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/parameter-properties" = ["error", {
  prefer = "class-property", # "class-property" or "parameter-property"
  allow = [], # list of strings
}]
```


## Examples

Reported:

```ts
class User {
  constructor(private name: string) {}
}
```

Not reported:

```ts
class User {
  private name: string;

  constructor(name: string) {
    this.name = name;
  }
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `prefer` | `"class-property"` | `"parameter-property"` flips the rule and reports fields that could be parameter properties. |
| `allow` | `[]` | Modifiers to leave alone: `"readonly"`, `"private"`, `"protected"`, `"public"`, `"private readonly"`, `"protected readonly"`, `"public readonly"`. |

With `prefer: "parameter-property"`, a field is reported if it has no initial value, and the constructor starts by assigning it from a parameter with the same name and the same type:

```ts
class User {
  private name: string;

  constructor(name: string) {
    this.name = name;
  }
}
```

```ts
class User {
  constructor(private name: string) {}
}
```

An `allow` entry must match all the modifiers. `"readonly"` allows `readonly id` but not `private readonly id`:

```ts
class User {
  constructor(readonly id: number) {}
}
```

```ts
class User {
  constructor(private readonly id: number) {}
}
```
