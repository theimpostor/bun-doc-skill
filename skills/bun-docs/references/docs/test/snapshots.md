# Snapshots
Source: https://bun.com/docs/test/snapshots

Learn how to use snapshot testing in Bun to save and compare output between test runs

Snapshot testing saves the output of a value and compares it against future test runs. Use it for UI components, complex objects, or any output that needs to remain consistent.

## Basic Snapshots

Write snapshot tests with the `.toMatchSnapshot()` matcher:

**File:** `test.ts`
```ts
import { test, expect } from "bun:test";

test("snap", () => {
  expect("foo").toMatchSnapshot();
});
```

The first time this test runs, Bun serializes the argument to `expect` and writes it to a snapshot file in a `__snapshots__` directory alongside the test file.

### Snapshot Files

After the first run, Bun creates:

**File:** `directory structure`
```text
your-project/
├── snap.test.ts
└── __snapshots__/
    └── snap.test.ts.snap
```

The snapshot file contains:

**File:** `__snapshots__/snap.test.ts.snap`
```ts
// Bun Snapshot v1, https://bun.sh/docs/test/snapshots

exports[`snap 1`] = `"foo"`;
```

On future runs, Bun compares the argument against the snapshot on disk.

## Updating Snapshots

Regenerate snapshots with:

```bash
bun test --update-snapshots
```

Do this when you've intentionally changed the output. In CI environments, Bun does not write new snapshots unless you pass this flag.

## Inline Snapshots

For smaller values, use `.toMatchInlineSnapshot()`. Bun stores inline snapshots directly in your test file:

**File:** `test.ts`
```ts
import { test, expect } from "bun:test";

test("inline snapshot", () => {
  // First run: snapshot will be inserted automatically
  expect({ hello: "world" }).toMatchInlineSnapshot();
});
```

After the first run, Bun automatically updates your test file:

**File:** `test.ts`
```ts
import { test, expect } from "bun:test";

test("inline snapshot", () => {
  expect({ hello: "world" }).toMatchInlineSnapshot(`
{
  "hello": "world",
}
`);
});
```

### Using Inline Snapshots

1. Write your test with `.toMatchInlineSnapshot()`
2. Run the test once
3. Bun automatically updates your test file with the snapshot
4. On subsequent runs, Bun compares the value against the inline snapshot

## Error Snapshots

You can also snapshot error messages with `.toThrowErrorMatchingSnapshot()` and `.toThrowErrorMatchingInlineSnapshot()`:

**File:** `test.ts`
```ts
import { test, expect } from "bun:test";

test("error snapshot", () => {
  expect(() => {
    throw new Error("Something went wrong");
  }).toThrowErrorMatchingSnapshot();

  expect(() => {
    throw new Error("Another error");
  }).toThrowErrorMatchingInlineSnapshot();
});
```

After running, the inline version becomes:

**File:** `test.ts`
```ts
test("error snapshot", () => {
  expect(() => {
    throw new Error("Something went wrong");
  }).toThrowErrorMatchingSnapshot();

  expect(() => {
    throw new Error("Another error");
  }).toThrowErrorMatchingInlineSnapshot(`"Another error"`);
});
```

## Advanced Snapshot Usage

### Complex Objects

Snapshots work well with complex nested objects:

**File:** `test.ts`
```ts
import { test, expect } from "bun:test";

test("complex object snapshot", () => {
  const user = {
    id: 1,
    name: "John Doe",
    email: "john@example.com",
    profile: {
      age: 30,
      preferences: {
        theme: "dark",
        notifications: true,
      },
    },
    tags: ["developer", "javascript", "bun"],
  };

  expect(user).toMatchSnapshot();
});
```

### Array Snapshots

Arrays are also well-suited for snapshot testing:

**File:** `test.ts`
```ts
import { test, expect } from "bun:test";

test("array snapshot", () => {
  const numbers = [1, 2, 3, 4, 5].map(n => n * 2);
  expect(numbers).toMatchSnapshot();
});
```

### Function Output Snapshots

Snapshot the output of functions:

**File:** `test.ts`
```ts
import { test, expect } from "bun:test";

function generateReport(data: any[]) {
  return {
    total: data.length,
    summary: data.map(item => ({ id: item.id, name: item.name })),
    timestamp: "2024-01-01", // Fixed for testing
  };
}

test("report generation", () => {
  const data = [
    { id: 1, name: "Alice", age: 30 },
    { id: 2, name: "Bob", age: 25 },
  ];

  expect(generateReport(data)).toMatchSnapshot();
});
```

## React Component Snapshots

Snapshots work well for React components:

**File:** `test.ts`
```tsx
import { test, expect } from "bun:test";
import { render } from "@testing-library/react";

function Button({ children, variant = "primary" }) {
  return <button className={`btn btn-${variant}`}>{children}</button>;
}

test("Button component snapshots", () => {
  const { container: primary } = render(<Button>Click me</Button>);
  const { container: secondary } = render(<Button variant="secondary">Cancel</Button>);

  expect(primary.innerHTML).toMatchSnapshot();
  expect(secondary.innerHTML).toMatchSnapshot();
});
```

## Property Matchers

For values that change between test runs (like timestamps or IDs), use property matchers:

**File:** `test.ts`
```ts
import { test, expect } from "bun:test";

test("snapshot with dynamic values", () => {
  const user = {
    id: Math.random(), // This changes every run
    name: "John",
    createdAt: new Date().toISOString(), // This also changes
  };

  expect(user).toMatchSnapshot({
    id: expect.any(Number),
    createdAt: expect.any(String),
  });
});
```

The snapshot file stores:

**File:** `snapshot file`
```txt
exports[`snapshot with dynamic values 1`] = `
{
  "createdAt": Any<String>,
  "id": Any<Number>,
  "name": "John",
}
`;
```

## Best Practices

### Keep Snapshots Small

**File:** `test.ts`
```ts
// Good: Focused snapshots
test("user name formatting", () => {
  const formatted = formatUserName("john", "doe");
  expect(formatted).toMatchInlineSnapshot(`"John Doe"`);
});

// Avoid: Huge snapshots that are hard to review
test("entire page render", () => {
  const page = renderEntirePage();
  expect(page).toMatchSnapshot(); // This could be thousands of lines
});
```

### Use Descriptive Test Names

**File:** `test.ts`
```ts
// Good: Clear what the snapshot represents
test("formats currency with USD symbol", () => {
  expect(formatCurrency(99.99)).toMatchInlineSnapshot(`"$99.99"`);
});

// Avoid: Unclear what's being tested
test("format test", () => {
  expect(format(99.99)).toMatchInlineSnapshot(`"$99.99"`);
});
```

### Group Related Snapshots

**File:** `test.ts`
```ts
import { describe, test, expect } from "bun:test";

describe("Button component", () => {
  test("primary variant", () => {
    expect(render(<Button variant="primary">Click</Button>))
      .toMatchSnapshot();
  });

  test("secondary variant", () => {
    expect(render(<Button variant="secondary">Cancel</Button>))
      .toMatchSnapshot();
  });

  test("disabled state", () => {
    expect(render(<Button disabled>Disabled</Button>))
      .toMatchSnapshot();
  });
});
```

### Handle Dynamic Data

**File:** `test.ts`
```ts
// Good: Normalize dynamic data
test("API response format", () => {
  const response = {
    data: { id: 1, name: "Test" },
    timestamp: Date.now(),
    requestId: generateId(),
  };

  expect({
    ...response,
    timestamp: "TIMESTAMP",
    requestId: "REQUEST_ID",
  }).toMatchSnapshot();
});

// Or use property matchers
test("API response with matchers", () => {
  const response = getApiResponse();

  expect(response).toMatchSnapshot({
    timestamp: expect.any(Number),
    requestId: expect.any(String),
  });
});
```

## Managing Snapshots

### Reviewing Snapshot Changes

When snapshots change, carefully review them:

```bash
# See what changed
git diff __snapshots__/

# Update if changes are intentional
bun test --update-snapshots

# Commit the updated snapshots
git add __snapshots__/
git commit -m "Update snapshots after UI changes"
```

### Organizing Large Snapshot Files

For large projects, consider organizing tests to keep snapshot files manageable:

**File:** `directory structure`
```text
tests/
├── components/
│   ├── Button.test.tsx
│   └── __snapshots__/
│       └── Button.test.tsx.snap
├── utils/
│   ├── formatters.test.ts
│   └── __snapshots__/
│       └── formatters.test.ts.snap
```

## Troubleshooting

### Snapshot Failures

When snapshots fail, Bun shows a diff:

**File:** `diff`
```diff
  {
-   "name": "John",
+   "name": "Jane",
  }

- Expected  - 1
+ Received  + 1
```

Common causes:

* Intentional changes (update with `--update-snapshots`)
* Unintentional changes (fix the code)
* Dynamic data (use property matchers)
* Environment differences (normalize the data)

### Platform Differences

Be aware of platform-specific differences:

**File:** `test.ts`
```ts
// Paths might differ between Windows/Unix
test("file operations", () => {
  const result = processFile("./test.txt");

  expect({
    ...result,
    path: result.path.replace(/\\/g, "/"), // Normalize paths
  }).toMatchSnapshot();
});
```
