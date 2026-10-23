# @typescript-eslint/no-inferrable-types
Source: https://bun.com/docs/lint/rules/typescript/no-inferrable-types

Disallow type annotations that repeat what the initial value already says


In `const retries: number = 3`, TypeScript already infers that `retries` is a number. The annotation only repeats it.

The rule looks at variables, parameters with a default value and class properties. It reports `bigint`, `boolean`, `number`, `null`, `string`, `symbol`, `undefined` and `RegExp` when the value is a literal of that type or a call such as `Number(input)` or `Symbol("id")`.

A `readonly` or optional property isn't reported. Without its annotation, `readonly limit = 10` has the type `10`, not `number`.

`--fix` removes the annotation.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-inferrable-types" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-inferrable-types" = ["error", {
  ignoreParameters = false,
  ignoreProperties = false,
}]
```


## Examples

Reported:

```ts
const retries: number = 3;
const pattern: RegExp = /\d+/;

function greet(name: string = "world") {}

class Cart {
  isOpen: boolean = false;
}
```

Not reported:

```ts
const retries = 3;
const pattern = /\d+/;

function greet(name = "world") {}

class Cart {
  isOpen = false;
  readonly limit: number = 10;
}
```

An annotation that's wider than the value isn't reported:

```ts
let selected: string | null = null;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreParameters` | `false` | Don't report parameters. |
| `ignoreProperties` | `false` | Don't report class properties. |

```ts
function greet(name: string = "world") {}
```

```ts
class Cart {
  isOpen: boolean = false;
}
```
