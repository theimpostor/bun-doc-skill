# Get the absolute path of the current file
Source: https://bun.com/docs/guides/util/import-meta-path


Bun provides a handful of module-specific utilities on the [`import.meta`](/runtime/module-resolution#import-meta) object. Use `import.meta.path` to retrieve the absolute path of the current file.

**File:** `/a/b/c.ts`
```ts
import.meta.path; // => "/a/b/c.ts"
```

***

See [Docs > API > import.meta](/runtime/module-resolution#import-meta) for complete documentation.
