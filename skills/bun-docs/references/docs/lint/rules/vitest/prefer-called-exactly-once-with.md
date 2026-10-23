# vitest/prefer-called-exactly-once-with
Source: https://bun.com/docs/lint/rules/vitest/prefer-called-exactly-once-with

Require `toHaveBeenCalledExactlyOnceWith()` over separate call count and argument checks


`toHaveBeenCalledOnce()` followed by `toHaveBeenCalledWith(...)` on the same mock takes two assertions to say one thing: the mock ran once, with these arguments. `toHaveBeenCalledExactlyOnceWith(...)` says it in one line.

The pair is reported when both assertions are in the same block, in either order. Assertions with `.not` are ignored.

`--fix-dangerously` replaces the pair with one `toHaveBeenCalledExactlyOnceWith(...)` call. `--fix` doesn't.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-called-exactly-once-with" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test, vi } from "vitest";

test("saves the draft", () => {
  const save = vi.fn();
  autosave("draft", save);
  expect(save).toHaveBeenCalledOnce();
  expect(save).toHaveBeenCalledWith("draft");
});
```

Not reported:

```ts
import { expect, test, vi } from "vitest";

test("saves the draft", () => {
  const save = vi.fn();
  autosave("draft", save);
  expect(save).toHaveBeenCalledExactlyOnceWith("draft");
});
```

A `mockClear()`, `mockReset()`, or `mockRestore()` on the mock between the two assertions means they're about different calls, so they aren't a pair:

```ts
import { expect, test, vi } from "vitest";

test("saves again after an edit", () => {
  const save = vi.fn();
  autosave("draft", save);
  expect(save).toHaveBeenCalledOnce();

  save.mockClear();
  autosave("edited", save);
  expect(save).toHaveBeenCalledWith("edited");
});
```
