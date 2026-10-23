# vitest/max-expects
Source: https://bun.com/docs/lint/rules/vitest/max-expects

Enforce a maximum number of `expect()` calls in a test


A test with many assertions usually checks several things at once. The first `expect` that fails stops the test, so it hides the failures after it, and the test's name no longer says what broke.

By default a test can have 5 `expect()` calls. Each call after that is reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/max-expects" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/max-expects" = ["error", {
  max = 5,
}]
```


## Examples

Reported:

```ts
import { expect, test } from "vitest";

test("creates a user", () => {
  const user = createUser({ name: "Ada", email: "ada@example.com" });
  expect(user.id).toBeGreaterThan(0);
  expect(user.name).toBe("Ada");
  expect(user.email).toBe("ada@example.com");
  expect(user.role).toBe("member");
  expect(user.active).toBe(true);
  expect(user.createdAt).toBeInstanceOf(Date);
});
```

Not reported:

```ts
import { expect, test } from "vitest";

test("keeps the name and the email", () => {
  const user = createUser({ name: "Ada", email: "ada@example.com" });
  expect(user).toMatchObject({ name: "Ada", email: "ada@example.com" });
});

test("fills in the defaults", () => {
  const user = createUser({ name: "Ada", email: "ada@example.com" });
  expect(user.id).toBeGreaterThan(0);
  expect(user.role).toBe("member");
  expect(user.active).toBe(true);
  expect(user.createdAt).toBeInstanceOf(Date);
});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `max` | `5` | The number of `expect()` calls allowed. |

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/max-expects" = ["error", { max = 2 }]
```

With `max = 2`, the third call is reported:

```ts
import { expect, test } from "vitest";

test("parses a URL", () => {
  const url = parse("https://example.com:8080/docs");
  expect(url.host).toBe("example.com");
  expect(url.port).toBe(8080);
  expect(url.path).toBe("/docs");
});
```

Calls are counted per function and per block. An `expect` inside a loop or a callback doesn't count toward the test around it, so this isn't reported:

```ts
import { expect, test } from "vitest";

test("lists active users", () => {
  const users = listUsers({ active: true });
  expect(users).toHaveLength(2);
  expect(users[0].name).toBe("Ada");
  for (const user of users) {
    expect(user.active).toBe(true);
  }
});
```
