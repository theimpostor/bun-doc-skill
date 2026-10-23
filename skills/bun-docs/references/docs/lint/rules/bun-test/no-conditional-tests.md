# bun:test/no-conditional-tests
Source: https://bun.com/docs/lint/rules/bun-test/no-conditional-tests

Disallow `test` and `describe` inside an `if` statement


A test declared inside an `if` only exists when the condition is true. When it's false, the test is missing from the output, so nobody sees that it didn't run.

Use `test.if(condition)` or `test.skipIf(condition)`. That way the test is always declared, and it shows up as skipped when it doesn't run. `describe` has the same two methods.

This rule is about an `if` around a test. For an `if` inside a test, see `bun:test/no-conditional-in-test`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/no-conditional-tests" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "bun:test";

if (process.platform === "linux") {
  test("reads the kernel version", async () => {
    expect(await Bun.file("/proc/version").text()).toContain("Linux");
  });
}
```

```ts
import { describe, expect, test } from "bun:test";
import { connect } from "./database";

describe("database", () => {
  if (process.env.DATABASE_URL) {
    test("connects", async () => {
      expect(await connect()).toBeDefined();
    });
  }
});
```

Not reported:

```ts
import { expect, test } from "bun:test";

test.if(process.platform === "linux")("reads the kernel version", async () => {
  expect(await Bun.file("/proc/version").text()).toContain("Linux");
});
```

```ts
import { describe, expect, test } from "bun:test";
import { connect } from "./database";

describe.skipIf(!process.env.DATABASE_URL)("database", () => {
  test("connects", async () => {
    expect(await connect()).toBeDefined();
  });
});
```
