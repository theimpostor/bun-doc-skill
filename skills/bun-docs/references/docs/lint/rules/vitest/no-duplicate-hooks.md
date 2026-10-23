# vitest/no-duplicate-hooks
Source: https://bun.com/docs/lint/rules/vitest/no-duplicate-hooks

Disallow using the same hook twice in one `describe` block


Two `beforeEach` calls in the same block both run, so nothing fails. But someone who reads the first one assumes it's all the setup and misses the second, which can be many lines below.

Hooks are counted per `describe` block, and the top level of the file counts as a block. A nested `describe` can have its own `beforeEach`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/no-duplicate-hooks" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { beforeEach, describe, test } from "vitest";

describe("cart", () => {
  beforeEach(() => {
    cart.clear();
  });

  test("starts empty", () => {});

  beforeEach(() => {
    cart.add("apple");
  });
});
```

Not reported:

```ts
import { beforeEach, describe, test } from "vitest";

describe("cart", () => {
  beforeEach(() => {
    cart.clear();
    cart.add("apple");
  });

  test("has one item", () => {});

  describe("after checkout", () => {
    beforeEach(() => {
      cart.checkout();
    });

    test("is empty", () => {});
  });
});
```
