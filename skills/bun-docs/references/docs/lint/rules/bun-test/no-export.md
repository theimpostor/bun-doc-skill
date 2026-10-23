# bun:test/no-export
Source: https://bun.com/docs/lint/rules/bun-test/no-export

Disallow exports from a file that has tests


When another file imports from a test file, the whole test file runs, including its `test()` calls, so its tests can run as part of the importing file. Put shared helpers in their own file.

The rule only checks files named like tests. That means the name ends in `test` or `spec` before the extension, such as `cart.test.ts`, or the file is under a `__tests__` directory. A file with no `test` or `it` call can export anything. Exported types are allowed, because importing a type doesn't run the file.

This rule is on by default in files that import from `"bun:test"`.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/no-export" = "off" # or "error"
```


## Examples

Reported:

```ts
import { expect, test } from "bun:test";

export function makeCart() {
  return { items: [] };
}

test("starts empty", () => {
  expect(makeCart().items).toEqual([]);
});
```

Not reported, with the helper in its own file:

```ts
export function makeCart() {
  return { items: [] };
}
```

```ts
import { expect, test } from "bun:test";
import { makeCart } from "./helpers";

export type Cart = ReturnType<typeof makeCart>;

test("starts empty", () => {
  expect(makeCart().items).toEqual([]);
});
```
