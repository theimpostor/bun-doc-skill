# bun:test/no-test-prefixes
Source: https://bun.com/docs/lint/rules/bun-test/no-test-prefixes

Require `.skip` instead of the `x` prefix


`xit`, `xtest` and `xdescribe` are short names for `it.skip`, `test.skip` and `describe.skip`. One extra letter is easy to miss in a review, and a search for `.skip` doesn't find it.

`--fix` rewrites the short name only if the file already imports the long one. For example, `xtest` becomes `test.skip` if `test` is imported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/no-test-prefixes" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, xdescribe, xtest } from "bun:test";

xtest("subtracts", () => {
  expect(3 - 1).toBe(2);
});

xdescribe("division", () => {});
```

Not reported:

```ts
import { describe, expect, test } from "bun:test";

test.skip("subtracts", () => {
  expect(3 - 1).toBe(2);
});

describe.skip("division", () => {});
```

`xit.each` is reported too. Write `it.skip.each`:

```ts
import { expect, xit } from "bun:test";

xit.each([1, 2, 3])("%i is positive", n => {
  expect(n).toBeGreaterThan(0);
});
```
