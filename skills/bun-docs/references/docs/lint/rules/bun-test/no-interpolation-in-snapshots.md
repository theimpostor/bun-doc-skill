# bun:test/no-interpolation-in-snapshots
Source: https://bun.com/docs/lint/rules/bun-test/no-interpolation-in-snapshots

Disallow `${}` in inline snapshots


An inline snapshot is text that `bun test` writes into your file and rewrites when you update snapshots. With `${}` in it, the expected text is computed while the test runs. The snapshot no longer shows what the output looks like, and `bun test --update-snapshots` can't rewrite it.

The rule checks the template literals passed to `toMatchInlineSnapshot` and `toThrowErrorMatchingInlineSnapshot`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/no-interpolation-in-snapshots" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "bun:test";

test("creates a user", () => {
  const user = createUser("Ada");
  expect(user).toMatchInlineSnapshot(`
    {
      "id": ${user.id},
      "name": "Ada",
    }
  `);
});
```

```ts
import { expect, test } from "bun:test";

test("rejects a missing file", () => {
  expect(() => load(path)).toThrowErrorMatchingInlineSnapshot(`"cannot read ${path}"`);
});
```

Not reported. For a value that changes from run to run, pass a property matcher as the first argument and keep the snapshot plain text:

```ts
import { expect, test } from "bun:test";

test("creates a user", () => {
  const user = createUser("Ada");
  expect(user).toMatchInlineSnapshot({ id: expect.any(Number) }, `
    {
      "id": Any<Number>,
      "name": "Ada",
    }
  `);
});
```
