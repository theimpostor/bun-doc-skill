# Delete files
Source: https://bun.com/docs/guides/runtime/delete-file


To delete a file, use `Bun.file(path).delete()`.

**File:** `delete-file.ts`
```ts
// Delete a file
const file = Bun.file("path/to/file.txt");
await file.delete();

// Now the file doesn't exist
const exists = await file.exists();
// => false
```

***

See [Docs > API > FileSystem](/runtime/file-io) for more filesystem operations.
