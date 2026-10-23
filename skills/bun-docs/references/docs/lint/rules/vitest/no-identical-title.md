# vitest/no-identical-title
Source: https://bun.com/docs/lint/rules/vitest/no-identical-title

Disallow two tests or two `describe` blocks with the same title in one block


When two tests in the same block share a title, a failure report doesn't tell you which one failed, and filtering by name runs both. The second one is often a copy that kept the old title.

Titles are compared inside one block. The same title in two different `describe` blocks is fine.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/no-identical-title" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { describe, expect, test } from "vitest";

describe("parsePrice", () => {
  test("reads a number", () => {
    expect(parsePrice("12")).toBe(12);
  });

  test("reads a number", () => {
    expect(parsePrice("12.50")).toBe(12.5);
  });
});
```

Two `describe` blocks next to each other are compared the same way:

```ts
import { describe, test } from "vitest";

describe("cart", () => {
  test("adds an item", () => {});
});

describe("cart", () => {
  test("removes an item", () => {});
});
```

Not reported:

```ts
import { describe, expect, test } from "vitest";

describe("parsePrice", () => {
  test("reads a whole number", () => {
    expect(parsePrice("12")).toBe(12);
  });

  test("reads a decimal", () => {
    expect(parsePrice("12.50")).toBe(12.5);
  });
});

describe("formatPrice", () => {
  test("reads a whole number", () => {
    expect(formatPrice(12)).toBe("12.00");
  });
});
```

The rule only compares titles that are plain strings. A title built from a variable is skipped, and so is `.each`, which fills in the title for each row:

```ts
import { expect, test } from "vitest";

test.each([1, 2])("doubles %i", n => {
  expect(double(n)).toBe(n * 2);
});

test.each([-1, -2])("doubles %i", n => {
  expect(double(n)).toBe(n * 2);
});

test("rounds " + mode, () => {});
test("rounds " + mode, () => {});
```
