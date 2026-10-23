# vitest/prefer-spy-on
Source: https://bun.com/docs/lint/rules/vitest/prefer-spy-on

Require `vi.spyOn()` instead of assigning `vi.fn()` to a property


`Date.now = vi.fn()` throws the real `Date.now` away. Unless you save it and put it back yourself, every test that runs afterwards gets the mock. `vi.spyOn(Date, "now")` remembers the original, so `mockRestore()` or `vi.restoreAllMocks()` brings it back.

`--fix-suggestions` rewrites `obj.save = vi.fn()` to `vi.spyOn(obj, 'save').mockImplementation()`. The `.mockImplementation()` is there because a spy calls the original function until you give it an implementation.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-spy-on" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { beforeEach, vi } from "vitest";

beforeEach(() => {
  Date.now = vi.fn(() => 1700000000000);
  console.warn = vi.fn();
});
```

Not reported:

```ts
import { afterEach, beforeEach, vi } from "vitest";

beforeEach(() => {
  vi.spyOn(Date, "now").mockImplementation(() => 1700000000000);
  vi.spyOn(console, "warn").mockImplementation(() => {});
});

afterEach(() => {
  vi.restoreAllMocks();
});
```

A mock that's stored in a variable or written in an object literal doesn't replace anything, so it isn't reported:

```ts
import { vi } from "vitest";

const onSave = vi.fn();
const logger = { warn: vi.fn() };
```
