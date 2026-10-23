# bun:test/require-top-level-describe
Source: https://bun.com/docs/lint/rules/bun-test/require-top-level-describe

Require tests and hooks to be inside a `describe` block


A test at the top level of a file shows up in the output with no group name, so a failure says "starts empty" but not what starts empty. A hook at the top level runs for every test in the file, including the ones somebody adds later for something else. Inside a `describe`, both say what they belong to.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/require-top-level-describe" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/require-top-level-describe" = ["error", {
  # maxNumberOfTopLevelDescribes = <number>,
}]
```


## Examples

Reported:

```ts
import { beforeEach, expect, test } from "bun:test";

beforeEach(() => {
  cart.clear();
});

test("starts empty", () => {
  expect(cart.size).toBe(0);
});
```

Not reported:

```ts
import { beforeEach, describe, expect, test } from "bun:test";

describe("cart", () => {
  beforeEach(() => {
    cart.clear();
  });

  test("starts empty", () => {
    expect(cart.size).toBe(0);
  });
});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `maxNumberOfTopLevelDescribes` | no limit | How many `describe` blocks a file can have at the top level. Each one after that is reported. Nested blocks don't count. |

```ts
import { describe, test } from "bun:test";

describe("cart", () => {
  test.todo("starts empty");
});

describe("checkout", () => {
  test.todo("charges the card");
});
```

```ts
import { describe, test } from "bun:test";

describe("shop", () => {
  describe("cart", () => {
    test.todo("starts empty");
  });

  describe("checkout", () => {
    test.todo("charges the card");
  });
});
```
