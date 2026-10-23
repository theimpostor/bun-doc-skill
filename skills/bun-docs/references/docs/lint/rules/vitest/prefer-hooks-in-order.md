# vitest/prefer-hooks-in-order
Source: https://bun.com/docs/lint/rules/vitest/prefer-hooks-in-order

Require hooks to be written in the order they run


Vitest runs hooks in a fixed order: `beforeAll`, `beforeEach`, `afterEach`, `afterAll`. If a file lists them in another order, you read the teardown before the setup it undoes.

Each `describe` block is checked on its own. The rule only compares hooks written one after another. Any other call between two hooks, such as a test, starts a new group.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-hooks-in-order" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { afterEach, beforeEach } from "vitest";

afterEach(() => {
  db.rollback();
});

beforeEach(() => {
  db.begin();
});
```

Not reported:

```ts
import { afterEach, beforeEach } from "vitest";

beforeEach(() => {
  db.begin();
});

afterEach(() => {
  db.rollback();
});
```

The test between these two hooks starts a new group, so this isn't reported. `vitest/prefer-hooks-on-top` reports it instead.

```ts
import { afterEach, beforeEach, test } from "vitest";

afterEach(() => {
  db.rollback();
});

test("saves a user", () => {
  db.save(user);
});

beforeEach(() => {
  db.begin();
});
```
