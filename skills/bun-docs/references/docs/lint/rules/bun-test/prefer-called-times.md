# bun:test/prefer-called-times
Source: https://bun.com/docs/lint/rules/bun-test/prefer-called-times

Require `toHaveBeenCalledTimes(1)` instead of `toHaveBeenCalledOnce()`


`toHaveBeenCalledOnce()` and `toHaveBeenCalledTimes(1)` assert the same thing. With `toHaveBeenCalledTimes()`, every call count is written the same way, and changing the expected count means changing one number.

`--fix` rewrites the matcher.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/prefer-called-times" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, mock, test } from "bun:test";

test("does not retry after a success", () => {
  const request = mock();
  retryFetch(request);
  expect(request).toHaveBeenCalledOnce();
});
```

Not reported:

```ts
import { expect, mock, test } from "bun:test";

test("does not retry after a success", () => {
  const request = mock();
  retryFetch(request);
  expect(request).toHaveBeenCalledTimes(1);
});
```

## When not to use it

`bun:test/prefer-called-once` asks for the opposite. Turn on one of the two, not both.
