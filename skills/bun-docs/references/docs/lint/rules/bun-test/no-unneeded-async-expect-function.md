# bun:test/no-unneeded-async-expect-function
Source: https://bun.com/docs/lint/rules/bun-test/no-unneeded-async-expect-function

Disallow an async function around a single awaited call in `expect`


`.rejects` and `.resolves` work on a promise. `bun test` doesn't call a function for them, so an async function in `expect` fails with `Expected promise`. Pass the call itself.

`--fix` replaces the function with the call. It leaves a function that has a comment in it alone, because the comment would be lost.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/no-unneeded-async-expect-function" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "bun:test";

test("rejects an empty name", async () => {
  await expect(async () => {
    await saveUser({ name: "" });
  }).rejects.toThrow("name is required");

  await expect(async () => await saveUser({ name: "" })).rejects.toThrow();
});
```

Not reported:

```ts
import { expect, test } from "bun:test";

test("rejects an empty name", async () => {
  await expect(saveUser({ name: "" })).rejects.toThrow("name is required");
});
```

Without `.rejects` or `.resolves` the function is needed, so it isn't reported. `toThrow` calls it and waits for its promise. Given the promise itself, it fails with `Expected value must be a function`:

```ts
import { expect, test } from "bun:test";

test("rejects an empty name", () => {
  expect(async () => {
    await saveUser({ name: "" });
  }).toThrow("name is required");
});
```

That form also catches an error that the call throws before it returns a promise. Without the function, such an error is thrown before `expect` runs.
