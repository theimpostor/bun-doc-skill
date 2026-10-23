# vitest/prefer-hooks-on-top
Source: https://bun.com/docs/lint/rules/vitest/prefer-hooks-on-top

Require hooks to come before the tests in their block


A hook applies to every test in its block, wherever it's written. A `beforeEach` below a test still runs before that test, but someone reading from the top hasn't seen it yet.

Each `describe` block is checked on its own.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-hooks-on-top" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { beforeEach, expect, test } from "vitest";

test("starts empty", () => {
  expect(cart.items).toHaveLength(0);
});

beforeEach(() => {
  cart.clear();
});
```

Not reported:

```ts
import { beforeEach, expect, test } from "vitest";

beforeEach(() => {
  cart.clear();
});

test("starts empty", () => {
  expect(cart.items).toHaveLength(0);
});
```

A hook at the top of a `describe` block is fine, even if there's a test before the block:

```ts
import { beforeEach, describe, expect, test } from "vitest";

test("loads the shop", () => {
  expect(shop.ready).toBe(true);
});

describe("cart", () => {
  beforeEach(() => {
    cart.clear();
  });

  test("starts empty", () => {
    expect(cart.items).toHaveLength(0);
  });
});
```
