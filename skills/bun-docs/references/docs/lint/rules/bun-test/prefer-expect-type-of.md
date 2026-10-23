# bun:test/prefer-expect-type-of
Source: https://bun.com/docs/lint/rules/bun-test/prefer-expect-type-of

Require `toBeTypeOf` instead of `expect(typeof value).toBe(...)`


`expect(typeof value).toBe("string")` only gives `expect` the name of the type. When the test fails, the output compares `"number"` with `"string"` and doesn't show the value. `expect(value).toBeTypeOf("string")` shows it.

The rule reports `typeof` inside `expect` with `toBe` or `toEqual`, with or without `.not`.

`--fix` rewrites the assertion.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/prefer-expect-type-of" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "bun:test";

test("the user has a name", () => {
  expect(typeof user.name).toBe("string");
  expect(typeof user.save).not.toEqual("undefined");
});
```

Not reported:

```ts
import { expect, test } from "bun:test";

test("the user has a name", () => {
  expect(user.name).toBeTypeOf("string");
  expect(user.save).not.toBeTypeOf("undefined");
});
```
