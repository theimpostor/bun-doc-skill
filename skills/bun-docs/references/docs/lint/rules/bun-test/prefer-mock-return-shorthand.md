# bun:test/prefer-mock-return-shorthand
Source: https://bun.com/docs/lint/rules/bun-test/prefer-mock-return-shorthand

Require `mockReturnValue()` for a mock that only returns a value


`mockImplementation(() => value)` wraps a value in a function that only returns it. `mockReturnValue(value)` does the same thing with less code. The same goes for `mockImplementationOnce()` and `mockReturnValueOnce()`.

`--fix` rewrites the call.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/prefer-mock-return-shorthand" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { mock } from "bun:test";

const getPort = mock().mockImplementation(() => 3000);

const getUser = mock().mockImplementationOnce(() => {
  return { name: "Ada" };
});
```

Not reported:

```ts
import { mock } from "bun:test";

const getPort = mock().mockReturnValue(3000);

const getUser = mock().mockReturnValueOnce({ name: "Ada" });
```

A function that takes parameters, is `async`, does more than return, or returns a `let` or `var` variable needs `mockImplementation()`, so it isn't reported:

```ts
import { mock } from "bun:test";

let visits = 0;

const double = mock().mockImplementation((n: number) => n * 2);
const load = mock().mockImplementation(async () => "done");
const countVisits = mock().mockImplementation(() => visits);
const nextVisit = mock().mockImplementation(() => {
  visits += 1;
  return "ok";
});
```

A function that calls something or creates an object with `new` isn't reported either. `mockReturnValue(createUser())` calls `createUser()` once, not each time the mock is called.

```ts
import { mock } from "bun:test";

const getUser = mock().mockImplementation(() => createUser());
const getDate = mock().mockImplementation(() => new Date());
```

## When not to use it

`mockReturnValue({ name: "Ada" })` returns the same object on every call. `mockImplementation(() => ({ name: "Ada" }))` returns a new one. If the code under test changes what the mock returns, keep the function and disable the rule on that line.
