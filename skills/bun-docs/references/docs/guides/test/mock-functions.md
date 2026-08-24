# Mock functions in `bun test`
Source: https://bun.com/docs/guides/test/mock-functions


Create mocks with the `mock` function from `bun:test`.

**File:** `test.ts`
```ts
import { test, expect, mock } from "bun:test";

const random = mock(() => Math.random());
```

***

The mock function can accept arguments.

**File:** `test.ts`
```ts
import { test, expect, mock } from "bun:test";

const random = mock((multiplier: number) => multiplier * Math.random());
```

***

The result of `mock()` is a new function decorated with extra properties.

**File:** `test.ts`
```ts
import { mock } from "bun:test";

const random = mock((multiplier: number) => multiplier * Math.random());

random(2);
random(10);

random.mock.calls;
// [[ 2 ], [ 10 ]]

random.mock.results;
//  [
//    { type: "return", value: 0.6533907460954099 },
//    { type: "return", value: 0.6452713933037312 }
//  ]
```

***

Use these properties to write `expect` assertions about how the mock was used: how many times it was called, with which arguments, and what it returned.

**File:** `test.ts`
```ts
import { test, expect, mock } from "bun:test";

const random = mock((multiplier: number) => multiplier * Math.random());

test("random", async () => {
  const a = random(1);
  const b = random(2);
  const c = random(3);

  expect(random).toHaveBeenCalled();
  expect(random).toHaveBeenCalledTimes(3);
  expect(random.mock.calls).toEqual([[1], [2], [3]]);
  expect(random.mock.results[0]).toEqual({ type: "return", value: a });
});
```

***

See [Mocks](/docs/test/mocks).
