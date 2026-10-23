# vitest/consistent-vitest-vi
Source: https://bun.com/docs/lint/rules/vitest/consistent-vitest-vi

Enforce one of `vi` or `vitest` for Vitest's helper object


Vitest exports its helper object under two names, `vi` and `vitest`. They're the same object. Using one name means a search for `vi.mock` finds every mock in the project.

By default the name is `vi`. Both the import and the calls are reported.

`--fix` renames the import and the calls.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/consistent-vitest-vi" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/consistent-vitest-vi" = ["error", {
  fn = "vi",
}]
```


## Examples

Reported:

```ts
import { expect, test, vitest } from "vitest";

test("calls the listener", () => {
  const listener = vitest.fn();
  emit("save", listener);
  expect(listener).toHaveBeenCalled();
});
```

Not reported:

```ts
import { expect, test, vi } from "vitest";

test("calls the listener", () => {
  const listener = vi.fn();
  emit("save", listener);
  expect(listener).toHaveBeenCalled();
});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `fn` | `"vi"` | The name to use: `"vi"` or `"vitest"`. |

With `"vitest"`, `vi` is reported:

```ts
import { vi } from "vitest";

vi.useFakeTimers();
```
