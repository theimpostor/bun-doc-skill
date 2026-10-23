# bun:test/prefer-each
Source: https://bun.com/docs/lint/rules/bun-test/prefer-each

Require `test.each` and `describe.each` instead of a loop around tests


`test.each` and `describe.each` take the list of cases as an argument and fill in the title for each one. A `for` loop around `test` does the same thing with more code, and you have to build every title by hand.

The rule reports `for`, `for...of` and `for...in` loops that contain a `test`, a `describe` or a hook such as `beforeEach`. A loop inside a test is fine. `while` loops and `cases.forEach(...)` around a test aren't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/prefer-each" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "bun:test";

const cases = [
  [1, 2],
  [2, 4],
];

for (const [input, expected] of cases) {
  test(`doubles ${input}`, () => {
    expect(input * 2).toBe(expected);
  });
}
```

Not reported:

```ts
import { expect, test } from "bun:test";

test.each([
  [1, 2],
  [2, 4],
])("doubles %i", (input, expected) => {
  expect(input * 2).toBe(expected);
});

test("every price is positive", () => {
  for (const price of [5, 10]) {
    expect(price).toBeGreaterThan(0);
  }
});
```
