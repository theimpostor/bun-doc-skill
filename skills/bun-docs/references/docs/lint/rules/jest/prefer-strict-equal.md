# jest/prefer-strict-equal
Source: https://bun.com/docs/lint/rules/jest/prefer-strict-equal

Require `toStrictEqual()` instead of `toEqual()`


`toEqual()` skips properties that are `undefined`, treats a hole in an array like `undefined`, and doesn't compare the two objects' classes. So `expect({ name: "Ada", email: undefined }).toEqual({ name: "Ada" })` passes. `toStrictEqual()` checks all three, and that test fails.

`--fix-suggestions` renames the matcher. `--fix` doesn't, because a test that passes with `toEqual()` can fail with `toStrictEqual()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/prefer-strict-equal" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "@jest/globals";

test("creates a user", () => {
  expect(createUser("Ada")).toEqual({ name: "Ada" });
});
```

Not reported:

```ts
import { expect, test } from "@jest/globals";

test("creates a user", () => {
  expect(createUser("Ada")).toStrictEqual({ name: "Ada" });
});
```

## When not to use it

If your code builds objects with optional properties set to `undefined`, or you compare class instances with plain objects on purpose, `toEqual()` is the matcher you want.
