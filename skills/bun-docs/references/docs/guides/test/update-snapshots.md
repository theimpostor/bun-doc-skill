# Update snapshots in `bun test`
Source: https://bun.com/docs/guides/test/update-snapshots


Bun's test runner supports Jest-style snapshot testing with `.toMatchSnapshot()`.

**File:** `snap.test.ts`
```ts
import { test, expect } from "bun:test";

test("snapshot", () => {
  expect({ foo: "bar" }).toMatchSnapshot();
});
```

***

The first time this test runs, Bun writes a snapshot file to a `__snapshots__` directory alongside the test file.

**File:** `File`
```txt
test
├── __snapshots__
│   └── snap.test.ts.snap
└── snap.test.ts
```

***

To regenerate snapshots, use the `--update-snapshots` flag.

```sh
bun test --update-snapshots
```

```txt
test/snap.test.ts:
✓ snapshot [0.86ms]

 1 pass
 0 fail
 snapshots: +1 added # the snapshot was regenerated
 1 expect() calls
Ran 1 test across 1 file. [102.00ms]
```

***

See [Snapshots](/docs/test/snapshots).
