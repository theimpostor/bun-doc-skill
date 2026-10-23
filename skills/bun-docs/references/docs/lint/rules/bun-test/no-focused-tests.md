# bun:test/no-focused-tests
Source: https://bun.com/docs/lint/rules/bun-test/no-focused-tests

Disallow `test.only` and `describe.only`


`.only` makes `bun test` run that test and skip every other one in the file. It's useful while debugging. If you commit one by accident, it hides failures in the tests that no longer run.

This rule is on by default in files that import from `"bun:test"`.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/no-focused-tests" = "off" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "bun:test";

test.only("adds", () => {
  expect(1 + 1).toBe(2);
});
```

Not reported:

```ts
import { expect, test } from "bun:test";

test("adds", () => {
  expect(1 + 1).toBe(2);
});
```
