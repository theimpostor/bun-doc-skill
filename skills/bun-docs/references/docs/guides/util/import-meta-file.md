# Get the file name of the current file
Source: https://bun.com/docs/guides/util/import-meta-file


Bun provides a handful of module-specific utilities on the [`import.meta`](/runtime/module-resolution#import-meta) object. Use `import.meta.file` to retrieve the name of the current file.

**File:** `/a/b/c.ts`
```ts
import.meta.file; // => "c.ts"
```

***

See [Docs > API > import.meta](/runtime/module-resolution#import-meta) for complete documentation.
