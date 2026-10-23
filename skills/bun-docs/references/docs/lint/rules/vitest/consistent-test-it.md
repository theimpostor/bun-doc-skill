# vitest/consistent-test-it
Source: https://bun.com/docs/lint/rules/vitest/consistent-test-it

Enforce one of `test` or `it` for defining tests


`test` and `it` are two names for the same function. When a project uses both at random, a reader wonders whether the difference means something. It doesn't.

By default, a test at the top level of a file uses `test`, and a test inside a `describe` uses `it`.

`--fix` renames the call. It doesn't change the import, so you need to import the new name yourself. It leaves a call alone if a variable around it has the new name.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/consistent-test-it" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/consistent-test-it" = ["error", {
  fn = "test",
  withinDescribe = "it",
}]
```


## Examples

Reported:

```ts
import { describe, expect, it, test } from "vitest";

it("adds", () => {
  expect(1 + 1).toBe(2);
});

describe("subtract", () => {
  test("goes below zero", () => {
    expect(1 - 2).toBe(-1);
  });
});
```

Not reported:

```ts
import { describe, expect, it, test } from "vitest";

test("adds", () => {
  expect(1 + 1).toBe(2);
});

describe("subtract", () => {
  it("goes below zero", () => {
    expect(1 - 2).toBe(-1);
  });
});
```

Forms such as `it.skip`, `it.only` and `it.each` are checked too:

```ts
import { expect, it } from "vitest";

it.skip("adds", () => {
  expect(1 + 1).toBe(2);
});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `fn` | `"test"` | The name for tests at the top level of a file: `"test"` or `"it"`. |
| `withinDescribe` | the value of `fn` if you set it, otherwise `"it"` | The name for tests inside a `describe`. |

To use `test` everywhere, only set `fn`:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/consistent-test-it" = ["error", { fn = "test" }]
```

Then `it` inside a `describe` is reported too:

```ts
import { describe, expect, it } from "vitest";

describe("subtract", () => {
  it("goes below zero", () => {
    expect(1 - 2).toBe(-1);
  });
});
```
