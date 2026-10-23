# vitest/prefer-called-once
Source: https://bun.com/docs/lint/rules/vitest/prefer-called-once

Require `toHaveBeenCalledOnce()` instead of `toHaveBeenCalledTimes(1)`


`toHaveBeenCalledTimes(1)` and `toHaveBeenCalledOnce()` assert the same thing. This rule picks the shorter one, so the whole project writes it the same way. The aliases are covered too, so `toBeCalledTimes(1)` becomes `toBeCalledOnce()`.

`--fix` rewrites the matcher.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-called-once" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test, vi } from "vitest";

test("notifies the listener", () => {
  const listener = vi.fn();
  publish("ready", listener);
  expect(listener).toHaveBeenCalledTimes(1);
});
```

Not reported:

```ts
import { expect, test, vi } from "vitest";

test("notifies the listener", () => {
  const listener = vi.fn();
  publish("ready", listener);
  expect(listener).toHaveBeenCalledOnce();

  publish("done", listener);
  expect(listener).toHaveBeenCalledTimes(2);
});
```

## When not to use it

`vitest/prefer-called-times` asks for the opposite. Turn on one of the two, not both.
