# vitest/prefer-expect-resolves
Source: https://bun.com/docs/lint/rules/vitest/prefer-expect-resolves

Require `await expect(promise).resolves` instead of `expect(await promise)`


In `expect(await promise)`, a rejected promise throws before `expect` is called, so the test fails with the raw error. With `.resolves`, `expect` gets the promise, and a rejection is reported as a failed assertion.

`--fix` rewrites the assertion.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-expect-resolves" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "vitest";

test("loads the user", async () => {
  expect(await loadUser(1)).toEqual({ id: 1, name: "Ada" });
});
```

Not reported:

```ts
import { expect, test } from "vitest";

test("loads the user", async () => {
  await expect(loadUser(1)).resolves.toEqual({ id: 1, name: "Ada" });
});

test("loads the user and checks two fields", async () => {
  const user = await loadUser(1);
  expect(user.id).toBe(1);
  expect(user.name).toBe("Ada");
});
```

## When not to use it

`await` accepts any value, but `.resolves` fails if it doesn't get a promise. If a function returns a plain value in some cases, keep `expect(await ...)` there.
