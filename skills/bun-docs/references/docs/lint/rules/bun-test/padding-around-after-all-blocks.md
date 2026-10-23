# bun:test/padding-around-after-all-blocks
Source: https://bun.com/docs/lint/rules/bun-test/padding-around-after-all-blocks

Require a blank line before each `afterAll` call


An `afterAll` hook that sits right under another statement is easy to miss when you're looking for a file's cleanup code. A blank line above it sets it apart.

Only the line above the call is checked, not the line below. Comments directly above the call count as part of it, so the blank line goes above them. An `afterAll` that comes first in a file or in a `describe` callback doesn't need a blank line.

`--fix` inserts the blank line.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/padding-around-after-all-blocks" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { afterAll, describe } from "bun:test";

describe("database", () => {
  const db = connect();
  afterAll(() => db.close());
});
```

Two `afterAll` calls in a row need a blank line between them too:

```ts
import { afterAll } from "bun:test";

const server = startServer();
afterAll(() => server.stop());
afterAll(() => removeTempFiles());
```

Not reported:

```ts
import { afterAll, describe } from "bun:test";

describe("database", () => {
  const db = connect();

  // Close the connection so the process can exit.
  afterAll(() => db.close());
});
```
