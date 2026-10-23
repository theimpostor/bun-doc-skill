# @typescript-eslint/no-import-type-side-effects
Source: https://bun.com/docs/lint/rules/typescript/no-import-type-side-effects

Require `import type` when every name in an import is marked `type`


With `verbatimModuleSyntax` in `tsconfig.json`, TypeScript removes the names marked `type` from an import and keeps the rest of the statement. `import { type User } from "./models"` becomes `import {} from "./models"`, so the module is still loaded and run. `import type { User } from "./models"` is removed completely.

`--fix` moves `type` in front of the braces.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-import-type-side-effects" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { type User, type Role } from "./models";

export function describe(user: User, role: Role) {}
```

Not reported:

```ts
import type { User, Role } from "./models";

export function describe(user: User, role: Role) {}
```

An import that also brings in a value must stay at run time, so it's fine:

```ts
import { type User, loadUser } from "./models";

export const user: User = loadUser();
```

## When not to use it

Without `verbatimModuleSyntax`, TypeScript drops an import that's only used for types, so both forms compile to the same code.
