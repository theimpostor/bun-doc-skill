# vitest/require-awaited-expect-poll
Source: https://bun.com/docs/lint/rules/vitest/require-awaited-expect-poll

Require `expect.poll` and `expect.element` assertions to be awaited or returned


`expect.poll` and `expect.element` retry until the assertion holds, so they return a promise. If you don't await or return it, the test doesn't wait for it and ends before the assertion has a result.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/require-awaited-expect-poll" = "error" # or "warn"
```


## Examples

Reported:

```js
import { expect, test } from "vitest";

test("shows the saved message", () => {
  expect.poll(() => status.text).toBe("Saved");
  expect.element(banner).toBeVisible();
});
```

Not reported:

```js
import { expect, test } from "vitest";

test("shows the saved message", async () => {
  await expect.poll(() => status.text).toBe("Saved");
  await expect.element(banner).toBeVisible();
});

test("hides the spinner", () => {
  return expect.poll(() => spinner.hidden).toBe(true);
});
```

The `await` or `return` must be right in front of the assertion. An arrow function without braces and `Promise.all` are reported too:

```js
import { expect, test } from "vitest";

test("hides the spinner", () => expect.poll(() => spinner.hidden).toBe(true));
```

```js
import { expect, test } from "vitest";

test("saves both fields", async () => {
  await Promise.all([
    expect.poll(() => title.saved).toBe(true),
    expect.poll(() => body.saved).toBe(true),
  ]);
});
```
