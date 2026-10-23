# jest/prefer-to-have-been-called-times
Source: https://bun.com/docs/lint/rules/jest/prefer-to-have-been-called-times

Require `toHaveBeenCalledTimes()` instead of checking the length of `mock.calls`


When `expect(save.mock.calls).toHaveLength(2)` fails, the message is about the length of an array. `expect(save).toHaveBeenCalledTimes(2)` says what the test means, and its failure message shows the expected and received number of calls.

`--fix` rewrites the assertion.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/prefer-to-have-been-called-times" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, jest, test } from "@jest/globals";

test("saves each item once", () => {
  const save = jest.fn();
  saveAll(["a", "b"], save);
  expect(save.mock.calls).toHaveLength(2);
});
```

Not reported:

```ts
import { expect, jest, test } from "@jest/globals";

test("saves each item once", () => {
  const save = jest.fn();
  saveAll(["a", "b"], save);
  expect(save).toHaveBeenCalledTimes(2);
  expect(save.mock.calls[0]).toHaveLength(1); // the arguments of the first call
});
```
