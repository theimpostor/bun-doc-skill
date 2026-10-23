# bun:test/no-restricted-matchers
Source: https://bun.com/docs/lint/rules/bun-test/no-restricted-matchers

Disallow the matchers and modifiers you list


Some matchers are too loose for your tests. `toBeTruthy()` passes for `1`, `"no"` and `[]`, so it doesn't prove that a value is `true`. This rule reports the matchers and modifiers you list.

Without options it reports nothing.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/no-restricted-matchers" = "error" # or "warn"
```


## Examples

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/no-restricted-matchers" = ["error", {
  toBeTruthy = "Use toBe(true) instead",
}]
```

Reported:

```ts
import { expect, test } from "bun:test";

test("a new user is active", () => {
  const user = { active: true };
  expect(user.active).toBeTruthy();
});
```

Not reported:

```ts
import { expect, test } from "bun:test";

test("a new user is active", () => {
  const user = { active: true };
  expect(user.active).toBe(true);
});
```

## Options

The rule takes one object. Each key is what you write after `expect(..)`, joined with dots. Each value is a hint shown with the report, or `""` for no hint. In `bunfig.toml`, put quotes around a key with a dot, like `"not.toBe" = ""`.

| Key | What it reports |
| --- | --- |
| A matcher, such as `"toBe"` | `expect(a).toBe(b)`, but not `expect(a).not.toBe(b)`. |
| A chain, such as `"not.toBe"` | `expect(a).not.toBe(b)`, but not `expect(a).toBe(b)`. |
| `"not"`, `"resolves"`, `"rejects"`, or a chain that ends in `.not`, such as `"resolves.not"` | Every chain that starts with it. |

A matcher only matches when it's the whole chain, so `{ toBe = "" }` allows this:

```ts
import { expect, test } from "bun:test";

test("ids differ", () => {
  expect(createId()).not.toBe(createId());
});
```

A modifier matches whatever comes after it. With `{ resolves = "" }`, both lines are reported:

```ts
import { expect, test } from "bun:test";

test("loads the user", async () => {
  await expect(loadUser(1)).resolves.toEqual({ id: 1 });
  await expect(loadUser(2)).resolves.not.toBeNull();
});
```
