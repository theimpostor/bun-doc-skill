# vitest/no-focused-tests
Source: https://bun.com/docs/lint/rules/vitest/no-focused-tests

Disallow `test.only` and `describe.only`


`.only` makes Vitest run that test and skip every other one in the file. It's useful while debugging. If you commit it by accident, it hides failures in the tests that no longer run.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/no-focused-tests" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { describe, expect, test } from "vitest";

test.only("adds", () => {
  expect(1 + 1).toBe(2);
});

describe.only("subtraction", () => {
  test("subtracts", () => {
    expect(2 - 1).toBe(1);
  });
});
```

Not reported:

```ts
import { describe, expect, test } from "vitest";

test("adds", () => {
  expect(1 + 1).toBe(2);
});

describe("subtraction", () => {
  test("subtracts", () => {
    expect(2 - 1).toBe(1);
  });
});
```
