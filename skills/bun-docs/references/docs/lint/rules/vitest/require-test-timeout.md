# vitest/require-test-timeout
Source: https://bun.com/docs/lint/rules/vitest/require-test-timeout

Require every test to set a timeout


A test without its own timeout gets the default, which is 5 seconds unless your config changes it. That's a long wait when a unit test hangs, and it's too short for a test that starts a server, which then fails now and then on a slow machine.

Set the timeout as a number after the test function, as `{ timeout }` in the options before it, or for all the tests below with `vi.setConfig({ testTimeout })`.

Tests marked `.skip` or `.todo` aren't checked.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/require-test-timeout" = "error" # or "warn"
```


## Examples

Reported:

```js
import { expect, test } from "vitest";

test("loads the report", async () => {
  expect(await loadReport()).toBeDefined();
});
```

Not reported:

```js
import { expect, test } from "vitest";

test("loads the report", async () => {
  expect(await loadReport()).toBeDefined();
}, 10_000);

test("exports the report", { timeout: 30_000 }, async () => {
  expect(await exportReport()).toBeDefined();
});
```

```js
import { expect, test, vi } from "vitest";

vi.setConfig({ testTimeout: 10_000 });

test("loads the report", async () => {
  expect(await loadReport()).toBeDefined();
});
```

The timeout must be written as a number that isn't negative. A variable is reported, and so are options without `timeout`:

```js
import { test } from "vitest";

const SLOW = 30_000;

test("exports the report", async () => {
  await exportReport();
}, SLOW);

test("prints the report", { retry: 2 }, async () => {
  await printReport();
});
```

## When not to use it

If the default timeout, or the `testTimeout` in your Vitest config, suits all your tests, a number on each test adds nothing.
