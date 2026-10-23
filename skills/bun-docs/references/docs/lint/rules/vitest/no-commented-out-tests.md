# vitest/no-commented-out-tests
Source: https://bun.com/docs/lint/rules/vitest/no-commented-out-tests

Disallow tests that are inside a comment


A test inside a comment never runs, and the test output doesn't say so. It's easy to comment one out while debugging and forget about it.

To turn a test off for now, use `test.skip` or `test.todo`, which show up in the summary. If nobody needs the test, delete it.

A comment is reported if one of its lines starts with a call to `test`, `it` or `describe`. That includes `xtest`, `fit`, `test.only` and the like.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/no-commented-out-tests" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "vitest";

// test("rounds down", () => {
//   expect(Math.floor(1.9)).toBe(1);
// });
```

```ts
import { describe, expect, it } from "vitest";

describe("Math.floor", () => {
  /*
  it.only("rounds down", () => {
    expect(Math.floor(1.9)).toBe(1);
  });
  */
});
```

Not reported:

```ts
import { expect, test } from "vitest";

test.skip("rounds down", () => {
  expect(Math.floor(1.9)).toBe(1);
});

// test negative numbers too
test.todo("rounds negative numbers down");
```
