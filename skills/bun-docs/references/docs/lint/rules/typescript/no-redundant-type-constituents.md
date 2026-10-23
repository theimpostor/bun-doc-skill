# @typescript-eslint/no-redundant-type-constituents
Source: https://bun.com/docs/lint/rules/typescript/no-redundant-type-constituents

Disallow members of unions and intersections that change nothing or swallow the rest


Some members of a union or an intersection don't do what they look like they do. `"draft" | string` is `string`, so the editor no longer suggests `"draft"`, and a typo in it is accepted. `User | any` is `any`, so nothing about it is checked.

| Written | What TypeScript makes of it |
| --- | --- |
| `T | any`, `T & any` | `any` |
| `T | unknown` | `unknown` |
| `T | never`, `T & unknown` | `T` |
| `T & never` | `never` |
| `"draft" | string`, `0 | number`, `true | boolean` | The wider type. |
| `"draft" & string`, `0 & number` | The literal. |

`T | never` is allowed as the return type of a function.

`bun lint --type-aware` turns this rule on in TypeScript files.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-redundant-type-constituents" = "error" # or "warn"
```


## Examples

Reported:

```ts
type Status = "draft" | "published" | string;

type Payload = { id: number } | any;

type Result = string | never;

function send(body: unknown | string) {}
```

Not reported:

```ts
type Status = "draft" | "published";

type Payload = { id: number } | string;

type Result = string;

function send(body: unknown) {}

function load(id: number): string | never {
  throw new Error(`No item ${id}`);
}
```

The rule looks through type aliases:

```ts
type Id = number;

type Key = Id | 0;
```

A type that can't be resolved acts as `any`, so it's reported too. Here `./missing` doesn't exist:

```ts
import type { User } from "./missing";

type Owner = User | string;
```
