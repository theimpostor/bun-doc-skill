# vitest/no-import-node-test
Source: https://bun.com/docs/lint/rules/vitest/no-import-node-test

Disallow importing from `node:test` in a project that uses Vitest


`node:test` exports `test`, `describe` and `it` too, so an editor's auto-import can pick it by mistake. Vitest doesn't collect tests registered with `node:test`, and reports that the file has no tests.

`--fix-suggestions` changes the source to `"vitest"`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"vitest/no-import-node-test" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { describe, it } from "node:test";

describe("slugify", () => {
  it("lowercases the title", () => {});
});
```

A re-export is reported too:

```ts
export { test } from "node:test";
```

Not reported:

```ts
import { describe, it } from "vitest";

describe("slugify", () => {
  it("lowercases the title", () => {});
});
```

## When not to use it

Turn it off for files that run under Node's own test runner on purpose.
