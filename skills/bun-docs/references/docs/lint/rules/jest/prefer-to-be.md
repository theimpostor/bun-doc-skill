# jest/prefer-to-be
Source: https://bun.com/docs/lint/rules/jest/prefer-to-be

Require `toBe()` for primitive literals, and `toBeNull()`, `toBeUndefined()`, `toBeNaN()`


`toEqual()` and `toStrictEqual()` compare objects property by property. For a string, a number or a boolean, they do the same check as `toBe()`, and `toBe()` tells the reader that you expect one plain value. `null`, `undefined` and `NaN` have matchers that name the value.

| Written | Use instead |
| --- | --- |
| `toEqual(2)`, `toStrictEqual("config")` | `toBe(2)`, `toBe("config")` |
| `toBe(null)`, `toEqual(null)` | `toBeNull()` |
| `toBe(undefined)`, `not.toBeDefined()` | `toBeUndefined()` |
| `not.toBe(undefined)`, `not.toBeUndefined()` | `toBeDefined()` |
| `toBe(NaN)`, `toEqual(NaN)` | `toBeNaN()` |

`--fix` rewrites the matcher.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/prefer-to-be" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "@jest/globals";

test("parses the header", () => {
  expect(header.version).toEqual(2);
  expect(header.name).toStrictEqual("config");
  expect(header.parent).toBe(null);
  expect(header.comment).not.toBeDefined();
  expect(header.size).not.toBe(undefined);
  expect(header.date).not.toBeUndefined();
  expect(header.ratio).toEqual(NaN);
});
```

Not reported:

```ts
import { expect, test } from "@jest/globals";

test("parses the header", () => {
  expect(header.version).toBe(2);
  expect(header.name).toBe("config");
  expect(header.parent).toBeNull();
  expect(header.comment).toBeUndefined();
  expect(header.size).toBeDefined();
  expect(header.date).toBeDefined();
  expect(header.ratio).toBeNaN();
});
```

Only literals count. Objects, arrays and variables are left alone:

```ts
import { expect, test } from "@jest/globals";

test("parses the body", () => {
  expect(body.tags).toEqual(["a", "b"]);
  expect(body.length).toEqual(expectedLength);
});
```
