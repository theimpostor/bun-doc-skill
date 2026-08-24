# Use snapshot testing in `bun test`
Source: https://bun.com/docs/guides/test/snapshot


Bun's test runner supports Jest-style snapshot testing with `.toMatchSnapshot()`.

**File:** `snap.test.ts`
```ts
import { test, expect } from "bun:test";

test("snapshot", () => {
  expect({ foo: "bar" }).toMatchSnapshot();
});
```

***

The first time this test runs, Bun evaluates the value passed into `expect()` and writes it to a `__snapshots__` directory alongside the test file. (Note the `snapshots: +1 added` line in the output.)

```sh
bun test test/snap
```

```txt
test/snap.test.ts:
✓ snapshot [1.48ms]

 1 pass
 0 fail
 snapshots: +1 added
 1 expect() calls
Ran 1 test across 1 file. [82.00ms]
```

***

The `__snapshots__` directory contains a `.snap` file for each test file in the directory.

**File:** `File`
```txt
test
├── __snapshots__
│   └── snap.test.ts.snap
└── snap.test.ts
```

***

The `snap.test.ts.snap` file is a JavaScript file that exports a serialized version of the value passed into `expect()`. Bun pretty-prints the `{foo: "bar"}` object in Jest's snapshot format, which is not strict JSON (note the trailing comma).

**File:** `snap.test.ts.snap`
```js
// Bun Snapshot v1, https://bun.sh/docs/test/snapshots

exports[`snapshot 1`] = `
{
  "foo": "bar",
}
`;
```

***

On later runs, Bun reads the snapshot file and compares it to the value passed into `expect()`. If they differ, the test fails.

```sh
bun test
```

```txt
bun test v1.3.3 (9c68abdb)
test/snap.test.ts:
✓ snapshot [1.05ms]

 1 pass
 0 fail
 1 snapshots, 1 expect() calls
Ran 1 test across 1 file. [101.00ms]
```

***

To update snapshots, use the `--update-snapshots` flag.

```sh
bun test --update-snapshots
```

```txt
bun test v1.3.3 (9c68abdb)
test/snap.test.ts:
✓ snapshot [0.86ms]

 1 pass
 0 fail
 snapshots: +1 added  # the snapshot was regenerated
 1 expect() calls
Ran 1 test across 1 file. [102.00ms]
```

***

See [Snapshots](/docs/test/snapshots).
