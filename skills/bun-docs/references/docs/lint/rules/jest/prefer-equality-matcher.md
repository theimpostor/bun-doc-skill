# jest/prefer-equality-matcher
Source: https://bun.com/docs/lint/rules/jest/prefer-equality-matcher

Require `toBe` or `toEqual` instead of comparing with `===` inside `expect`


`expect(a === b).toBe(true)` compares the values before `expect` sees them. When the test fails, the output only says that `false` is not `true`. It doesn't show the two values.

The rule reports `===` and `!==` inside `expect` when the result is compared with `true` or `false` using `toBe`, `toEqual` or `toStrictEqual`. `==` and `!=` aren't reported.

`--fix-suggestions` rewrites the assertion with `toBe`. Your editor also offers `toEqual` and `toStrictEqual`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/prefer-equality-matcher" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "@jest/globals";

test("the session belongs to the user", () => {
  expect(session.userId === user.id).toBe(true);
  expect(user.role !== "admin").toBe(true);
});
```

Not reported:

```ts
import { expect, test } from "@jest/globals";

test("the session belongs to the user", () => {
  expect(session.userId).toBe(user.id);
  expect(user.role).not.toBe("admin");
});
```

```ts
import { expect, test } from "@jest/globals";

test("the port matches the string in the config", () => {
  expect(server.port == config.port).toBe(true);
});
```
