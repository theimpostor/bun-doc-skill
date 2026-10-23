# jest/prefer-to-have-length
Source: https://bun.com/docs/lint/rules/jest/prefer-to-have-length

Require `toHaveLength()` instead of comparing the `length` property


When `expect(users.length).toBe(2)` fails, the message shows two numbers. `expect(users).toHaveLength(2)` also prints the value it measured, so you see which items are missing or extra.

The rule reports `.length` inside `expect()` when the matcher is `toBe()`, `toEqual()`, or `toStrictEqual()`.

`--fix` rewrites the assertion.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/prefer-to-have-length" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "@jest/globals";

test("finds the active users", () => {
  const users = findUsers({ active: true });
  expect(users.length).toBe(2);
  expect(users[0].roles.length).not.toEqual(0);
});
```

Not reported:

```ts
import { expect, test } from "@jest/globals";

test("finds the active users", () => {
  const users = findUsers({ active: true });
  expect(users).toHaveLength(2);
  expect(users[0].roles).not.toHaveLength(0);
  expect(users.length).toBeGreaterThan(1);
});
```
