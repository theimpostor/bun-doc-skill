# vitest/padding-around-test-blocks
Source: https://bun.com/docs/lint/rules/vitest/padding-around-test-blocks

Require a blank line before each `test` and `it` call


Tests written right under each other, or right under setup code, are hard to tell apart when you scan a file. A blank line above each `test` or `it` call separates them.

The rule only checks the line above the call, not the line below. Comments directly above the call count as part of it, so the blank line goes above them. A test that comes first in a file or in a `describe` callback doesn't need a blank line.

`--fix` inserts the blank line.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/padding-around-test-blocks" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { describe, expect, test } from "vitest";

describe("cart", () => {
  const cart = createCart();
  test("starts empty", () => {
    expect(cart.items).toEqual([]);
  });
  test.skip("adds an item", () => {
    expect(cart.add("apple").items).toEqual(["apple"]);
  });
});
```

Not reported:

```ts
import { describe, expect, test } from "vitest";

describe("cart", () => {
  const cart = createCart();

  test("starts empty", () => {
    expect(cart.items).toEqual([]);
  });

  // Waits for the new storage layer.
  test.skip("adds an item", () => {
    expect(cart.add("apple").items).toEqual(["apple"]);
  });
});
```
