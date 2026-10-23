# jest/no-test-return-statement
Source: https://bun.com/docs/lint/rules/jest/no-test-return-statement

Disallow `return expect(..)` in a test


The only thing worth returning from a test is a promise for Jest to wait for. A matcher such as `toBe()` returns nothing, so the `return` in `return expect(total).toBe(3)` has no effect. It only makes the test look like it waits for something.

The rule reports `return expect(..).matcher(..)` in a `test` or `it` callback, and in a function declaration that's passed to one of them. The matcher must be called directly on `expect(..)`. With `.resolves`, `.rejects` or `.not` in between, the `return` isn't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/no-test-return-statement" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "@jest/globals";

test("adds the prices", () => {
  const total = sum([1, 2]);
  return expect(total).toBe(3);
});
```

```ts
import { expect, test } from "@jest/globals";

test("adds the prices", addsThePrices);

function addsThePrices() {
  return expect(sum([1, 2])).toBe(3);
}
```

Not reported:

```ts
import { expect, test } from "@jest/globals";

test("adds the prices", () => {
  const total = sum([1, 2]);
  expect(total).toBe(3);
});
```

Other `return` statements aren't reported. That includes a returned promise, which Jest waits for:

```ts
import { expect, test } from "@jest/globals";

test("loads the prices", () => {
  return expect(loadPrices()).resolves.toEqual([1, 2]);
});

test("loads the taxes", () => {
  return loadTaxes().then(taxes => {
    expect(taxes).toEqual([0.2]);
  });
});
```

`jest/prefer-ending-with-an-expect` reports a test that ends with a `return`. With both rules on, write `await expect(..)` instead.
