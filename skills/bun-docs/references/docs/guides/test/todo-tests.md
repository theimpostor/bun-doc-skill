# Mark a test as a "todo" with the Bun test runner
Source: https://bun.com/docs/guides/test/todo-tests


To remind yourself to write a test later, use the `test.todo` function. An implementation isn't required.

**File:** `test.test.ts`
```ts
import { test, expect } from "bun:test";

// write this later
test.todo("unimplemented feature");
```

***

The `bun test` output reports the number of `todo` tests.

```sh
bun test
```

```txt
test.test.ts:
✎ unimplemented feature

 0 pass
 1 todo
 0 fail
Ran 1 test across 1 file. [74.00ms]
```

***

You can provide a test implementation.

```ts
import { test, expect } from "bun:test";

test.todo("unimplemented feature", () => {
  expect(Bun.isAwesome()).toBe(true);
});
```

***

Bun doesn't run the implementation unless you pass the `--todo` flag. With `--todo`, the test runs and is *expected to fail*. If a todo test passes, `bun test` returns a non-zero exit code.

```sh
bun test --todo
```

```txt
test.test.ts:
✗ unimplemented feature
  ^ this test is marked as todo but passes. Remove `.todo` if tested behavior now works

 0 pass
 1 fail
 1 expect() calls
$ echo $?
1 # this is the exit code of the previous command
```

***

See also:

* [Skip a test](/docs/guides/test/skip-tests)
* [Writing tests](/docs/test/writing-tests)
