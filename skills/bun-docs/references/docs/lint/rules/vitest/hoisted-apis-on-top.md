# vitest/hoisted-apis-on-top
Source: https://bun.com/docs/lint/rules/vitest/hoisted-apis-on-top

Require `vi.mock`, `vi.unmock` and `vi.hoisted` at the top level of the file


Vitest moves `vi.mock()`, `vi.unmock()` and `vi.hoisted()` to the top of the file before it runs the file. A call written inside an `if`, a hook or a test looks like it runs there, but it runs first, every time, and applies to the whole file.

Write these calls at the top level, where they run anyway. If you want a mock that starts where it's written, use `vi.doMock()`.

The report comes with a suggestion that moves the call to just below the imports. For `vi.mock` there's a second one that replaces it with `vi.doMock`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/hoisted-apis-on-top" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { beforeEach, vi } from "vitest";

beforeEach(() => {
  vi.mock("./database");
});
```

Not reported:

```ts
import { beforeEach, vi } from "vitest";

vi.mock("./database");

beforeEach(() => {
  vi.doMock("./clock");
});
```

You can await the result of `vi.hoisted()` and store it in a variable:

```ts
import { vi } from "vitest";

const mocks = vi.hoisted(() => ({ send: vi.fn() }));
const config = await vi.hoisted(async () => ({ retries: 3 }));
```

An exported variable is reported:

```ts
import { vi } from "vitest";

export const mocks = vi.hoisted(() => ({ send: vi.fn() }));
```
