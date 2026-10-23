# jest/no-confusing-set-timeout
Source: https://bun.com/docs/lint/rules/jest/no-confusing-set-timeout

Disallow `jest.setTimeout` inside a block, after a test, or more than once in a file


`jest.setTimeout` sets the timeout for the whole test file. A call inside a `describe` or a test looks like it only applies there, but it doesn't. With two calls in a file, it's hard to tell which one a given test gets.

The rule reports a `jest.setTimeout` call that's:

- not at the top level of the file
- after another Jest function such as `test` or `expect`
- not the first one in the file

To give one test more time, pass the timeout as the third argument to `test`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/no-confusing-set-timeout" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { describe, expect, jest, test } from "@jest/globals";
import { upload } from "./upload";

describe("upload", () => {
  jest.setTimeout(10_000);

  test("sends the file", async () => {
    expect(await upload("report.pdf")).toBe(true);
  });
});
```

```ts
import { jest } from "@jest/globals";

jest.setTimeout(5_000);
jest.setTimeout(10_000);
```

Not reported:

```ts
import { describe, expect, jest, test } from "@jest/globals";
import { upload } from "./upload";

jest.setTimeout(10_000);

describe("upload", () => {
  test("sends the file", async () => {
    expect(await upload("report.pdf")).toBe(true);
  });
});
```

```ts
import { expect, test } from "@jest/globals";
import { upload } from "./upload";

test("sends the file", async () => {
  expect(await upload("report.pdf")).toBe(true);
}, 10_000);
```
