# jest/prefer-comparison-matcher
Source: https://bun.com/docs/lint/rules/jest/prefer-comparison-matcher

Require matchers such as `toBeGreaterThan()` instead of comparing inside `expect()`


`expect(price < 100).toBe(true)` compares first and only hands `expect` the result. When it fails, the message says that `false` is not `true`, and you don't see the price. `expect(price).toBeLessThan(100)` prints both numbers.

The rule reports `>`, `>=`, `<` and `<=` inside `expect()` when the result is checked against `true` or `false` with `toBe()`, `toEqual()` or `toStrictEqual()`.

`--fix` rewrites the assertion.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/prefer-comparison-matcher" = "error" # or "warn"
```


## Examples

Reported:

```js
import { expect, test } from "@jest/globals";

test("applies the discount", () => {
  const price = discounted(100);
  expect(price < 100).toBe(true);
  expect(price < 0).toBe(false);
});
```

Not reported:

```js
import { expect, test } from "@jest/globals";

test("applies the discount", () => {
  const price = discounted(100);
  expect(price).toBeLessThan(100);
  expect(price).toBeGreaterThanOrEqual(0);
});
```

The comparison matchers only take numbers and bigints, so a comparison with a string literal or a template literal is left alone:

```js
import { expect, test } from "@jest/globals";

test("sorts after the first entry", () => {
  expect(lastName() > "Adams").toBe(true);
});
```

## When not to use it

The rule doesn't look at types, so it also reports comparisons of dates, or of strings held in variables. The comparison matchers throw on those values, and `--fix` rewrites the assertion anyway. This test is correct as written:

```js
import { expect, test } from "@jest/globals";

test("renewing extends the subscription", () => {
  expect(renewed.expiresAt > current.expiresAt).toBe(true);
});
```
