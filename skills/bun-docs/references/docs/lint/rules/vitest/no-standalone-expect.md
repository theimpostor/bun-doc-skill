# vitest/no-standalone-expect
Source: https://bun.com/docs/lint/rules/vitest/no-standalone-expect

Disallow `expect` outside of a `test` or `it` block


An `expect` directly in a `describe` block or at the top of the file isn't part of any test. It runs while the file loads, before the first test starts, so a failure doesn't show up as a failed test. Usually someone forgot the `test(..)` around it. An `expect` in a hook such as `beforeEach` is reported too.

An `expect` in a function declaration, or in a function assigned to a variable, is allowed, because a test can call that helper. So are `expect.extend()` and asymmetric matchers such as `expect.any(String)`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/no-standalone-expect" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/no-standalone-expect" = ["error", {
  additionalTestBlockFunctions = [], # list of strings
}]
```


## Examples

Reported:

```ts
import { beforeEach, describe, expect } from "vitest";

describe("cart", () => {
  const cart = createCart();
  expect(cart.items).toHaveLength(0);

  beforeEach(() => {
    expect(cart.total).toBe(0);
  });
});
```

Not reported:

```ts
import { describe, expect, test } from "vitest";

function expectEmpty(cart: Cart) {
  expect(cart.items).toHaveLength(0);
}

describe("cart", () => {
  test("starts empty", () => {
    const cart = createCart();
    expectEmpty(cart);
    expect(cart.total).toBe(0);
  });
});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `additionalTestBlockFunctions` | `[]` | Names of other functions to treat like `test`. An `expect` in a callback passed to one of them is allowed. |

Use it for your own wrappers around `test`, or to allow `expect` in a hook. A name can have dots.

```ts
import { beforeEach, expect } from "vitest";

beforeEach(() => {
  expect(database.isConnected()).toBe(true);
});

admin.test("can delete a user", () => {
  expect(deleteUser(1)).toBe(true);
});
```
