# jest/no-unneeded-async-expect-function
Source: https://bun.com/docs/lint/rules/jest/no-unneeded-async-expect-function

Disallow an async function around a single awaited call in `expect`


`.rejects` and `.resolves` work on a promise, so you can pass the call itself to `expect`. An async function that only awaits the call rejects with the same error, so the wrapper is extra code.

`--fix` replaces the function with the call. It leaves a function that has a comment in it alone, because the comment would be lost.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/no-unneeded-async-expect-function" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { expect, test } from "@jest/globals";

test("rejects an empty name", async () => {
  await expect(async () => {
    await saveUser({ name: "" });
  }).rejects.toThrow("name is required");

  await expect(async () => await saveUser({ name: "" })).rejects.toThrow();
});
```

Not reported:

```ts
import { expect, test } from "@jest/globals";

test("rejects an empty name", async () => {
  await expect(saveUser({ name: "" })).rejects.toThrow("name is required");
});
```

A function that does more than await one call isn't reported:

```ts
import { expect, test } from "@jest/globals";

test("rejects a second save", async () => {
  await expect(async () => {
    await saveUser({ name: "Ada" });
    await saveUser({ name: "Ada" });
  }).rejects.toThrow("name is taken");
});
```

## When not to use it

The two forms differ if the call can throw before it returns a promise. The async function turns that error into a rejection. Without the function, the error is thrown before `expect` runs.
