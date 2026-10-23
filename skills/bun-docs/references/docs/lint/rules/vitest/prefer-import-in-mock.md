# vitest/prefer-import-in-mock
Source: https://bun.com/docs/lint/rules/vitest/prefer-import-in-mock

Require `import()` instead of a string path in `vi.mock()` and `vi.doMock()`


TypeScript doesn't check a path that's written as a string. With `vi.mock(import("./api"))` it knows which module is mocked, so a wrong path is a type error and `importOriginal()` in the factory has the module's type.

`--fix` wraps the string in `import()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-import-in-mock" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/prefer-import-in-mock" = ["error", {
  fixable = true,
}]
```


## Examples

Reported:

```ts
import { vi } from "vitest";

vi.mock("./api", async importOriginal => {
  const api = await importOriginal();
  return { ...api, fetchUser: vi.fn() };
});
```

Not reported:

```ts
import { vi } from "vitest";

vi.mock(import("./api"), async importOriginal => {
  const api = await importOriginal();
  return { ...api, fetchUser: vi.fn() };
});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `fixable` | `true` | Set it to `false` to keep the report but leave the code alone with `--fix`. |

```ts
import { vi } from "vitest";

vi.doMock("./api");
```
