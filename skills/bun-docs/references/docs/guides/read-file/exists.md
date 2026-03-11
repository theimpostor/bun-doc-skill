# Check if a file exists
Source: https://bun.com/docs/guides/read-file/exists


The `Bun.file()` function accepts a path and returns a `BunFile` instance. Use the `.exists()` method to check if a file exists at the given path.

**File:** `index.ts`
```ts
const path = "/path/to/package.json";
const file = Bun.file(path);

await file.exists(); // boolean;
```

***

Refer to [API > File I/O](/runtime/file-io) for more information on working with `BunFile`.
