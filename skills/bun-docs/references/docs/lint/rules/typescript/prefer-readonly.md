# @typescript-eslint/prefer-readonly
Source: https://bun.com/docs/lint/rules/typescript/prefer-readonly

Require `readonly` on private members that are only assigned in the constructor


A private member can only be assigned inside its class. If nothing there assigns it after the constructor, it never changes. `readonly` says so, and then TypeScript rejects an assignment that someone adds later by mistake.

The rule checks `private` fields and `#private` fields, including static ones, and `private` constructor parameters. Assignments, `++`, `--`, `delete`, and destructuring into the member count as changes. Changing what's inside the value, such as `this.entries.set(...)`, doesn't.

`--fix` adds `readonly`. If the member starts as a literal and the constructor assigns to it, it also adds the type, as in `readonly #limit: number = 0`. Without it the type would be the literal `0`.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-readonly" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-readonly" = ["error", {
  onlyInlineLambdas = false,
}]
```


## Examples

Reported:

```ts
class Cache {
  private entries = new Map<string, string>();
  #limit = 100;
  private name: string;

  constructor(name: string, private ttl: number) {
    this.name = name;
  }

  set(key: string, value: string) {
    this.entries.set(key, value);
  }
}
```

Not reported:

```ts
class Cache {
  private readonly entries = new Map<string, string>();
  readonly #limit = 100;
  private hits = 0;
  size = 0;

  constructor(private readonly ttl: number) {}

  get(key: string) {
    this.hits++;
    return this.entries.get(key);
  }
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `onlyInlineLambdas` | `false` | Skip members that are declared with a value other than an arrow function. |

With `onlyInlineLambdas: true`, this isn't reported:

```ts
class Button {
  private label = "Save";
}
```

An arrow function is still reported, and so is a member that's declared without a value:

```ts
class Button {
  private id: string;
  private onClick = () => {
    console.log("clicked");
  };

  constructor(id: string) {
    this.id = id;
  }
}
```
