# bun:test/max-nested-describe
Source: https://bun.com/docs/lint/rules/bun-test/max-nested-describe

Enforce a maximum depth of nested `describe()` calls


Every level of `describe` can add its own hooks and variables. To understand a test that sits many levels deep, you have to read all the blocks around it, and the test's full name gets long.

By default `describe` blocks can be 5 levels deep. Any `describe` nested deeper than that is reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/max-nested-describe" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/max-nested-describe" = ["error", {
  max = 5,
}]
```


## Examples

These examples use a maximum of 2:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/max-nested-describe" = ["error", { max = 2 }]
```

Reported:

```ts
import { describe, expect, test } from "bun:test";

describe("cart", () => {
  describe("checkout", () => {
    describe("with a coupon", () => {
      test("lowers the total", () => {
        expect(checkout({ coupon: "SAVE10" }).total).toBe(90);
      });
    });
  });
});
```

Not reported:

```ts
import { describe, expect, test } from "bun:test";

describe("cart", () => {
  describe("checkout", () => {
    test("a coupon lowers the total", () => {
      expect(checkout({ coupon: "SAVE10" }).total).toBe(90);
    });
  });
});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `max` | `5` | The number of levels allowed. |
