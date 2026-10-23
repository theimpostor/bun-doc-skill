# vitest/valid-expect
Source: https://bun.com/docs/lint/rules/vitest/valid-expect

Require `expect` to get a value, end in a called matcher, and be awaited when it is async


`expect(value)` doesn't check anything by itself. The check happens when a matcher such as `.toBe()` is called, so an `expect` with no matcher, or with a matcher that isn't called, passes no matter what the value is.

`.resolves` and `.rejects` make the matcher return a promise. If the test doesn't await or return it, the test can end first, and a failed assertion doesn't fail the test.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/valid-expect" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/valid-expect" = ["error", {
  alwaysAwait = false,
  asyncMatchers = ["toResolve", "toReject"],
  minArgs = 1,
  maxArgs = 1,
}]
```


## Examples

Reported:

```ts
import { expect, test } from "vitest";

test("adds the tax", () => {
  expect(total(100)); // no matcher
  expect(total(100)).toBe; // the matcher is not called
  expect().toBe(108); // no value
  expect(total(100)).never.toBe(0); // `never` is not a modifier
});
```

```ts
import { expect, test } from "vitest";

test("loads the user", () => {
  expect(loadUser(1)).resolves.toEqual({ id: 1 });
});
```

Not reported:

```ts
import { expect, test } from "vitest";

test("adds the tax", () => {
  expect(total(100)).toBe(108);
  expect(total(100)).not.toBe(0);
});

test("loads the user", async () => {
  await expect(loadUser(1)).resolves.toEqual({ id: 1 });
});

test("rejects an unknown id", () => {
  return expect(loadUser(-1)).rejects.toThrow("not found");
});
```

A second argument that's a string or a template literal is the message to print on failure. It doesn't count toward `maxArgs`:

```ts
import { expect, test } from "vitest";

test("adds the tax", () => {
  expect(total(100), "after tax").toBe(108);
});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `alwaysAwait` | `false` | Also report an async assertion that's returned instead of awaited. |
| `asyncMatchers` | `["toResolve", "toReject"]` | Matchers that return a promise, so they must be awaited or returned. Your list replaces the default. |
| `minArgs` | `1` | The fewest arguments `expect` can take. |
| `maxArgs` | `1` | The most arguments `expect` can take. |

```ts
import { expect, test } from "vitest";

test("rejects an unknown id", () => {
  return expect(loadUser(-1)).rejects.toThrow("not found");
});
```

Use `asyncMatchers` for custom matchers that return a promise:

```ts
import { expect, test } from "vitest";

test("loads the user", () => {
  expect(loadUser(1)).toResolveWith({ id: 1 });
});
```

A message that comes from a variable is reported. Raise `maxArgs` to allow it:

```ts
import { expect, test } from "vitest";

test("adds the tax", () => {
  expect(total(100), message).toBe(108);
});
```

```ts
import { expect, test } from "vitest";

test("adds the tax", () => {
  expect(total(100), message).toBe(108);
});
```
