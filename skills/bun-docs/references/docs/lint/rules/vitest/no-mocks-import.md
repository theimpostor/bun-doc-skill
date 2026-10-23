# vitest/no-mocks-import
Source: https://bun.com/docs/lint/rules/vitest/no-mocks-import

Disallow importing from a `__mocks__` directory


Vitest picks up the files in `__mocks__` on its own when you call `vi.mock()`. Importing one by its path doesn't mock anything. The code under test still gets the real module, and your assertions look at a mock that nobody calls.

Import the real path and mock it. The test and the code under test then share the same mock.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/no-mocks-import" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "vitest";
import { sendEmail } from "./__mocks__/mailer";
import { register } from "./register";

test("sends a welcome email", () => {
  register("ada@example.com");
  expect(sendEmail).toHaveBeenCalled();
});
```

`require()` is checked too:

```js
const { sendEmail } = require("../__mocks__/mailer");
```

Not reported:

```ts
import { expect, test, vi } from "vitest";
import { sendEmail } from "./mailer";
import { register } from "./register";

vi.mock("./mailer");

test("sends a welcome email", () => {
  register("ada@example.com");
  expect(sendEmail).toHaveBeenCalled();
});
```
