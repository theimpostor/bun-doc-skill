# Check if the current file is the entrypoint
Source: https://bun.com/docs/guides/util/entrypoint


Bun provides a handful of module-specific utilities on the [`import.meta`](/runtime/module-resolution#import-meta) object. Use `import.meta.main` to check if the current file is the entrypoint of the current process.

**File:** `index.ts`
```ts
if (import.meta.main) {
  // this file is directly executed with `bun run`
} else {
  // this file is being imported by another file
}
```

***

See [Docs > API > import.meta](/runtime/module-resolution#import-meta) for complete documentation.
