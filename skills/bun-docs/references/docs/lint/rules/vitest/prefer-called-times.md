# vitest/prefer-called-times
Source: https://bun.com/docs/lint/rules/vitest/prefer-called-times

Require `toHaveBeenCalledTimes(1)` instead of `toHaveBeenCalledOnce()`


`toHaveBeenCalledOnce()` and `toHaveBeenCalledTimes(1)` assert the same thing. With `toHaveBeenCalledTimes()`, every call count is written the same way, and changing the expected count means changing one number. The aliases are covered too, so `toBeCalledOnce()` becomes `toBeCalledTimes(1)`.

`--fix` rewrites the matcher.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-called-times" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test, vi } from "vitest";

test("does not retry after a success", () => {
  const request = vi.fn();
  retryFetch(request);
  expect(request).toHaveBeenCalledOnce();
});
```

Not reported:

```ts
import { expect, test, vi } from "vitest";

test("does not retry after a success", () => {
  const request = vi.fn();
  retryFetch(request);
  expect(request).toHaveBeenCalledTimes(1);
});
```

## When not to use it

`vitest/prefer-called-once` asks for the opposite. Turn on one of the two, not both.
