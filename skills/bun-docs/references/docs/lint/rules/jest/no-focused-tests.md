# jest/no-focused-tests
Source: https://bun.com/docs/lint/rules/jest/no-focused-tests

Disallow `test.only`, `describe.only`, `fit` and `fdescribe`


`.only` makes Jest run that test and skip every other one in the file. It's useful while debugging. If you commit one by accident, it hides failures in the tests that no longer run.

The `f` prefix does the same thing, so `fit` and `fdescribe` are reported too.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/no-focused-tests" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, fit, test } from "@jest/globals";

test.only("adds", () => {
  expect(1 + 1).toBe(2);
});

fit("subtracts", () => {
  expect(2 - 1).toBe(1);
});
```

Not reported:

```ts
import { expect, it, test } from "@jest/globals";

test("adds", () => {
  expect(1 + 1).toBe(2);
});

it("subtracts", () => {
  expect(2 - 1).toBe(1);
});
```
