# vitest/prefer-mock-return-shorthand
Source: https://bun.com/docs/lint/rules/vitest/prefer-mock-return-shorthand

Require `mockReturnValue()` for a mock that only returns a value


`mockImplementation(() => value)` wraps a value in a function that only returns it. `mockReturnValue(value)` does the same thing with less code. The same goes for `mockImplementationOnce()` and `mockReturnValueOnce()`.

`--fix` rewrites the call.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-mock-return-shorthand" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { vi } from "vitest";

const getPort = vi.fn().mockImplementation(() => 3000);

const getUser = vi.fn().mockImplementationOnce(() => {
  return { name: "Ada" };
});
```

Not reported:

```ts
import { vi } from "vitest";

const getPort = vi.fn().mockReturnValue(3000);

const getUser = vi.fn().mockReturnValueOnce({ name: "Ada" });
```

A function that takes parameters, is `async`, does more than return, or returns a `let` or `var` variable needs `mockImplementation()`, so it isn't reported:

```ts
import { vi } from "vitest";

let visits = 0;

const double = vi.fn().mockImplementation((n: number) => n * 2);
const load = vi.fn().mockImplementation(async () => "done");
const countVisits = vi.fn().mockImplementation(() => visits);
const nextVisit = vi.fn().mockImplementation(() => {
  visits += 1;
  return "ok";
});
```

A function that returns the result of a call or a `new` is reported, but `--fix` leaves it alone. `mockReturnValue(createUser())` calls `createUser()` once, not each time the mock is called.

```ts
import { vi } from "vitest";

const getUser = vi.fn().mockImplementation(() => createUser());
```

## When not to use it

`mockReturnValue({ name: "Ada" })` returns the same object on every call. `mockImplementation(() => ({ name: "Ada" }))` returns a new one. If the code under test changes what the mock returns, keep the function and disable the rule on that line.
