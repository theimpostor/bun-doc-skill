# bun:test/prefer-to-have-been-called
Source: https://bun.com/docs/lint/rules/bun-test/prefer-to-have-been-called

Require `not.toHaveBeenCalled()` instead of `toHaveBeenCalledTimes(0)`


`toHaveBeenCalledTimes(0)` means "not called", and `.not.toHaveBeenCalledTimes(0)` is a double negative for "called". `.not.toHaveBeenCalled()` and `toHaveBeenCalled()` say it directly.

The alias `toBeCalledTimes(0)` is reported too. Any other count is fine.

`--fix` rewrites both forms.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/prefer-to-have-been-called" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, mock, test } from "bun:test";

test("only notifies on failure", () => {
  const onError = mock();
  const onDone = mock();
  run(task, { onError, onDone });
  expect(onError).toHaveBeenCalledTimes(0);
  expect(onDone).not.toHaveBeenCalledTimes(0);
});
```

Not reported:

```ts
import { expect, mock, test } from "bun:test";

test("only notifies on failure", () => {
  const onError = mock();
  const onDone = mock();
  run(task, { onError, onDone });
  expect(onError).not.toHaveBeenCalled();
  expect(onDone).toHaveBeenCalled();
  expect(onDone).toHaveBeenCalledTimes(1);
});
```
