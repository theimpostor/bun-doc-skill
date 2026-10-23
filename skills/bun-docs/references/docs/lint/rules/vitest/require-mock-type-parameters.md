# vitest/require-mock-type-parameters
Source: https://bun.com/docs/lint/rules/vitest/require-mock-type-parameters

Require a type parameter on `vi.fn()`


A plain `vi.fn()` is typed as a function that takes any arguments and returns `any`. TypeScript then accepts `mockReturnValue(42)` on a mock of a function that returns a string. With a type parameter, TypeScript checks what you pass to the mock and what it returns.

A mock with an implementation, such as `vi.fn(() => 1)`, is reported too, even though TypeScript infers its type. The rule only checks TypeScript files.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/require-mock-type-parameters" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/require-mock-type-parameters" = ["error", {
  checkImportFunctions = false,
}]
```


## Examples

Reported:

```ts
import { vi } from "vitest";

const findUser = vi.fn();
const log = vi.fn((message: string) => {});
```

Not reported:

```ts
import { vi } from "vitest";

type User = { name: string };

const findUser = vi.fn<(id: string) => Promise<User>>();
const log = vi.fn<(message: string) => void>((message) => {});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `checkImportFunctions` | `false` | Also require a type parameter on `vi.importActual()` and `vi.importMock()`. |

```ts
import { vi } from "vitest";

const mailer = await vi.importActual("./mailer");
```

```ts
import { vi } from "vitest";

const mailer = await vi.importActual<typeof import("./mailer")>("./mailer");
```
