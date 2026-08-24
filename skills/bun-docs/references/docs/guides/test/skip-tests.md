# Skip tests with the Bun test runner
Source: https://bun.com/docs/guides/test/skip-tests


To skip a test with the Bun test runner, use the `test.skip` function.

**File:** `test.test.ts`
```ts
import { test, expect } from "bun:test";

test.skip("unimplemented feature", () => {
  expect(Bun.isAwesome()).toBe(true);
});
```

***

Running `bun test` doesn't execute this test. The terminal output marks it as skipped.

```sh
bun test
```

```txt
test.test.ts:
» unimplemented feature

 0 pass
 1 skip
 0 fail
Ran 1 test across 1 file. [74.00ms]
```

***

See also:

* [Mark a test as a todo](/docs/guides/test/todo-tests)
* [Writing tests](/docs/test/writing-tests)
