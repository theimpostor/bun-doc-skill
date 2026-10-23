# vitest/no-restricted-vi-methods
Source: https://bun.com/docs/lint/rules/vitest/no-restricted-vi-methods

Disallow the `vi` methods you list


Some `vi` methods don't fit every project. `vi.mock()` replaces a whole module for the file, and your team might want tests to pass fakes in as arguments instead. This rule reports calls to the `vi` methods you list.

Without options it doesn't report anything.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/no-restricted-vi-methods" = "error" # or "warn"
```


## Examples

Both examples use `{ "mock": "Pass a fake as an argument instead" }`.

Reported:

```ts
import { vi } from "vitest";

vi.mock("./mailer");
```

Not reported:

```ts
import { expect, test, vi } from "vitest";
import { signUp } from "./sign-up";

test("sends a welcome mail", () => {
  const send = vi.fn();
  signUp("ada@example.com", { send });
  expect(send).toHaveBeenCalledTimes(1);
});
```

## Options

The rule takes one object. Each key is the name of a `vi` method. Each value is the message to report, or `null` for the default message, ``Use of `useFakeTimers` is not allowed``.

```json
{
  "rules": {
    "vitest/no-restricted-vi-methods": [
      "error",
      {
        "mock": "Pass a fake as an argument instead",
        "useFakeTimers": null
      }
    ]
  }
}
```
