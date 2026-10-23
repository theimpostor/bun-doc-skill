# vitest/warn-todo
Source: https://bun.com/docs/lint/rules/vitest/warn-todo

Disallow `.todo` on `test`, `it` and `describe`


`test.todo` marks a test that nobody has written yet. It doesn't check anything and the run still passes, so it's easy to forget, and the behavior it names stays untested.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/warn-todo" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { describe, test } from "vitest";

test.todo("refunds the order");

describe.todo("checkout");
```

Not reported:

```ts
import { expect, test } from "vitest";

test("refunds the order", () => {
  expect(refund(order).total).toBe(0);
});
```

## When not to use it

If you use `.todo` to plan tests and read the list in the test output, this rule only repeats it.
