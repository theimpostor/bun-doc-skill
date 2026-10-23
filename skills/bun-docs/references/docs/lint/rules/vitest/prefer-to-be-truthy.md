# vitest/prefer-to-be-truthy
Source: https://bun.com/docs/lint/rules/vitest/prefer-to-be-truthy

Require `toBeTruthy()` instead of `toBe(true)`


`toBe(true)` only passes for `true` itself. If the code returns `1`, a string, or an object instead, the test fails, even though `if (value)` treats them all the same. `toBeTruthy()` passes for any truthy value.

`toEqual(true)` and `toStrictEqual(true)` are reported too, with or without `.not`.

`--fix-suggestions` replaces the matcher with `toBeTruthy()`. `--fix` doesn't, because the new matcher accepts more values.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-to-be-truthy" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "vitest";

test("an admin can delete posts", () => {
  const user = createUser({ role: "admin" });
  expect(user.canDelete).toBe(true);
  expect(user.isBanned).not.toEqual(true);
});
```

Not reported:

```ts
import { expect, test } from "vitest";

test("an admin can delete posts", () => {
  const user = createUser({ role: "admin" });
  expect(user.canDelete).toBeTruthy();
  expect(user.isBanned).not.toBeTruthy();
});
```

## When not to use it

`toBe(true)` is the stricter check. If returning `1` or a string instead of `true` would be a bug, keep it. `vitest/prefer-strict-boolean-matchers` is the opposite rule.
