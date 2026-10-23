# vitest/prefer-strict-boolean-matchers
Source: https://bun.com/docs/lint/rules/vitest/prefer-strict-boolean-matchers

Require `toBe(true)` and `toBe(false)` instead of `toBeTruthy()` and `toBeFalsy()`


`toBeTruthy()` passes for `1`, `"no"` and `{}`. `toBeFalsy()` passes for `0`, `""`, `null` and `undefined`. If a function should return a boolean and starts returning `undefined`, a test with `toBeFalsy()` still passes. `toBe(false)` fails.

`--fix` rewrites the matcher. A test that passed with a value that isn't a boolean fails afterwards.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-strict-boolean-matchers" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "vitest";

test("checks the password", () => {
  expect(isValid("correct horse")).toBeTruthy();
  expect(isValid("")).toBeFalsy();
});
```

Not reported:

```ts
import { expect, test } from "vitest";

test("checks the password", () => {
  expect(isValid("correct horse")).toBe(true);
  expect(isValid("")).toBe(false);
});
```

`not.toBeTruthy()` is reported too, and the rewrite is `not.toBe(true)`, which passes for everything except `true`. Write `toBe(false)` instead.

```ts
import { expect, test } from "vitest";

test("rejects an empty password", () => {
  expect(isValid("")).not.toBeTruthy();
});
```

## When not to use it

Some tests only care that there's a value, like a match from `String.prototype.match()` or a non-empty string. In those tests `toBeTruthy()` says what you mean.

`vitest/prefer-to-be-truthy` and `vitest/prefer-to-be-falsy` ask for the opposite. Don't turn them on together with this rule.
